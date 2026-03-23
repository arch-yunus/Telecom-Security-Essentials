import logging

class Orchestrator:
    """
    The central motor of the project. Loads analyzers and processes telemetry data.
    Supports a plug-and-play architecture for protocol modules.
    """
    
    def __init__(self):
        self.analyzers = []
        self._setup_logging()

    def _setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - [%(levelname)s] - %(name)s - %(message)s'
        )
        self.logger = logging.getLogger("Orchestrator")

    def register_analyzer(self, analyzer):
        self.logger.info(f"Registering analyzer: {analyzer.protocol_name}")
        self.analyzers.append(analyzer)

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
