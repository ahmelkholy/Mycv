# CV update — 9 October 2026

The current CV is `Ahmed_M_Elkholy-cv.pdf`; its editable source is
`CV_Ahmed_M_Elkholy.md`. The three-page layout includes academic experience,
education, skills, training, service, 12 journal articles, and 13 conference
papers. The previous files are preserved in `original/`.

## Sources and decisions

- [LinkedIn](https://www.linkedin.com/in/ahmelkholy/): direct access returned an
  access restriction; publicly indexed Arabic/Russian versions corroborated
  earlier degrees and certificates. The MIT research stay was a post by Mohamed
  Numair appearing among reactions, not Ahmed's position. No MIT affiliation is
  included, as explicitly confirmed by the user.
- [ResearchGate](https://www.researchgate.net/profile/Ahmed-Elkholy-7): used to
  discover publications and confirm MPEI/Tanta affiliations. The old
  `Ahmed_Elkholy10` link redirects here. Its publication count includes items
  such as preprints and an erratum; it is not used as a CV paper count.
- [Google Scholar](https://scholar.google.com/citations?user=KbZs8_AAAAAJ&hl=en):
  correct user-provided profile saved, but direct access was restricted. No
  citation count or h-index was inferred.
- [ORCID](https://orcid.org/0000-0002-1834-1175): public API supplied DOI records
  and the Researcher/R&D Engineer role at MPEI from October 2023. Snapshot in
  `research/orcid_works.json`. The older Tanta employment entry has a generic
  teaching-assistant title; role dates from the existing CV were retained.
- [Zotero](https://www.zotero.org/ahmelkholy): public user ID 10420737. A public
  library request succeeded; the publications endpoint timed out. Authored
  records are saved in `research/zotero_authored_records.json`. Saved literature
  by other researchers was excluded. Pagination must be followed on future API
  reads; the first page alone does not represent the complete library.
- [GitHub](https://github.com/ahmelkholy): checked public repository metadata.
  Included original IEEE13-optimization and Zthevenin projects. Forks were not
  presented as authored software or contributions.
- [Tanta staff page](http://tdb2.tanta.edu.eg/staff/ahmelkholy): accessible over
  HTTPS and corroborates the name, department, and earlier publications.
- [Personal website](https://ahmelkholy.github.io/): degree dates, thesis titles,
  expected completion, language claims, and some sections conflict with the
  existing CV or contain placeholders. Such claims were not adopted.
- [Crossref](https://api.crossref.org/): title and direct DOI lookups verified
  author order, publication venues, dates, volumes, and pages. Final snapshot:
  `research/publications_verified.json`. Query results can match preprints, so
  check the DOI against ORCID/publisher before including a record.
- Two additional July 2026 articles were found in Zotero and verified on
  [Springer: shunt regulation devices](https://link.springer.com/article/10.3103/S1068371226700847)
  and [Springer: dual-loop shunt regulation](https://link.springer.com/article/10.3103/S1068371226700835).
  The author's published transliteration is Elkholi in these papers.

## Dates and unresolved details

The user confirmed that the PhD is in progress and expected to finish in December
2026. The year is interpreted relative to the current date. The start year is
omitted because the old CV and profiles give conflicting years (2019–2022).

The newest EV corridor planning article is online and assigned to the December
2026 issue (DOI 10.1016/j.epsr.2026.113505). The CV labels that future issue date.
Other issue years follow DOI metadata, including the arc-suppression article in
IEEE Transactions on Industry Applications, January 2026 (online DOI dated 2025),
and low-voltage SVC paper, February 2025 (DOI dated 2024).

Zotero also lists a 2026 paper titled "Comparative Analysis of Metaheuristic
Algorithms for Optimizing the Placement of Electric Vehicle Charging
Infrastructure on Highways with Cartographic Visualization of the Obtained
Solutions". The record has no DOI, journal title, pages, or public URL. It is
retained in the research snapshot, but excluded from the finished publication
list pending confirmation of publication details.

Languages use conservative descriptions. No current IELTS validity or new
Russian proficiency is claimed. Contact details and teaching responsibilities
come from the existing CV. Referees' potentially outdated positions and private
contact details, the unrelated job target, and generic personal-skills filler
were removed from the main CV. The original remains available.

## Future update workflow

1. Read `profiles.json` and check the user-confirmed facts.
2. Review each saved profile and the public APIs. Follow pagination. If a source
   blocks access, record the limitation and use corroborating public records.
3. Check actual authorship and affiliation before adding information; compare
   against `research/publications_verified.json`, deduplicating DOI values
   case-insensitively.
4. Verify new publications with their DOI/publisher. Check whether an item is
   published, accepted, a preprint, software, or an erratum. Do not silently
   promote it to a journal paper or infer citation metrics.
5. Edit the Markdown CV and verified bibliography, then run `python3 build_cv.py`.
6. Inspect all PDF pages and extracted text for overflow and split entries.
7. Update the review date, evidence notes, and relevant metadata snapshots.

This stores instructions and sources for future updates; it does not schedule
background updates or change the public profiles.
