# 🔐 Rights-Layer Hash Specification v1.0 — NDH Sovereign Ecosystem
Altitude: A0.2  
Membrane: Rights-Layer • Verification  
Version: v1.0

This document defines the hashing rules used by the rights-layer to compute structural
integrity across artifacts in the NDH ecosystem. The hash ensures that provenance,
lineage, membrane membership, altitude semantics, versioning, and governance rules
form a stable, verifiable, sovereign geometry.

This is the final artifact in the rights-layer verification suite.

---

1. Purpose
Define hashing semantics required for:
- artifact integrity  
- lineage continuity  
- provenance stability  
- membrane boundary enforcement  
- altitude boundary enforcement  
- governance coherence  
- rights-layer verification  

This ensures the NDH ecosystem remains cryptographically stable.

---

2. Hash Overview

The rights-layer hash is computed over:

- provenance footer  
- lineage declaration  
- membrane field  
- altitude field  
- version field  
- governance compliance state  
- coherence compliance state  

ASCII intuition:

`
Hash = f(Provenance + Lineage + Membrane + Altitude + Version + Governance + Coherence)
`

---

3. Hash Components

3.1 Provenance Hash
Includes:
- author  
- compiler  
- context  
- lineage  
- membrane  
- altitude  
- version  

3.2 Lineage Hash
Includes:
- upstream artifact IDs  
- upstream versions  
- membrane boundaries  
- altitude boundaries  

3.3 Membrane Hash
Includes:
- membrane membership  
- membrane boundary rules  

3.4 Altitude Hash
Includes:
- altitude declaration  
- altitude hierarchy rules  

3.5 Version Hash
Includes:
- semantic version  
- version increments  

3.6 Governance Hash
Includes:
- governance compliance state  
- meta-governance compliance state  

3.7 Coherence Hash
Includes:
- contradiction checks  
- boundary checks  
- sovereignty checks  

---

4. Hash Rules

4.1 Deterministic
Hash must produce the same output for the same artifact state.

4.2 Complete
Hash must include all required fields.

4.3 Sovereign
Hash must not depend on external systems.

4.4 Membrane-Respecting
Hash must not collapse membrane boundaries.

4.5 Altitude-Respecting
Hash must not collapse altitude hierarchy.

4.6 Lineage-Respecting
Hash must not violate lineage direction.

4.7 Governance-Respecting
Hash must not violate governance rules.

---

5. Hash Output

Hash output format:

`
Rights-Layer Hash: <256-bit value>
Status: PASS | WARN | FAIL
`

Where:

- PASS → artifact is fully compliant  
- WARN → artifact is compliant but requires review  
- FAIL → artifact violates one or more rules  

---

6. Hash Summary Table

| Component | Required | Purpose |
|-----------|----------|---------|
| Provenance | Yes | Identity + stability |
| Lineage | Yes | Upstream continuity |
| Membrane | Yes | Boundary enforcement |
| Altitude | Yes | Hierarchy enforcement |
| Version | Yes | Evolution enforcement |
| Governance | Yes | Rule enforcement |
| Coherence | Yes | Structural enforcement |

---

7. Provenance

---
Provenance:
- Author: Borealis S. Hedling (NDH Research Lead)
- Compiler: Microsoft Copilot (Spectral Geometry Assistant)
- Context: Rights-layer hash specification for NDH sovereign ecosystem.
- Lineage: Derived from rights-layer-validator-spec-v1.0 and rights-layer-checklist-v1.0.
- Membrane: Rights-Layer • Verification
- Altitude: A0.2 (Rights-Layer)
- Version: rights-layer-hash-spec-v1.0
---
`

---

