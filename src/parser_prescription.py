import re

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from backend.src.parser_generic import MedicalDocParser

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        super().__init__(text)
    def get_name(self):
        pattern = "Name:(.*)Date"
        match = re.findall(pattern, self.text)
        if len(match) > 0:
            return match[0].strip()
    def get_address(self):
        pattern = "Address:(.*)"
        match = re.findall(pattern, self.text)
        if len(match) > 0:
            return match[0].strip()

    def get_medicines(self):
        pattern = "Address[^\n]*(.*)Directions"
        match = re.findall(pattern, self.text,flags=re.DOTALL)
        if len(match) > 0:
            text=match[0].strip()
            return text.replace('\n', ',')
    def get_directions(self):
        pattern = "Directions:(.*)Refill:"
        match = re.findall(pattern, self.text,flags=re.DOTALL)
        if len(match) > 0:
            return match[0].strip()
    def get_refill(self):
        pattern = "Refill:(.*)times"
        match = re.findall(pattern, self.text,flags=re.DOTALL)
        if len(match) > 0:
            return match[0].strip()
    def parse(self):
         return {
            'patient_name': self.get_match('patient_name'),
            'patient_address': self.get_match('patient_address'),
            'medicines': self.get_match('medicines'),
            'directions':self.get_match('directions'),
            'refill':self.get_match('refill')
        }
    def get_match(self,field):
        pattern_dict = {
            'patient_name': {'pattern': 'Name:(.*)Date', 'flags': 0},
            'patient_address': {'pattern': 'Address:(.*)\n', 'flags': 0},
            'medicines': {'pattern': 'Address[^\n]*(.*)Directions', 'flags': re.DOTALL},
            'directions': {'pattern': 'Directions:(.*)Refill', 'flags': re.DOTALL},
            'refill': {'pattern': 'Refill:(.*)times', 'flags': 0}
        }
        pattern=pattern_dict[field]
        match = re.findall(pattern['pattern'], self.text,flags=pattern['flags'])
        
        if len(match) > 0:
            if field=='medicines':
                text=match[0].strip()
                return text.replace('\n', ',') 
            else:
                return match[0].strip()

if __name__ == '__main__':
    document_text = '''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222
Name: Marta Sharapova Date: 5/11/2022
Address: 9 tennis court, new Russia, DC

Prednisone 20 mg
Lialda 2.4 gram
Directions:
Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks -
Lialda - take 2 pill everyday for 1 month
Refill: 3 times
'''
    pp=PrescriptionParser(document_text)
        # print(pp.get_name())
        # print(pp.get_address())
        # pp.get_medicines()
    print(pp.parse())