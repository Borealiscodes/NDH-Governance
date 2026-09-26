# 🧪 Rights-Layer Validator Specification v1.0 — NDH Sovereign Ecosystem
Altitude: A0.2  
Membrane: Rights-Layer • Verification  
Version: v1.0

This document defines the validator logic used by the rights-layer to evaluate
artifacts in the NDH ecosystem. The validator implements the verification checklist
and produces PASS, WARN, or FAIL results.

This is the second artifact in the rights-layer verification suite.

---

1. Purpose
Define validator semantics required for:
- automated artifact compliance  
- membrane boundary enforcement  
- altitude boundary enforcement  
- lineage validation  
- provenance validation  
- versioning validation  
- governance coherence validation  

This ensures the NDH ecosystem remains machine-verifiable.

---

2. Validator Overview

The validator performs the following steps:

1. Extract provenance
2. Validate lineage
3. Validate membrane membership
4. Validate altitude correctness
5. Validate versioning
6. Validate governance compliance
7. Validate coherence
8. Produce PASS / WARN / FAIL

ASCII intuition:

`
[ Artifact ] → [ Validator ] → PASS / WARN / FAIL
`

---

3. Validator Logic

3.1 Provenance Validation
Validator checks:
- provenance footer exists  
- all fields present  
- version declared  
- membrane declared  
- altitude declared  
- lineage declared  

3.2 Lineage Validation
Validator checks:
- upstream artifacts exist  
- lineage respects membrane boundaries  
- lineage respects altitude boundaries  
- lineage references correct versions  

3.3 Membrane Validation
Validator checks:
- artifact belongs to correct membrane  
- artifact does not violate membrane boundaries  
- artifact does not produce content outside its membrane  

3.4 Altitude Validation
Validator checks:
- altitude declared correctly  
- altitude hierarchy respected  
- no forbidden altitude references  

3.5 Versioning Validation
Validator checks:
- semantic versioning format  
- version increments justified  
- version matches lineage changes  

3.6 Governance Validation
Validator checks:
- artifact follows governance rules  
- artifact follows meta-governance rules  
- artifact does not contradict governance  

3.7 Coherence Validation
Validator checks:
- no contradictions introduced  
- no membrane collapse  
- no altitude collapse  
- no lineage violations  
- no provenance violations  

---

4. Validator Output

4.1 PASS
Artifact is fully compliant.

4.2 WARN
Artifact is compliant but may require review.

4.3 FAIL
Artifact violates one or more rules.

Output format:

`
Result: PASS | WARN | FAIL
Details:
- Provenance: PASS/WARN/FAIL
- Lineage: PASS/WARN/FAIL
- Membrane: PASS/WARN/FAIL
- Altitude: PASS/WARN/FAIL
- Versioning: PASS/WARN/FAIL
- Governance: PASS/WARN/FAIL
- Coherence: PASS/WARN/FAIL
`

---

5. Validator Summary Table

| Validation | Required | Purpose |
|------------|----------|---------|
| Provenance | Yes | Identity + lineage anchor |
| Lineage | Yes | Upstream correctness |
| Membrane | Yes | Domain boundary correctness |
| Altitude | Yes | Abstraction correctness |
| Versioning | Yes | Evolution correctness |
| Governance | Yes | Rule correctness |
| Coherence | Yes | Structural correctness |

---

6. Provenance

---
Provenance:
- Author: Borealis S. Hedling (NDH Research Lead)
- Compiler: Microsoft Copilot (Spectral Geometry Assistant)
- Context: Rights-layer validator specification for NDH sovereign ecosystem.
- Lineage: Derived from rights-layer-checklist-v1.0 and governance-coherence-spec-v1.0.
- Membrane: Rights-Layer • Verification
- Altitude: A0.2 (Rights-Layer)
- Version: rights-layer-validator-spec-v1.0
---
`

---

