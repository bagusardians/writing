# The Estate Sale — v1.4.0

**Status:** Final release (current).
**Manuscript:** `the-estate-sale-v1.4.0.md`
**Word count:** 44,955 excluding image prompts (v1.3.0, same method: 44,955; delta 0 — prose unchanged).
**Plates:** 135 (v1.3.0: 135 markers across 122 labels; v1.4.0: 135 markers across 135 labels).
**Structure:** 22 units across three movements (survey, chain, convergence).

## Changes since v1.3.0

An illustration-specification pass. No prose changed; the only manuscript edit is the plate
numbering.

1. **Plate labels are now unique across the whole book.** v1.3.0 inherited a numbering fault:
   the manuscript used one scheme (a running number that restarted at `1` and collided, so
   `7.1`–`7.5` appeared in both The Ledger and the Interlude, and `9.1`–`9.7` in both Frame
   Three and The Tea Set), while the prompt sheet used a different scheme. Labels are now
   `<chapter>.<plate>`, unique and stable, identical in the manuscript caption and the sheet.
   Colliding and lettered labels (`6.2b`, `7.4b`, `11.2b`, `20.1b`) are gone.
2. **Every illustration prompt is standalone.** Each entry in
   `phase-8-visuals/illustration-prompts.md` now restates the full house style, the world
   anchors, the negative prompt, and the chapter's continuity anchors, so any single prompt can
   be pasted into an image model on its own.
3. **The sheet is fully structured.** Each plate is a short block (medium / aspect, subject,
   camera, light, chapter anchors, avoid) followed by a single-paragraph full prompt.
4. **Sheet and manuscript are reconciled.** Every one of the 135 captions in the manuscript has
   exactly one entry in the sheet, and vice versa; verified programmatically.

## What this release does not change

The prose, voice, structure, chapter titles, and the story are unchanged from v1.3.0. The
manuscript edit is confined to the `[IMAGE ...]` caption labels.

## Contents

The assembled manuscript, in reading order. Source chapter files live in
`../../phase-6-draft/chapters/`; the phase artifacts that produced them live in the sibling
`phase-*` folders.

## What "final" means here

- All eight pipeline phases produced an artifact; the revision rationale is recorded here.
- Word count verified by the assembly script; the release is byte-identical to a fresh
  assembly of the chapter files.
- Illustrations are specified (135 plates) but not generated.

## Known carried items

1. The finder is intentionally unnamed.
2. Real-place texture references: Yanaka Ginza, Setagaya Bōro-ichi.
3. The final line's date is "today"; it needs handling if the book is ever dated.
4. The consecutive case chapters still share a discovery beat; a future pass may compress them.
