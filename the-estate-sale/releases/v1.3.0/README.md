# The Estate Sale — v1.3.0

**Status:** Final release (current).
**Manuscript:** `the-estate-sale-v1.3.0.md`
**Word count:** 44,955 excluding image prompts (v1.2.0, same method: 46,666; delta −1,711).
**Structure:** 22 units across three movements (survey, chain, convergence).

## Changes since v1.2.0

A page-turner pass, made after the v1.2.0 continuity fix. The brief: make the book hooked
on every page, never boring, without long descriptive filler; keep the language easy to
understand, in the register of Jim Rion's Uketsu translations for Pushkin Vertigo. The
fixes are at the sentence, paragraph, and plate level; the architecture is unchanged.

1. **Frame chapters rebuilt for momentum.** Frames One, Two, Three, and Four were rewritten
   with shorter paragraphs, faster opens, and scene breaks as beats. Average sentence length
   across the five frame/interlude units fell from **17.0 words to 12.2**.
2. **The Interlude was tightened in place** — it is the tense pivot and was largely left
   alone.
3. **Run-on sentences split.** Across the book, average sentence length fell from **18.1 to
   16.6**; sentences over 50 words fell **149 → 125**; sentences over 70 words fell
   **29 → 16**.
4. **Dense paragraphs split** in The Tea Set, The Swords, The Doll, and The Room;
   paragraphs over 120 words fell **4 → 2** (the two remaining are in-world bureaucratic
   documents, where density is the point).
5. **Five hand-drawn plates added** at clue points, so the drawn-artifact medium carries
   pace and clue-work rather than decoration: a locksmith's pencil floor plan (6.2b), a
   timeline chart (7.4b), a two-column chart of the two hands (9.7), a copied name-table
   (11.2b), and a seating chart (20.1b). Plates **129 → 134**; the illustration prompt
   sheet was updated to match.
6. **A duplicated Swords passage was de-duplicated.**

## What this release does not change

The structure, chapter titles, POV scheme, and the eleven-case architecture are unchanged.
No chapter was cut or merged. The repetitive case chapters were sped up at the sentence and
paragraph level, but their architecture (eleven statements, one discovery beat each) is
unchanged — that remains a candidate for a future structural pass.

## Contents

The assembled manuscript, in reading order. Source chapter files live in
`../../phase-6-draft/chapters/`; the phase artifacts that produced them live in the sibling
`phase-*` folders.

## What "final" means here

- All eight pipeline phases produced an artifact; the revision rationale is recorded here
  and in the story bible.
- Word count verified by the assembly script; the release is byte-identical to a fresh
  assembly of the chapter files.
- Illustrations are specified (134 plates) but not generated.

## Known carried items

1. The finder is intentionally unnamed.
2. Real-place texture references: Yanaka Ginza, Setagaya Bōro-ichi.
3. The final line's date is "today"; it needs handling if the book is ever dated.
4. The consecutive case chapters still share a discovery beat; a future pass may compress
   them (see v1.1.0 review, finding on structure).
5. Five new plates reuse existing chapter plate numbers with a `b` suffix (6.2b, 7.4b,
   11.2b, 20.1b) or extend a series (9.7); the ledger chapter and the interlude share a
   `7.x` prefix, and frame three and the tea set share a `9.x` prefix, as in prior releases.
