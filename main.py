import sys
import os

# Add src to path for direct execution
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from engine.orchestrator import Orchestrator
from engine.loader import SignatureLoader
from engine.ss7 import SS7Analyzer
from engine.diameter import DiameterAnalyzer
from engine.gtp import GTPAnalyzer

def main():
    print("""
    ==================================================
    TELECOM SECURITY ESSENTIALS - CORE ENGINE v1.1
    ==================================================
    """)
    
    # 1. Initialize Signature Loader
    loader = SignatureLoader()
    
    # 2. Initialize Orchestrator
    orchestrator = Orchestrator()
    
    # 3. Register Analyzers with shared loader
    orchestrator.register_analyzer(SS7Analyzer(loader))
    orchestrator.register_analyzer(DiameterAnalyzer(loader))
    orchestrator.register_analyzer(GTPAnalyzer(loader))
    
    # 4. Simulate Multi-Protocol Capture Data
    simulation_data = {
        "SS7": [
            "ProvideSubscriberInfo",
            "AnyTimeInterrogation"
        ],
        "Diameter": [
            "Update-Location-Request",
            "Device-Watchdog-Request"
        ],
        "GTP": [
            "Create-Session-Request",
            "Echo-Request"
        ]
    }
    
    # 5. Run Execution
    scan_results = orchestrator.run_all(simulation_data)
    
    # 6. Display Findings
    print("\n[!] SECURITY FINDINGS REPORT:")
    print("-" * 30)
    
    for protocol, findings in scan_results.items():
        if not findings:
            print(f"[{protocol}] No vulnerabilities detected.")
            continue
            
        print(f"[{protocol}] Found {len(findings)} issues:")
        for idx, finding in enumerate(findings, 1):
            print(f"  {idx}. {finding['severity']} - {finding['id']} ({finding['name']})")
            print(f"     Op: {finding['operation']}")
            print(f"     Desc: {finding['description']}\n")

if __name__ == "__main__":
    main()
