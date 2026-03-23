import re
from .base import BaseAnalyzer

class GTPAnalyzer(BaseAnalyzer):
    """
    Security Analyzer for GTP (GPRS Tunnelling Protocol) for Packet Core security.
    """
    
    @property
    def protocol_name(self) -> str:
        return "GTP"

    def __init__(self, loader):
        self.loader = loader

    def analyze(self, messages: list) -> list:
        findings = []
        signatures = self.loader.get_signatures_for_protocol(self.protocol_name)
        
        for msg in messages:
            for sig in signatures:
                if re.search(sig['pattern'], msg, re.IGNORECASE):
                    findings.append({
                        "id": sig['id'],
                        "name": sig['name'],
                        "severity": sig['severity'],
                        "operation": msg,
                        "description": sig['description']
                    })
        return findings
