from abc import ABC, abstractmethod


class SomethingDriving(ABC):
    def __init__(self):
        self.wheels = None
        self.doors = None
        self.engine = True
        self.type_of_engine = None

    @abstractmethod
    def start_engine(self):
        """Implement start engine behaviour"""
        pass

    @abstractmethod
    def stop_engine(self):
        """Implement stop engine behaviour"""
        pass
