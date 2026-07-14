# Manual Upload Package: Crew Capabilities v1.0

Upload these files to `ChromoSapient/Traveller-Campaign-Brain`, branch `main`.

## Files

1. `Characters/Garnette_Crew_Capabilities.yaml`
   - New canonical crew characteristics, raw skills, role assessments, role matrix, and continuity checks.
   - Source authority: uploaded `Secrets of the Ancients crew.xlsx`.
   - Treats the spreadsheet as an explicit referee ruling that supersedes older stat summaries where they conflict.

2. `Instructions/PROJECT_ROUTER.yaml`
   - Full replacement for the current router.
   - Bumps router version from 1.2 to 1.3.
   - Adds the crew capabilities file to prose, recommendations, characters, Garnette, and Tapir routes.
   - Adds a dedicated `crew_roles` route and refresh trigger.

## Recommended commit message

`Add canonical Garnette crew skills and role validation`

## Important interpretation decisions

- Raw skill levels are stored separately from characteristic DMs, equipment, software, augments, and assistance.
- Assigned jobs do not override skill ratings.
- Tapir remains unavailable in the active branch.
- Roamer is the only trained Engineer.
- Ruuk is the only trained Medic.
- Solveig and Tapir are the only trained Astrogators.
- Ardric is the primary spacecraft pilot; Corbin and Roamer are trained backups.
- Ardric and Roamer are the strongest sensor operators by raw skill, even though Solveig is assigned the Sensors job.
- Corbin is the strongest computer operator and investigator.
- Garnette currently has no established weapon fit, so Corbin's Gunner role is dormant unless that changes.

## Name normalization note

The workbook says `Ardric Dravayne`; the repository currently uses `Ardric Vellarn D'Ravayne`.
The new file preserves the repository name as an alias while retaining the workbook form.
No entity rename is included in this package.
