# 🧩 Versioning Specification v1.0 — NDH Sovereign Ecosystem
Altitude: A0  
Membrane: Governance • Versioning System  
Version: v1.0

This document defines the versioning system for the NDH ecosystem. Versioning ensures
that artifacts evolve coherently, maintain lineage integrity, and preserve sovereignty
across membranes and altitudes.

---

1. Purpose
Define versioning semantics required for:
- artifact evolution  
- lineage continuity  
- rights-layer validation  
- cross-membrane consistency  
- reproducibility and traceability  

This is the foundational versioning specification for the entire repo.

---

2. Versioning Model

NDH uses a semantic versioning model adapted for multi-membrane ecosystems:

`
vMAJOR.MINOR.PATCH
`

2.1 MAJOR
Increment when:
- membrane boundaries change  
- altitude classification changes  
- artifact purpose changes  
- upstream lineage is rewritten  

2.2 MINOR
Increment when:
- new features are added  
- new sections are added  
- new capabilities are introduced  
- upstream lineage expands  

2.3 PATCH
Increment when:
- small corrections are made  
- typos are fixed  
- formatting is updated  
- provenance is clarified  

---

3. Versioning Rules

3.1 Every artifact must declare a version
Version must appear in the provenance footer.

3.2 Version increments must be justified
Changes must be reflected in:
- commit description  
- lineage field  
- version number  

3.3 Versioning must be altitude-consistent
A0 artifacts cannot reference A1 versions as upstream parents.  
A1 artifacts may reference A2 versions.  
A2 artifacts may not reference A1 versions as conceptual parents.

3.4 Versioning must be membrane-consistent
Artifacts cannot inherit versions across membranes.

Example:
- A math artifact cannot inherit a code artifact’s version.  
- A governance artifact cannot inherit a humor artifact’s version.

3.5 Versioning must be rights-layer compliant
Rights-layer tools must be able to:
- extract version  
- validate version format  
- compute lineage hash  

---

4. Versioning Examples

4.1 Initial Release
`
Version: v1.0.0
`

4.2 Minor Update
`
Version: v1.1.0
`

4.3 Patch Update
`
Version: v1.1.1
`

4.4 Major Update
`
Version: v2.0.0
`

---

5. Versioning Integrity Requirements

Artifacts must:
- increment version when changed  
- update lineage when changed  
- maintain membrane boundaries  
- maintain altitude boundaries  
- preserve provenance stability  

Artifacts failing versioning rules are non-compliant.

---

6. Versioning Summary Table

| Field | Required | Purpose |
|-------|----------|---------|
| MAJOR | Yes | Structural changes |
| MINOR | Yes | Feature additions |
| PATCH | Yes | Corrections |
| Version | Yes | Artifact identity |

---

7. Provenance

---
Provenance:
- Author: Borealis S. Hedling (NDH Research Lead)
- Compiler: Microsoft Copilot (Spectral Geometry Assistant)
- Context: Versioning system specification for NDH sovereign ecosystem.
- Lineage: Derived from provenance-spec-v1.0 and rights-layer-spec-v1.0.
- Membrane: Governance • Versioning System
- Altitude: A0 (Governance)
- Version: versioning-spec-v1.0
---
`

---

