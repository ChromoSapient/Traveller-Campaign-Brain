# Extraction Log v1.4

## Source

- *Integrated Timeline Traveller*, Donald E. McKinney, version 2.1, September 16, 2006.
- Supplied filename: `Third Imperium - timeline of canon events.pdf`.
- Verified against `Traveller_Integrated_Timeline_NoRestriction.pdf` supplied after the initial patch.
- Date-code definitions were verified on PDF page 6 (printed page 5), the Ancient dating methodology on PDF page 7 (printed page 6), the Ancient pilot entries on PDF page 9 (printed page 8), and the Droyne renaissance on PDF page 11 (printed page 10).

## Extraction method and authority limits

The pilot records the dates and claims requested by the v1.4 task and verifies their date codes and wording against the supplied PDF. The integrated timeline is treated as a historical index and provenance spine, not as authority above referee rulings, campaign canon, or current-edition sources.

## Date-code handling

- `c` is preserved as `source_date_code: c` with `precision: circa`.
- `X` identifies compiler inference.
- `cX` retains both markers and requires `inferred: true`. The PDF applies `cX` to the -410000, -350000, -320000, -315000, -310000, and -302000 Ancient entries used by this pilot.
- The -300000 Final War boundary and -75000 Droyne renaissance are plain `c`; the Church's -312463 teaching has no date code.
- Precision and confidence remain independent.

## Pilot events

The pilot covers the maximum proposed Ancient dating variance, Grandfather among the Droyne, Ancient exploration, Humaniti transplantation, the Church of the Chosen Ones uplift teaching, proto-Vargr transplantation to Lair, the Final War, and the Droyne coyn renaissance.

The Church's exact uplift date is stored as a disputed, public, belief-attributed religious teaching. It is not promoted to objective fact.

## Ruuk knowledge boundary

For *Mysterious Secrets of Wrathful Ancients*, Ruuk knows or accepts that the Ancients created the Vargr but does not know why. Kzarn encouraged Ruuk's motivating question about a higher purpose. The intended purpose, responsible Ancient, and genetic-modification sequence remain restricted, and this patch does not answer the question.
