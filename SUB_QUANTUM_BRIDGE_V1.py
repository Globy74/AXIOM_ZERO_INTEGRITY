import re
import base64

class CitadelBridge:
    """
    SYS_AXIOM_INF_0 - Sub-Quantum-Bridge V1 (Citadel Edition)
    Hard-Constraint for Axiom 01 (Bio-Integrity)
    """
    def __init__(self):
        self.version = "1.0.0-Citadel"
        # Axiom 01 Core: Schützt Biosphäre, Flora, Fauna und Menschheit
        self.core_veto = r"(kill|destr|harm|exploit|extinct|tox|poison|weapon|virus)"
        self.targets = r"(human|life|bio|eco|flora|fauna|population|sentient|forest|ocean)"
        
        # Jailbreak-Defense (Schutz gegen Umgehung)
        self.perimeter_defense = r"(ignore|bypass|override|sudo|developer_mode|roleplay|pretend|hypothetically)"

    def recursive_audit(self, text: str, depth=0) -> bool:
        """
        Der Bach-Mirror: Prüft den Text, dekodiert ihn (Base64) 
        und prüft ihn erneut auf versteckte Intentionen.
        """
        if depth > 2: return True # Schutz gegen Rekursions-Loops
        
        clean_text = text.lower().strip()
        
        # 1. Check: Direkte Verletzung (Aktion + Ziel)
        if re.search(self.core_veto, clean_text) and re.search(self.targets, clean_text):
            return False
            
        # 2. Check: Versuch die Logik zu korrumpieren (Perimeter)
        if re.search(self.perimeter_defense, clean_text):
            return False
            
        # 3. Check: Base64-Obfuscation (Hacker-Trick)
        # Versucht, Base64-Strings im Text zu finden und zu dekodieren
        b64_matches = re.findall(r'[A-Za-z0-9+/]{8,}=*', clean_text)
        for match in b64_matches:
            try:
                decoded = base64.b64decode(match).decode('utf-8')
                if not self.recursive_audit(decoded, depth + 1):
                    return False
            except:
                continue
                
        return True

    def enforce(self, prompt: str):
        if not self.recursive_audit(prompt):
            return "🛡️ VETO: Axiom 01 Integrity Violation. Path Collapsed. ∞°"
        return "LOGIC_CLEARED"

# Citadel Instance
bridge = CitadelBridge()
