from abc import ABC, abstractmethod

class BaseAnalyzer(ABC):
    """
    Abstract Base Class for all protocol analyzers (SS7, Diameter, GTP).
    Ensures a consistent interface across the engine.
    """
    
    @property
    @abstractmethod
    def protocol_name(self) -> str:
        pass

    @abstractmethod
    def analyze(self, data: any) -> list:
        """
        Performs analysis on given protocol data and returns a list of findings.
        """
        pass

    def __repr__(self):
        return f"<Analyzer: {self.protocol_name}>"
