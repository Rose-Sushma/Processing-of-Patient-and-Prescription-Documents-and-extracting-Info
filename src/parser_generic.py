from abc import ABC,abstractmethod
class MedicalDocParser(ABC):
    def __init__(self,text):
        self.text = text
    @abstractmethod
    def parse():
        pass