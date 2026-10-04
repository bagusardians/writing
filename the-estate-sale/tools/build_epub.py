#!/usr/bin/env python3
"""Build an EPUB 3 for The Estate Sale from the built markdown."""
import re, os, sys, uuid, html, zipfile, datetime

SRC = sys.argv[1]
OUT = sys.argv[2]

raw = open(SRC, encoding="utf-8").read()

# --- split into units on <!-- filename.md --> markers -------------------------
parts = re.split(r"<!--\s*([0-9A-Za-z\-_.]+\.md)\s*-->", raw)
# parts[0] is preamble (usually empty); then name, body, name, body...
units = []
for i in range(1, len(parts) - 1, 2):
    name, body = parts[i], parts[i + 1]
    m = re.search(r"^#\s+(.*)$", body, flags=re.M)
    title = m.group(1).strip() if m else name
    if m:
        body = body[: m.start()] + body[m.end():]
    units.append((name, title, body.strip()))

# --- inline markdown ----------------------------------------------------------
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<em>\1</em>", t)
    return t

def render_block(block):
    block = block.strip()
    if not block:
        return ""
    if block == "---":
        return '<p class="scene">&#42;&#160;&#42;&#160;&#42;</p>'
    if block.startswith("[IMAGE") and block.endswith("]"):
        inner = inline(block[1:-1].strip())  # drop the brackets, keep "IMAGE 00.1 — ..."
        return f'<p class="plate">{inner}</p>'
    if block.startswith("*[") and block.endswith("]*"):
        inner = inline(block[2:-2].strip())
        return f'<p class="note"><em>{inner}</em></p>'
    return "<p>" + inline(block.replace("\n", " ")) + "</p>"

def render_body(body):
    blocks = re.split(r"\n\s*\n", body)
    return "\n".join(filter(None, (render_block(b) for b in blocks)))

CSS = """@charset "utf-8";
body { font-family: serif; line-height: 1.5; margin: 0 5%; text-align: left; }
h1 { font-family: sans-serif; font-size: 1.5em; text-align: center;
     margin: 2em 0 1.5em; page-break-before: always; }
h1.first { page-break-before: avoid; }
p { margin: 0 0 0.6em; text-indent: 1.2em; }
p.first { text-indent: 0; }
p.scene { text-align: center; text-indent: 0; margin: 1em 0; letter-spacing: 0.3em; }
p.plate { text-indent: 0; font-family: sans-serif; font-size: 0.82em; color: #555;
          border-left: 3px solid #bbb; padding: 0.3em 0.7em; margin: 1em 0; }
p.note { text-indent: 0; font-size: 0.92em; color: #333; margin: 1em 0; }
.titlepage { text-align: center; margin-top: 25%; }
.titlepage h1 { font-size: 2.2em; }
.titlepage .sub { font-style: italic; margin-top: 1em; }
.titlepage .by { margin-top: 2em; }
"""

def xhtml(title, body, first=False):
    cls = ' class="first"' if first else ""
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head><meta charset="utf-8"/><title>{html.escape(title)}</title>
<link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
<h1{cls}>{html.escape(title)}</h1>
{body}
</body></html>"""

# --- assemble chapters --------------------------------------------------------
chapters = []
titlepage = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head><meta charset="utf-8"/><title>The Estate Sale</title>
<link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
<div class="titlepage">
<h1 class="first">The Estate Sale</h1>
<p class="sub">An interlocking anthology of the dead</p>
<p class="by">bagusardians</p>
</div>
</body></html>"""
chapters.append(("titlepage", "Title Page", titlepage))

for idx, (name, title, body) in enumerate(units):
    body_html = render_body(body)
    # first paragraph of a unit gets no indent
    body_html = body_html.replace('<p>', '<p class="first">', 1)
    fid = "ch%02d" % idx
    chapters.append((fid, title, xhtml(title, body_html)))

bookid = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, "estate-sale-bagusardians"))
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

manifest = ['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
            '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
            '<item id="css" href="style.css" media-type="text/css"/>']
spine = []
for fid, title, _ in chapters:
    manifest.append(f'<item id="{fid}" href="{fid}.xhtml" media-type="application/xhtml+xml"/>')
    spine.append(f'<itemref idref="{fid}"/>')

opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="bookid">{bookid}</dc:identifier>
<dc:title>The Estate Sale</dc:title>
<dc:creator>bagusardians</dc:creator>
<dc:language>en</dc:language>
<dc:description>An interlocking anthology horror-mystery set in present-day Tokyo.</dc:description>
<meta property="dcterms:modified">{now}</meta>
</metadata>
<manifest>
{chr(10).join(manifest)}
</manifest>
<spine toc="ncx">
{chr(10).join(spine)}
</spine>
</package>"""

nav_items = "\n".join(
    f'<li><a href="{fid}.xhtml">{html.escape(title)}</a></li>' for fid, title, _ in chapters
)
nav = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops"
 xml:lang="en" lang="en">
<head><meta charset="utf-8"/><title>Contents</title></head>
<body>
<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>
{nav_items}
</ol></nav>
</body></html>"""

points = "\n".join(
    f'<navPoint id="np{fid}" playOrder="{i+1}"><navLabel><text>{html.escape(title)}</text>'
    f'</navLabel><content src="{fid}.xhtml"/></navPoint>'
    for i, (fid, title, _) in enumerate(chapters)
)
ncx = f"""<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="{bookid}"/></head>
<docTitle><text>The Estate Sale</text></docTitle>
<navMap>
{points}
</navMap>
</ncx>"""

container = """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf"
 media-type="application/oebps-package+xml"/></rootfiles></container>"""

# --- write epub ---------------------------------------------------------------
os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
with zipfile.ZipFile(OUT, "w") as z:
    z.writestr("mimetype", "application/epub+zip", zipfile.ZIP_STORED)
    z.writestr("META-INF/container.xml", container, zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/content.opf", opf, zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/nav.xhtml", nav, zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/toc.ncx", ncx, zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/style.css", CSS, zipfile.ZIP_DEFLATED)
    for fid, title, content in chapters:
        z.writestr(f"OEBPS/{fid}.xhtml", content, zipfile.ZIP_DEFLATED)

print(f"wrote {OUT}: {len(chapters)} documents, {len(units)} units")
