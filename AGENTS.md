# CV maintenance

This repository contains Ahmed M. Elkholy's CV. For future updates, read
`profiles.json` and `UPDATE_NOTES.md`, then check the saved profile URLs for new
information. The user explicitly requested that these links be retained and used
for later CV updates.

- Keep the wording straightforward and credible. The user wants a good practical
  CV, with no exaggerated expertise or invented achievements.
- The user confirmed on 9 October 2026 that he is still pursuing his PhD and
  expects to finish in December 2026. Do not mark the degree completed without
  later confirmation. The exact start year remains unresolved.
- The user explicitly confirmed that he is not affiliated with MIT. LinkedIn
  reactions, reposts, and other people's posts are not his experience.
- Verify identity with ORCID 0000-0002-1834-1175, affiliations, and coauthors.
  Other researchers named Ahmed Elkholy exist.
- Zotero is a reading library as well as a publication list. Include only works
  whose author list contains this researcher; check `inPublications` and verify
  DOI metadata. A saved paper, GitHub fork, or LinkedIn reaction is not evidence
  of authorship, a contribution, or a qualification.
- Use publisher/DOI metadata for titles, author order, journal/issue dates, and
  publication status. Deduplicate preprints, errata, and final versions.
- Personal website content currently contains placeholders and contradictory
  degree dates and thesis titles. Do not propagate these without corroboration.
- Edit `CV_Ahmed_M_Elkholy.md`, then run `python3 build_cv.py` to regenerate the
  LaTeX, PDF, and text files. The build needs XeLaTeX and Arial.
- Check PDF layout, text extraction, links, and LaTeX overflow warnings. Update
  `profiles.json`, bibliography, and research notes when new facts are verified.
- Keep the original CV in `original/`. Saving local changes is authorized;
  publication or pushing to a remote should follow the user's actual request.
