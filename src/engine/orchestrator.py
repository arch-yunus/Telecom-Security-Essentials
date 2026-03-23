import logging

from .report import ReportGenerator

class Orchestrator:
    """
    The central motor of the project. Loads analyzers and processes telemetry data.
    Supports fixed-format reporting and real-time visualization.
    """
    
    def __init__(self, reports_dir="reports"):
        self.analyzers = []
        self._setup_logging()
        self.reporter = ReportGenerator(reports_dir)

    def _setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - [%(levelname)s] - %(name)s - %(message)s'
        )
        self.logger = logging.getLogger("Orchestrator")

    def register_analyzer(self, analyzer):
        self.logger.info(f"Registering analyzer: {analyzer.protocol_name}")
        self.analyzers.append(analyzer)

    def generate_reports(self, results: dict):
        """
        Exports the scan results into JSON and HTML formats via the reporter.
        """
        self.logger.info("Generating security reports...")
        json_path = self.reporter.generate_json(results)
        html_path = self.reporter.generate_html(results)
        self.logger.info(f"JSON Report: {json_path}")
        self.logger.info(f"HTML Report: {html_path}")
        return json_path, html_path

    def run_all(self, capture_data: dict):
        """
        Dispatches capture data to relevant analyzers.
        """
        self.logger.info("Starting global security scan...")
        results = {}
        
        for analyzer in self.analyzers:
            protocol = analyzer.protocol_name
            if protocol in capture_data:
                self.logger.info(f"Processing {protocol} traffic...")
                results[protocol] = analyzer.analyze(capture_data[protocol])
            else:
                self.logger.warning(f"No data provided for protocol: {protocol}")
        
        return results
