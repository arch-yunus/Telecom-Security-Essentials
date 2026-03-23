import sys
import os

# Add src to path for direct execution
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from engine.orchestrator import Orchestrator
from engine.ss7 import SS7Analyzer

def main():
    print("""
    ==================================================
    📡 TELECOM SECURITY ESSENTIALS - CORE ENGINE v1.0
    ==================================================
    """)
    
    # 1. Initialize Orchestrator
    orchestrator = Orchestrator()
    
    # 2. Register Analyzers
    orchestrator.register_analyzer(SS7Analyzer())
    
    # 3. Simulate Capture Data (SS7, Diameter, etc.)
    simulation_data = {
        "SS7": [
            "ProvideSubscriberInfo",
            "UpdateLocation",
            "MTP-Transfer-Confirmed"
        ],
        "Diameter": [] # Placeholder for next phase
    }
    
    # 4. Run Execution
    scan_results = orchestrator.run_all(simulation_data)
    
    # 5. Display Findings
    print("\n[!] SECURITY FINDINGS REPORT:")
    print("-" * 30)
    
    for protocol, findings in scan_results.items():
        if not findings:
            print(f"[{protocol}] No vulnerabilities detected.")
            continue
            
        print(f"[{protocol}] Found {len(findings)} issues:")
        for idx, finding in enumerate(findings, 1):
            print(f"  {idx}. {finding['severity']} - {finding['id']}")
            print(f"     Op: {finding['operation']}")
            print(f"     Desc: {finding['description']}\n")

if __name__ == "__main__":
    main()
