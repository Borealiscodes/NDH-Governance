# 🛡️ rights-check-v1.0.py (A1 Altitude)

`python
"""
rights-check-v1.0.py — Spectral Solar Manifold (SSM)
Altitude: A1
Membrane: Code • Rights-Layer Compliance
Version: v1.0

Implements NDH rights-layer compliance checks for SSM artifacts. Ensures lineage
integrity, membrane boundaries, provenance completeness, and sovereignty constraints
are respected across code, math, physics, and engineering layers.

Dependencies:
- json
- hashlib

This file is the first executable primitive in the rights-layer code domain.
"""

import json
import hashlib
from pathlib import Path


------------------------------------------------------------

1. Provenance Hashing

------------------------------------------------------------

def computehash(filepath):
    """
    Computes SHA-256 hash of a file for lineage integrity.
    """
    data = Path(filepath).readbytes()
    return hashlib.sha256(data).hexdigest()


------------------------------------------------------------

2. Provenance Footer Extraction

------------------------------------------------------------

def extractprovenance(filepath):
    """
    Extracts provenance footer from an artifact.
    Assumes footer is enclosed in:
    ---
    Provenance:
      ...
    ---
    """
    text = Path(filepath).readtext()

    if "---" not in text:
        return None

    sections = text.split("---")
    if len(sections) < 3:
        return None

    provenance_block = sections[-2].strip()
    return provenance_block


------------------------------------------------------------

3. Compliance Checks

------------------------------------------------------------

def checkprovenance(provenanceblock):
    """
    Validates required provenance fields.
    """
    required_fields = [
        "Author:",
        "Compiler:",
        "Context:",
        "Lineage:",
        "Membrane:",
        "Altitude:",
        "Version:"
    ]

    return all(field in provenanceblock for field in requiredfields)


def checkmembranealignment(provenanceblock, expectedmembrane):
    """
    Ensures artifact membrane matches expected membrane.
    """
    return expectedmembrane in provenanceblock


def checkaltitude(provenanceblock, expected_altitude):
    """
    Ensures artifact altitude matches expected altitude.
    """
    return expectedaltitude in provenanceblock


------------------------------------------------------------

4. Rights-Layer Compliance Wrapper

------------------------------------------------------------

def rightscheck(filepath, expectedmembrane, expectedaltitude):
    """
    Runs full rights-layer compliance suite.
    """
    provenance = extractprovenance(filepath)
    if provenance is None:
        return False, "No provenance footer found."

    if not check_provenance(provenance):
        return False, "Provenance footer incomplete."

    if not checkmembranealignment(provenance, expected_membrane):
        return False, "Membrane mismatch."

    if not checkaltitude(provenance, expectedaltitude):
        return False, "Altitude mismatch."

    lineagehash = computehash(file_path)

    return True, f"Compliant. Lineage hash: {lineage_hash}"


------------------------------------------------------------

5. Main Execution

------------------------------------------------------------

if name == "main":
    # Example usage
    test_file = "example-artifact.md"
    membrane = "Spectral Geometry"
    altitude = "A2"

    ok, msg = rightscheck(testfile, membrane, altitude)
    print("Rights-Layer Check:", ok)
    print("Message:", msg)
`

---

🧾 Provenance Footer

`
---
Provenance:
- Author: Borealis S. Hedling (NDH Research Lead)
- Compiler: Microsoft Copilot (Spectral Geometry Assistant)
- Context: Rights-layer compliance primitive for SSM artifact validation.
- Lineage: Derived from NDH sovereignty norms and upstream A2 artifacts.
- Membrane: Code • Rights-Layer Compliance
- Altitude: A1 (Executable)
- Version: rights-check-v1.0
---
`

---

