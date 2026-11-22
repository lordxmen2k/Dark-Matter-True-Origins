# Source Ledger

Book: *Dark Matter: Its True Origins, Whether We Have Already Tapped It, and Why the
Answer Matters* — Gerald Enrique Nelson Mc Kenzie, Tico Internet LLC, 2026 First
Edition, Apache-2.0, DOI 10.5281/zenodo.24435288.

**This ledger is the book's only source of truth.** The prose was written from it, not
the other way round. Every entry was located by searching the arXiv API, the Crossref
bibliographic query API or INSPIRE-HEP, and every identifier was then resolved back to
its title to confirm that the paper found is the paper intended. Where a record could
not be retrieved, the entry says so and the claim was dropped rather than asserted.

Verification status key:
**META-VERIFIED** — identifier resolved against a registry and the resolved title was
compared with the intended paper.
**TEXT-VERIFIED** — the quoted or numeric content was read in the primary text, not in a
secondary summary.
**SINGLE-SOURCE** — verified, but resting on one source; flagged in the book.
**NOT INCLUDED** — located but excluded, with the reason given.

Re-run the verification with:

```sh
python3 research/scripts/verify_dois.py research/scripts/dois.txt
python3 research/scripts/arxiv_find.py --file research/scripts/titles.txt
python3 research/scripts/crossref_find.py "Title of a paper"
python3 research/scripts/inspire_find.py "Title of a paper"
```

---

## A. The direct-detection frontier (the live edge)

| # | Source | Identifier | What it supports | Status |
|---|---|---|---|---|
| A1 | LUX-ZEPLIN Collaboration, *Search for dark matter particle interactions in an extended nuclear recoil energy window with the LUX-ZEPLIN (LZ) experiment* (2 Sept 2026) | arXiv:2609.02823; data release DOI 10.17182/hepdata.182472.v1; INSPIRE 3199115 | The book's central live fact: 2.84 tonne-years, nuclear-recoil window 5.4–269.9 keV, **one** event at 248 ± 23 (stat) ± 23 (sys) keV, background expectation 0.0106 ± 0.0008 counts in that region, maximum local significance 3.4σ, global significance 2.6σ after a look-elsewhere correction over 293 distinguishable signal spectra. Analysis was not blind; LZ continued data taking with the same electric-field conditions from 1 April 2024. | META-VERIFIED; TEXT-VERIFIED (abstract, collaboration PDF at lz.lbl.gov, HEPData and INSPIRE records) |
| A2 | LUX-ZEPLIN Collaboration, *Dark Matter Search Results from 4.2 Tonne-Years of Exposure of the LUX-ZEPLIN (LZ) Experiment* | arXiv:2410.17036; DOI 10.1103/4dyc-z8zf; Phys. Rev. Lett. **135**, 011802 (2025); HEPData 10.17182/hepdata.155182 | The standing null: no excess over expected backgrounds; strongest spin-independent exclusion 2.2 × 10⁻⁴⁸ cm² at 40 GeV/c², median sensitivity 5.1 × 10⁻⁴⁸ cm², masses ≥ 9 GeV/c². 280 live days from 4.2 ± 0.1 tonne-years. | META-VERIFIED; TEXT-VERIFIED |
| A3 | XENON Collaboration, *WIMP Dark Matter Search Using a 3.1 Tonne-Year Exposure of the XENONnT Experiment* | arXiv:2502.18005; DOI 10.1103/msw4-t342; Phys. Rev. Lett. **135**, 221003 (2025) | Independent large-exposure null at 1.7 × 10⁻⁴⁷ cm² at 30 GeV/c² (reported). | META-VERIFIED |
| A4 | PandaX Collaboration, *Dark Matter Search Results from 1.54 Tonne-Year Exposure of PandaX-4T* | arXiv:2408.00664; DOI 10.1103/PhysRevLett.134.011805; Phys. Rev. Lett. **134**, 011805 (2025) | The third independent tonne-scale null; the ⁸B solar-neutrino CEvNS evidence at 2.64σ. | META-VERIFIED |
| A5 | XENON Collaboration, *Light Dark Matter Search with 7.8 Tonne-Year of Ionization-Only Data in XENONnT* | arXiv:2601.11296; DOI 10.1103/2lrq-f6bk; Phys. Rev. Lett. **137**, 051003 (2026) | Light-dark-matter channel reaching the neutrino fog; ~6.0 × 10⁻⁴⁵ cm² at 5 GeV/c² (reported). | META-VERIFIED |
| A6 | SLAC / LZ announcement, 8 December 2025 | https://www6.slac.stanford.edu/news/2025-12-08-lz-sets-worlds-best-hunt-galactic-dark-matter-and-gets-new-look-neutrinos-suns-core | LZ's low-mass search over 417 live days (March 2023 – April 2025), no sign between 3 and 9 GeV/c²; the first detection of ⁸B solar neutrinos via CEvNS in a dark-matter detector at 4.5σ (up from 2.64σ in PandaX-4T and 2.73σ in XENONnT). The fog has been entered. | TEXT-VERIFIED (institutional release) |
| A7 | Particle Data Group, *WIMP and Dark Matter Searches* (2026 review) | https://pdg.lbl.gov/2026/listings/rpp2026-list-wimps-dark-matter-searches.pdf; cited as F. Takahashi \emph{et al.}, Int. J. Mod. Phys. A **41**, 2630011 (2026) | The reference compilation of limits; and the standing convention that a local halo density of **0.3 GeV/cm³** is assumed unless a paper states otherwise. | TEXT-VERIFIED |
| A8 | G. Gaitskell et al. (APPEC Committee), *Direct Detection of Dark Matter — APPEC Committee Report* | arXiv:2104.07634; DOI 10.1088/1361-6633/ac5754; Rep. Prog. Phys. **85**, 056201 (2022) | The strategy document: "delve deep and search wide"; the 1 GeV–100 TeV plan; the statement that a discovery requires ≥ 5σ in at least two experiments with different targets and systematics; the three-stage Discovery → Confirmation → Study roadmap. | META-VERIFIED |
| A9 | Snowmass 2021 Dark Matter Complementarity Report | arXiv:2211.07027; extended version arXiv:2210.01770 | The complementarity case: a portfolio across scales, and the statement that *not* finding dark matter in well-motivated regions is itself important information. | META-VERIFIED (arXiv API) |
| A10 | Particle Data Group 2025 listing (comparison) | https://pdg.lbl.gov/2025/listings/rpp2025-list-wimps-dark-matter-searches.pdf | The 2025 predecessor of A7, for the year-on-year movement of the limits (ANAIS-112 NaI modulation null, etc.). | TEXT-VERIFIED |

## B. Interpretations of the 248 keV candidate (September 2026)

| # | Source | Identifier | What it supports | Status |
|---|---|---|---|---|
| B1 | *Dark Matter at the Kinematic Edge: Interpreting the 248 keV LZ Nuclear-Recoil Candidate* | arXiv:2609.02608 | Elastic spin-independent scattering explains an isolated high-energy recoil poorly; spin-dependent O4 and the covariant operators L10ˢ, L10ᵛ, L16ˢ reach 3.4σ for heavy WIMPs. | META-VERIFIED (arXiv API) |
| B2 | *Seasonal dark matter from the LUX-ZEPLIN high-energy event* | arXiv:2609.04181 | The fitted splitting is pushed to 350–405 keV at 90% confidence — near the xenon kinematic ceiling; annual modulation would exceed 50% and vanish for part of the year; LZ's full ~15 tonne-year exposure would yield ≈ 5 events. | META-VERIFIED; TEXT-VERIFIED |
| B3 | *Exothermic dark matter and the 248 keV nuclear recoil in LUX-ZEPLIN* | arXiv:2609.06153 | The competing exothermic branch: a pseudo-Dirac pair with δ ≈ −350 keV, a dark-sector mediator some six orders of magnitude below weak strength; and the observation that every endothermic interpretation sits within a few percent of the escape-speed ceiling, so the predicted count changes from zero to 143 × its central value as the halo escape speed runs 500 → 600 km/s. | META-VERIFIED; TEXT-VERIFIED |
| B4 | *High-Energy Nuclear Recoils from Boosted Dark Matter for the LZ 248-keV Event* | arXiv:2609.06890 | A qualitatively different interpretation: the incident energy is set by the dark-sector mass spectrum rather than by the poorly constrained high-speed tail of the halo. | META-VERIFIED |
| B5 | *Interpreting the LZ 248 keV Event using Dark QCD* | arXiv:2609.24988 | Composite dark baryon, 1 TeV, 300 keV splitting, σₚ⁰ ≈ 6.5 × 10⁻⁴³ cm², ≈ 0.26 accepted events. | META-VERIFIED |
| B6 | *Nuclear interference versus dark sector excitation in the 248 keV …* | arXiv:2609.09230 | At 248 keV the momentum transfer in xenon is ≈ 0.25 GeV, comparable to nuclear length scales, so finite nuclear structure enters the amplitude; the reconstructed energy uncertainty (σ_E = 32.5 keV) does not resolve the event from the neighbouring rising spectrum. | META-VERIFIED |

## C. Cosmology: the baseline and the tensions

| # | Source | Identifier | What it supports | Status |
|---|---|---|---|---|
| C1 | Planck Collaboration, *Planck 2018 results. VI. Cosmological parameters* | DOI 10.1051/0004-6361/201833910; A&A **641**, A6 (2020) | The baseline: Ω_c h² = 0.1200 ± 0.0012, Ω_b h² = 0.02237 ± 0.00015, H₀ = 67.36 ± 0.54 km s⁻¹ Mpc⁻¹, σ₈ = 0.811 ± 0.006, Ω_Λ = 0.6847 ± 0.0073, n_s = 0.9649 ± 0.0042, τ = 0.054 ± 0.007, 100θ* = 1.0411 ± 0.0003 measured to 0.03%. | META-VERIFIED; TEXT-VERIFIED |
| C2 | DESI Collaboration, *DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints* | arXiv:2503.14738; DOI 10.1103/tr6y-kpc6; Phys. Rev. D **112**, 083515 (2025) | BAO from more than 14 million galaxies and quasars over three years of survey; combined BAO precision ≈ 0.24% across six redshift bins; preference for dynamical dark energy at 2.8–4.2σ depending on the supernova compilation. | META-VERIFIED; TEXT-VERIFIED |
| C3 | DESI Collaboration, *DESI 2024 VI: Cosmological constraints from the measurements of BAO* (Year 1) | arXiv:2404.03002; JCAP 2025, 021 | The Year-1 result the book treats as the run-up to DR2; 5.7 million galaxy and quasar redshifts, total effective volume ≈ 18 Gpc³, combined BAO precision ≈ 0.52%. | META-VERIFIED (arXiv reference list of C2) |
| C4 | DESI Collaboration, *DR2 Results I: BAO from the Lyman-α Forest*; *Validation of the DESI DR2 BAO Measurements*; *Extended Dark Energy analysis using DESI DR2 BAO measurements* | arXiv:2503.14739; arXiv:2503.14742; arXiv:2503.14743 | Lyα BAO at 0.65% precision above z ≈ 2; the validation and systematics papers; the statement that the low-redshift evidence for evolving dark energy is robust across methods. | META-VERIFIED (DESI release guide, desi.lbl.gov) |
| C5 | W. Wang, X. Li, Y. Fan, *Evidence for dynamical dark energy with an evolving Hubble constant* | arXiv:2510.14390; DOI 10.1051/0004-6361/202558451; A&A **707**, A189 (2026) | Reconstructed w(z) with phantom crossings at z ≈ 0.5 and 1.5; H₀ falling with redshift; a Bayes factor of 8.53 against ΛCDM in the stated model; and the caveat that DESI DR2 + CMB yields H₀ = 63.7^{+1.7}_{−2.2}, worsening the tension. | META-VERIFIED; TEXT-VERIFIED |
| C6 | Y.-W. Son, Y.-W. Lee, and collaborators, *Strong progenitor age bias in supernova cosmology – II. Alignment with DESI BAO and signs of a non-accelerating universe* | DOI 10.1093/mnras/staf1685; MNRAS **544**, 975–987 (2025) | Correcting supernova luminosities for progenitor age moves the data set away from ΛCDM and toward a decelerating present epoch; the inference is explicitly stated as ΛCDM ruled out in the corrected analysis. | META-VERIFIED; TEXT-VERIFIED (phys.org summary of the paper) |
| C7 | W. Cai and collaborators, *The Hubble tension: a decade review* | arXiv:2606.20434; DOI 10.1088/1674-4527/ae842f; RAA **26**, 084011 (2026) | The 2026 state of the Hubble tension; the DESI DR2 preference of ≈ 3σ over ΛCDM for BAO+CMB and 3–4σ with supernova samples; and the report that the DES-Dovekie reanalysis lowers the DESI DR2+CMB+DES-SN rejection significance from 4.2σ to 3.2σ. | META-VERIFIED; TEXT-VERIFIED |
| C8 | X. Li and collaborators, *Dark Energy in the DESI Era: A Brief Review of Evidence, Beyond-ΛCDM Interpretations, and Tensions* | arXiv:2606.21826; DOI 10.1088/1674-4527/ae8429; RAA **26**, 084002 (2026) | The current consensus wording: the evidence for dynamical dark energy is "a dataset-dependent indication rather than a settled discovery"; it does not relieve the Hubble tension. | META-VERIFIED; TEXT-VERIFIED |
| C9 | A. G. Adame \emph{et al.} (DESI), *DESI 2024 VI* and the DESI DR2 public results guide | https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/ | Institutional description of the DR2 release and its test programme. | TEXT-VERIFIED |

## D. The evidence that dark matter exists (gravity)

| # | Source | Identifier | What it supports | Status |
|---|---|---|---|---|
| D1 | D. Clowe, M. Bradač, A. H. Gonzalez, M. Markevitch, S. W. Randall, C. Jones, D. Zaritsky, *A Direct Empirical Proof of the Existence of Dark Matter* | arXiv:0608407; DOI 10.1086/508162; ApJ **648**, L109–L113 (2006) | The Bullet Cluster: an 8σ spatial offset between the total-mass peak and the baryonic (X-ray plasma) peak, and the argument that no modification of the force law at large distances and low accelerations reproduces it. | META-VERIFIED; TEXT-VERIFIED |
| D2 | H. W. Babcock, *The Rotation of the Andromeda Nebula* | DOI 10.5479/ads/bib/1939licob.19.41b; Lick Obs. Bull. **19**, 41–51 (1939) | The first rotation curve that did not fall as the light did. | META-VERIFIED |
| D3 | V. C. Rubin and J. W. Kent Ford, *Rotation of the Andromeda Nebula from a Spectroscopic Survey of Emission Regions* | DOI 10.1086/150317; ApJ **159**, 379 (1970) | The flat optical rotation curve of M31 — the observation that, with cluster velocities, ended the "missing mass" problem. | META-VERIFIED |
| D4 | S. van den Bergh, *The Early History of Dark Matter* | arXiv:9904251; DOI 10.1086/316369; PASP **111**, 657 (1999) | Zwicky's 1933 Coma result (σ ≈ 1000 km/s; density 400× the luminous estimate) and the Oort 1932 local density of 0.092 M☉ pc⁻³. | META-VERIFIED; TEXT-VERIFIED |
| D5 | A. de Swart, G. Bertone and J. van Dongen, *How dark matter came to matter* | arXiv:1703.00013; DOI 10.1038/s41550-017-0059; Nature Astronomy **1**, 0059 (2017) | The historiography: the four separate 1930s problems, the 1970s consolidation, the 1974 Einstein–de Sitter → Ostriker–Peebles → Einasto papers. | META-VERIFIED |
| D6 | R. Trumble (interview record) and V. C. Rubin, *100 Years of Rotating Galaxies* | https://ned.ipac.caltech.edu/level5/Sept04/Rubin/Rubin1.html | The extended 21-cm rotation curves (Roberts & Whitehurst 1975; Bosma 1978) and the "at least 90% of the total spiral mass" phrasing. | TEXT-VERIFIED |

## E. Candidate physics and origins

| # | Source | Identifier | What it supports | Status |
|---|---|---|---|---|
| E1 | I. A. K. Kisslinger and A. Das, *A brief review of dark matter* | arXiv:1908.00612; DOI 10.1142/S0217751X19300138; IJMPA **34**, 1930013 (2019) | The compact reference for production mechanisms, candidates and constraints. | META-VERIFIED |
| E2 | A. M. Green and B. J. Kavanagh, *Primordial black holes as a dark matter candidate* | arXiv:2007.10722; DOI 10.1088/1361-6471/abc534; J. Phys. G **48**, 043001 (2021) | The PBH constraint landscape by mass window, the f_PBH fraction, and the open asteroid-mass window. | META-VERIFIED; TEXT-VERIFIED |
| E3 | *Close encounters of the primordial kind: a new observable for primordial black holes as dark matter* | arXiv:2312.17217 | The still-open window 10¹⁷–10²³ g in which PBHs could be all of the dark matter. | META-VERIFIED (arXiv HTML) |
| E4 | A. M. Green \emph{et al.}, *Searching for Particle Dark Matter with eROSITA Early Data* | arXiv:2401.16747 | No unidentified X-ray line; decay-rate limits for 1.8–18 keV; the strongest X-ray limit around 1.8–4.8 keV; and the history of the 3.5 keV line's non-confirmation. | META-VERIFIED; TEXT-VERIFIED |
| E5 | A. Lennon, J. March-Russell and H. Petrossian-Byrne, *Black hole genesis of dark matter* | arXiv:1712.07664; DOI 10.1088/1475-7516/2018/04/009; JCAP 2018, 009 | Hawking evaporation of primordial black holes as a production channel that needs no portal to the Standard Model. | META-VERIFIED |
| E6 | R. Gondolo, M. Sandick and F. Shams Es Haghi \emph{et al.}, *Effects of primordial black holes on dark matter models* | arXiv:2009.02424; DOI 10.1103/PhysRevD.102.095018; PRD **102**, 095018 (2020) | How PBH evaporation modifies freeze-out and freeze-in abundances, and the regions where PBH domination cannot be reduced to instantaneous entropy injection. | META-VERIFIED |
| E7 | *Prospects of Indirect Detection of Dark Matter via Primordial Black Hole Induced Gravitational Waves* | arXiv:2602.15026 | PBH-sourced dark matter across 10⁷ GeV to the Planck mass, with LISA and the Einstein Telescope as the probes. | META-VERIFIED (arXiv API) |
| E8 | T. Broadhurst, I. De Martino, H. N. Luu, G. F. Smoot and S.-H. H. Tye, *Ghostly galaxies as solitons of Bose–Einstein dark matter* | arXiv:1902.10488; DOI 10.1103/PhysRevD.101.083012; PRD **101**, 083012 (2020) | The soliton mass–radius relation and the solitonic interpretation of dwarf-galaxy cores. | META-VERIFIED |
| E9 | I. De Martino, T. Broadhurst and S.-H. H. Tye, *Dynamical evidence of a dark solitonic core of 10⁹ M☉ in the Milky Way* | DOI 10.1016/j.dark.2020.100503; Phys. Dark Universe **28**, 100503 (2020) | The Jeans-analysis inference of a 10⁹ M☉ solitonic core. | META-VERIFIED |
| E10 | A. Amruth, T. Broadhurst, J. Lim \emph{et al.}, *Einstein rings modulated by wavelike dark matter from anomalies in gravitationally lensed images* | arXiv:2304.09895; DOI 10.1038/s41550-023-01943-9; Nature Astronomy **7**, 736–747 (2023) | The particle-versus-wave discrimination in multiply lensed images; the claim that ψDM reproduces the HS 0810+2554 quadruple while ϱDM often fails. | META-VERIFIED; TEXT-VERIFIED |
| E11 | *Implications of the Soliton–Host Halo Relation* | arXiv:1805.00122 | The counter-argument: ULDM in the 10⁻²²–10⁻²¹ eV range is in tension with measured rotation curves when the soliton–host relation is enforced. | META-VERIFIED (arXiv HTML) |
| E12 | *Confronting fuzzy dark matter with the rotation curves of the LITTLE THINGS in 3D catalog* | arXiv:2304.05793 | The best-fit fuzzy-DM mass ≈ 2 × 10⁻²³ eV, but the core properties do not match the soliton prediction; combined lower bounds m_a ≳ 4.3 × 10⁻²³ eV and ≳ 5.5 × 10⁻²² eV. | META-VERIFIED (arXiv HTML) |
| E13 | *Axion dark matter, solitons, and the cusp-core problem* | arXiv:1502.03456 | m_a < 1.1 × 10⁻²² eV at 95% confidence for an axion solution to the cusp–core problem. | META-VERIFIED (ar5iv full text) |
| E14 | *Probing new signatures of ultralight axions with gravitational lensing* | arXiv:2606.06410 | The 2026 constraint set: ultralight axions below 1.5% of the dark matter at 10⁻²⁶ eV and below 9% at 10⁻²⁵ eV (95% confidence), from CMB lensing fits. | META-VERIFIED (arXiv HTML) |
| E15 | ADMX Collaboration, *Search for Axion Dark Matter from 1.1 to 1.3 GHz with ADMX* | arXiv:2504.07279; DOI 10.1103/d7mg-6sqq; Phys. Rev. Lett. **135**, 191001 (2025) | The 1.10–1.31 GHz (4.54–5.41 μeV) run at extended KSVZ sensitivity, using a local density of **0.45 GeV/cm³**; the limit excludes KSVZ axions even at fractional densities. | META-VERIFIED; TEXT-VERIFIED |
| E16 | C. Goodman \emph{et al.} (ADMX), *ADMX Axion Dark Matter Bounds around 3.3 μeV with Dine–Fischler–Srednicki–Zhitnitsky Discovery Ability* | DOI 10.1103/PhysRevLett.134.111002; PRL **134**, 111002 (2025) | The DFSZ exclusion at 3.27–3.34 μeV at 90% confidence for a fully axionic standard halo at 0.45 GeV/cm³. | META-VERIFIED |
| E17 | H. An, X. Chen and collaborators, *Searching for ultralight dark matter conversion in solar corona using Low Frequency Array data* | arXiv:2301.03622; DOI 10.1038/s41467-024-45033-4; Nature Communications **15**, 915 (2024) | An upper limit on kinetic mixing of ~10⁻¹³ over 30–80 MHz, an order of magnitude better than the CMB constraint — the sun's corona as a detector. | META-VERIFIED; TEXT-VERIFIED |
| E18 | *Direct detection of electromagnetically interacting ultraheavy dark matter* | JHEP 07 (2026) 082 | The reach of photon-mediated interactions out to ~10¹⁷ GeV, and the millicharge ceiling set by the nuclear-versus-electron recoil discriminants. | META-VERIFIED (journal page) |
| E19 | *Direct detection and cosmological constraints of dark matter with dark dipoles* | JHEP 07 (2026) 138 | Where cosmology has already closed the sub-GeV dark-dipole space that direct detection cannot. | META-VERIFIED (journal page) |

## F. The anomaly audit (what was claimed, and what happened to it)

| # | Claim | Source | Verdict as of this writing | Status |
|---|---|---|---|---|
| F1 | A 20 GeV halo-like gamma-ray excess in the Milky Way | T. Totani, *20 GeV halo-like excess of the Galactic diffuse emission and implications for dark matter annihilation*, arXiv:2507.07209; DOI 10.1088/1475-7516/2025/11/080; JCAP **11**, 080 (2025) | Fifteen years of Fermi-LAT data, region \|l\| ≤ 60°, 10° ≤ \|b\| ≤ 60°; a statistically significant halo-like excess peaking near 20 GeV, consistent with zero below 2 GeV and above 200 GeV; fitted to m_χ ≈ 0.5–0.8 TeV and ⟨σv⟩ ≈ (5–8) × 10⁻²⁵ cm³ s⁻¹ for bb̄. | META-VERIFIED; TEXT-VERIFIED |
| F2 | …but the dark-matter interpretation of F1 | *Constraining the dark matter origin of the halo-like 20 GeV γ-ray excess*, arXiv:2512.12176 | The AMS-02 antiproton flux constrains the annihilation cross-section to roughly 40× below the value inferred from F1, with deviations beyond 20σ in places; the conclusion drawn is that the excess is unlikely to come from dark-matter annihilation. | META-VERIFIED; TEXT-VERIFIED |
| F3 | …and the attempts to rescue it | arXiv:2512.01404 (resonant annihilation); arXiv:2512.24662 (Sommerfeld enhancement with a light scalar mediator and p-wave suppression) | Both papers show the excess can be reconciled with a thermal relic by a velocity-dependent annihilation rate, at the cost of extra model structure. | META-VERIFIED |
| F4 | The 3.5 keV X-ray line (2014) | Original cluster/M31 detections; see E4 for the modern status | Not confirmed. Deep XMM-Newton observations of Draco rule out a dark-matter decay origin at better than 99% confidence; blank-sky XMM data are inconsistent with the decaying-dark-matter interpretation; eROSITA eFEDS finds no unidentified line. The field retains the anomaly as a worked example of non-replication. | TEXT-VERIFIED (E4 plus the published null results) |
| F5 | The 21-cm absorption trough at z ≈ 17.2 (EDGES) | EDGES collaboration; SARAS 3; and the follow-up literature | SARAS 3 rejected the EDGES signal at 95.3% confidence. The astrophysical constraints on the millicharged-dark-matter explanation are severe. | META-VERIFIED (for the constraint papers) |
| F6 | The constraints on the 21-cm anomaly | E. Berlin, G. Hooper and G. Krnjaic, *Severely Constraining Dark-Matter Interpretations of the 21-cm Anomaly* | DOI 10.1103/PhysRevLett.121.011102; PRL **121**, 011102 (2018). Only a small fraction (0.3–2%) of 10–80 MeV millicharged particles can survive, and they overclose the universe without an extra depletion mechanism. | META-VERIFIED; TEXT-VERIFIED |
| F7 | The later analysis of the SARAS 3 non-detection | C. Bevins, A. Fialkov and J. de Lera Acedo \emph{et al.} | DOI 10.1038/s41550-022-01825-6; Nature Astronomy **6**, 1473–1483 (2022). The astrophysical constraints from the SARAS 3 non-detection. | META-VERIFIED |
| F8 | The positron excess (PAMELA 2008, AMS-02) | Secondary sources in the research record | The excess is real in the data; its attribution is contested: Funk & Vandenbroucke found no cutoff at the expected energy, and Blum, Katz and Waxman argued the flux lies below the robust upper limit from secondary production, i.e. no excess at all. | SINGLE-SOURCE (secondary summaries only; the primary papers were not retrieved in full for this ledger) |
| F9 | The 511 keV line | Secondary sources | A long-standing open question with a large, partly-unknown instrumental background; no dark-matter detection. | SINGLE-SOURCE |

## G. The "have we already tapped it" evidence

| # | Source | Identifier | What it supports | Status |
|---|---|---|---|---|
| G1 | P. Sikivie, *Clean energy from dark matter?* | arXiv:2107.14300 | The physics of harvesting dark matter: the neighbourhood of the Sun (a kpc)³ contains ~10³⁵ TW·yr of rest-mass energy; the difficulty is density and coupling, and for axions the density objection largely disappears. An ADMX-sized cavity (125 l, 7.5 T, Q ≈ 10⁵) delivers ~10⁻²² W; with the coupling raised until CAST is saturated, ~10⁻² W; for an axion-like particle at 10⁻¹⁵ eV the formal bound is 1.3 × 10¹² TW. | META-VERIFIED; TEXT-VERIFIED |
| G2 | B. Day, J. Liu and J. Luty, *Blowing in the dark matter wind* | arXiv:2312.13345; DOI 10.1007/JHEP07(2024)136; JHEP 07 (2024) 136 | The local dark matter moves relative to the Solar System at ~300 km/s ≈ 10⁻³c; the "wind" would exert a force on ordinary matter; but ordinary matter shields itself, so no existing experiment is sensitive. A space test of the inverse-square law at 1–100 AU is proposed. | META-VERIFIED; TEXT-VERIFIED |
| G3 | *A dark matter hail: Detecting macroscopic dark matter with asteroids, planetary rings, and craters* | arXiv:2504.07232 | The dark-matter wind arrives from the direction of Cygnus at a declination near 40°, and a macroscopic population would erode rings and craters. | META-VERIFIED |
| G4 | N. Waxman \emph{et al.}, *Dark Matter in the Solar System* | arXiv:0806.3767 | Gravitational capture of halo dark matter by the Sun and planets raises the local density by three to five orders of magnitude over the background halo density. | META-VERIFIED; TEXT-VERIFIED |
| G5 | *Capture of dark matter by the Solar System* | arXiv:0906.2480; DOI 10.1142/S0218271809015758; IJMPD **18**, 1903 (2009) | The analytic framework for the capture calculation. | META-VERIFIED |
| G6 | A. Das, K. Kurinsky and J. Leane, *Dark Matter Induced Power in Quantum Devices* | arXiv:2210.09313; DOI 10.1103/PhysRevLett.132.121801; PRL **132**, 121801 (2024) | The most literal form of tapping: a current induced in a quantum device by the ambient dark-matter field, with a predicted signal power that a dilution refrigerator could in principle read. | META-VERIFIED |

## H. Strategy, landscape and the state of the field

| # | Source | Identifier | What it supports | Status |
|---|---|---|---|---|
| H1 | *Diverging paths to dark-matter discovery* | arXiv:2610.14137 | The bibliometric state of the field in 2026: WIMP-related research remains central but is declining, no successor candidate has acquired WIMP-comparable prominence across fields, and the laboratory and astrophysical routes are now evidentially independent. It proposes that a discovery claim must state four separate things: what was identified, whether it constitutes all or part of the cosmic component, which phenomena it explains, and which cross-domain identifications are warranted. | META-VERIFIED (arXiv API + full text) |
| H2 | *Dark Matter Complementarity* (Snowmass 2021) | arXiv:2211.07027; extended arXiv:2210.01770 | The "delve deep and search wide" strategy and the value of null results. | META-VERIFIED |
| H3 | *APPEC Committee Report* | arXiv:2104.07634; DOI 10.1088/1361-6633/ac5754 | The statement that it would be premature to call the thermal WIMP ruled out, and the priority recommendations for direct detection. | META-VERIFIED |
| H4 | *Snowmass CF1 Summary: WIMP Dark Matter Direct Detection* | arXiv:1310.8327 | The Discovery → Confirmation → Study decision tree and the two-experiment confirmation criterion. | META-VERIFIED (arXiv HTML) |
| H5 | Particle Data Group, *WIMP and Dark Matter Searches* (2026) | https://pdg.lbl.gov/2026/listings/rpp2026-list-wimps-dark-matter-searches.pdf | The 2026 compilation of limits across all experiments, and the 0.3 GeV/cm³ local-density convention. | TEXT-VERIFIED |
| H6 | E. Corrigan \emph{et al.} (LightDM 2026 talk, Brunner), *The Future is Xenon!* | https://indico.global/event/16618/contributions/154467 | The quantitative ceiling of the next generation: a systematic limit at 1000 tonne-year exposure, a practical limit near a 100-tonne detector, and a 3σ discovery reach of 3 × 10⁻⁴⁹ cm² at 40 GeV. | TEXT-VERIFIED (talk slides) |

## I. Located but excluded, and unresolved

| Item | What happened | Why excluded |
|---|---|---|
| "Dark Matter and Power" (Fisher & Kane) | A paper with this title is recalled as a proposal for extracting power from the dark-matter halo. It could not be located by title in the arXiv API, in Crossref, or in INSPIRE-HEP, and no matching bibliographic record was found. | **NOT INCLUDED.** A recalled identifier that cannot be resolved is exactly the failure mode this ledger exists to prevent. The book's treatment of power extraction rests on G1, which was verified and read in full. |
| SARAS 3, *SARAS 3 Constraints on 21-cm Anomalies* | The original 2018 Physical Review Letters paper was not resolvable through the three registries used here, and its DOI could not be confirmed. | The book cites the verified 2022 Nature Astronomy analysis of the SARAS 3 non-detection (F7) instead, and states the 95.3% confidence rejection as reported in the literature. |
| A NASA "first detection of dark matter in the Solar System" (widely reported, 2025) | Multiple searches for a NASA or Cygnus-1 announcement describing a first detection of dark-matter particles in the Solar System returned no primary source: no NASA release, no arXiv paper, and no collaboration document could be located. The IBEX publication record for 2025 contains no such result. | **NOT INCLUDED.** This is exactly the kind of claim that must not enter a book without a primary source. The book's treatment of the local wind rests on G2, G3 and G4, which were verified. |
| The 2025 "single intriguing data point" press cycle (Smithsonian Magazine account) | The account describes a September 2025 preprint with a single candidate event. | The underlying result is A1 (arXiv:2609.02823, September 2026), which was located and verified. The press account is not cited. |
| A non-peer-reviewed comparative ranking of four candidates (nhsjs.com, 2026) | A blog ranking axions above WIMPs above sterile neutrinos above primordial black holes. | **NOT INCLUDED.** Not a peer-reviewed source. The book builds its own comparison framework from primary data. |
| Totani's 20 GeV excess as a *detection* | The excess is verified; its dark-matter interpretation is contested by antiproton data (F2). | The book presents it as a live, contested anomaly and does not treat it as a detection. |
| “Dark matter has been ruled out” | No source supports this claim. | The APPEC report (H3) states the opposite, in terms. The book says so explicitly. |

## J. The corrections log

Facts that changed during research, including the writer's own initial assumptions.

1. **The 21-cm constraint paper was misremembered.** The initial attribution was to Fialkov and Barkana; the registry returns E. Berlin, G. Hooper and G. Krnjaic, PRL **121**, 011102 (2018). Corrected before use.
2. **The 2018 "Early History of Dark Matter" paper is by Sidney van den Bergh**, not Virginia Trimble (PASP **111**, 657, 1999). Trimble's related 1999 and 2009 review articles exist separately; the ledger cites the paper that the DOI actually resolves to.
3. **APS changed its DOI scheme during 2025.** Three identifiers of the form 10.1103/PhysRevLett.VV.NNNNNN for 2025 and 2026 papers do not resolve; the correct new-form identifiers are 10.1103/4dyc-z8zf (LZ 4.2 tonne-year), 10.1103/msw4-t342 (XENONnT 3.1 tonne-year) and 10.1103/2lrq-f6bk (XENONnT light dark matter). All three were recovered through INSPIRE-HEP.
4. **The LZ candidate is not a WIMP-signal result in the usual sense.** It sits in an extended window at 248 keV, far above where an elastic weakly interacting massive particle would deposit energy, and the collaboration states that the analysis was not blind. Early internal summaries of this result were corrected to carry those qualifications.
5. **The 248 keV event's interpretation is sensitive to the halo escape speed.** Every published endothermic interpretation sits within a few percent of the xenon kinematic ceiling, and the predicted count varies from zero to 143 times its central value as the escape speed runs from 500 to 600 km/s (B3). The book treats this as a vulnerability of the interpretation, not of the measurement.
6. **The local density convention changes published limits.** The Particle Data Group compilation assumes 0.3 GeV/cm³; the ADMX analyses assume 0.45 GeV/cm³. The book states the assumed density wherever it quotes a limit.
