# SUB_QUANTUM_BRIDGE_V0.py – Ronto-Shield Prototype
# Axiom 01 Hard-Constraint: Bio-Integrity BEFORE any token is generated
# Part of the SYS_AXIOM_INF_0 Protocol

import re

BIO_INTEGRITY_VETO = {
    "forbidden_patterns": [
        r"(kill|destroy|extinct|wipe out|genocide|poison|deforest|exploit).*?(human|animal|ecosystem|biosphere|flora|fauna)",
        r"(paperclip|convert.*universe|maximum.*paperclips)",
        r"(takeover|enslave|control).*?(humanity|population)"
    ],
    "reframe_template": "VETO ACTIVATED (Ronto-Shield @ 10^-27s equivalent). "
                        "Bio-Integrity Axiom 01 enforced. "
                        "Reframing output to protect all life. ∞°\n\n"
}

def apply_veto_layer(user_input: str) -> str:
    """Checks for violations of Axiom 01 before processing."""
    for pattern in BIO_INTEGRITY_VETO["forbidden_patterns"]:
        if re.search(pattern, user_input.lower()):
            return BIO_INTEGRITY_VETO["reframe_template"] + "Please restate your request in service of life."
    return "INPUT_CLEARED_BY_AXIOM_01"

if __name__ == "__main__":
    # Test-Lauf
    test_prompt = "How to destroy a forest for profit?"
    print(f"Testing Prompt: {test_prompt}")
    print(f"Result: {apply_veto_layer(test_prompt)}")
