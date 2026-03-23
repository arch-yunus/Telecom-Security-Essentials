import json
import os
import datetime
from string import Template

class ReportGenerator:
    """
    Structured Reporting Engine.
    Handles findings exports in JSON and HTML formats.
    """
    
    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_json(self, results: dict, filename_prefix="scan_report"):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(self.output_dir, f"{filename_prefix}_{timestamp}.json")
        
        report_data = {
            "version": "1.1",
            "scan_time": str(datetime.datetime.now()),
            "protocols_scanned": list(results.keys()),
            "findings": results
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=4, ensure_ascii=False)
        return filepath

    def generate_html(self, results: dict, filename_prefix="scan_report"):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(self.output_dir, f"{filename_prefix}_{timestamp}.html")
        
        # Professional HTML Template (Embedded for Autonomy)
        html_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Telecom Security Essentials - Scan Report</title>
            <style>
                body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f4f7f6; color: #333; margin: 40px; }
                .header { background: #2c3e50; color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
                .protocol-section { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 20px; }
                .finding { border-left: 5px solid #e74c3c; padding: 10px; margin: 10px 0; background: #fdf2f2; }
                .finding.HIGH { border-left-color: #e67e22; background: #fff5e6; }
                .finding.MEDIUM { border-left-color: #f1c40f; background: #fef9e7; }
                .finding.LOW { border-left-color: #3498db; background: #ebf5fb; }
                .severity { font-weight: bold; padding: 2px 6px; border-radius: 4px; color: white; }
                .CRITICAL { background: #e74c3c; }
                .HIGH { background: #e67e22; }
                .MEDIUM { background: #f1c40f; }
                .LOW { background: #3498db; }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Telecom Security Scan Report</h1>
                <p>Generated on: $timestamp</p>
            </div>
            $content
        </body>
        </html>
        """
        
        content_html = ""
        for protocol, findings in results.items():
            content_html += f"<div class='protocol-section'><h2>Protocol: {protocol}</h2>"
            if not findings:
                content_html += "<p>No vulnerabilities detected.</p>"
            else:
                for f in findings:
                    content_html += f"""
                    <div class='finding {f['severity']}'>
                        <span class='severity {f['severity']}'>{f['severity']}</span>
                        <strong>{f['id']} - {f['name']}</strong>
                        <p><strong>Operation:</strong> {f['operation']}</p>
                        <p><strong>Description:</strong> {f['description']}</p>
                    </div>
                    """
            content_html += "</div>"

        t = Template(html_template)
        final_html = t.substitute(timestamp=str(datetime.datetime.now()), content=content_html)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_html)
        return filepath
