import yaml
import os
import logging

class SignatureLoader:
    """
    Handles loading and parsing of the YAML signatures file.
    """
    
    def __init__(self, config_path=None):
        if not config_path:
            # Default path relative to project root
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            config_path = os.path.join(base_dir, 'config', 'signatures.yaml')
            
        self.config_path = config_path
        self.logger = logging.getLogger("SignatureLoader")
        self.signatures = {}
        self.load()

    def load(self):
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                self.signatures = data.get('signatures', {})
                self.logger.info(f"Successfully loaded signatures for {len(self.signatures)} protocols.")
        except Exception as e:
            self.logger.error(f"Failed to load signatures from {self.config_path}: {e}")
            self.signatures = {}

    def get_signatures_for_protocol(self, protocol_name: str) -> list:
        return self.signatures.get(protocol_name, [])
