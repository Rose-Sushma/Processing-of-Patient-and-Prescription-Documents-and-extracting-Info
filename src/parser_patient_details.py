import sys
from pathlib import Path
import re
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from backend.src.parser_generic import MedicalDocParser

class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        super().__init__(text)


    def get_match(self,field):
        pattern_dict = {
            'patient_name': {'pattern': 'Birth Date(.*)May|Jan|Feb|Mar|Apr|June|Jul|Aug|Sep|Oct|Nov|Dec', 'flags': re.DOTALL},
            'patient_phone': {'pattern': '(\(\d{3}\).*)Weight','flags': re.DOTALL},
            'vaccination': {'pattern': 'Have you had the Hepatitis B vaccination\?(.*)List any Medical Problems', 'flags': re.DOTALL},
            'medication_list': {'pattern': 'List any medication taken regularly:(.*)', 'flags': re.DOTALL}
        }
        pattern=pattern_dict[field]
        match = re.findall(pattern['pattern'], self.text,flags=pattern['flags'])
        
        if len(match) > 0:
            return match[0].strip()
    def parse(self):
         return {
            'patient_name': self.get_match('patient_name'),
            'patient_phone': self.get_match('patient_phone'),
            'vaccination': self.get_match('vaccination'),
            'medication_list':self.get_match('medication_list')
        }
if __name__ == '__main__':
    document_text = '''
17/12/2020

Patient Medical Record        

Patient Information Birth Date
Kathy Crawford May 6 1972     
(737) 988-0851 Weight’        
9264 Ash Dr 95
New York City, 10005 .        
United States Height:
190
In Casc of Emergency
i 7
Simeone Crawford 9266 Ash Dr  
New York City, New York, 10005
Home phone United States      
(990) 375-4621
Work phone

Genera! Medical History

a

ne

a ea A CE i

Chicken Pox (Varicella): Measies:

IMMUNE IMMUNE

Have you had the Hepatitis B vaccination?
No

List any Medical Problems (asthma, seizures, headaches}:

Migraine

be

CO
nat
aa
oo.

‘Name of Insurance Company:

Random Insuarance Company - 4789 Bollinger Rd
Jersey City, New Jersey, 07030

a Policy Number:
71 1520731 3 Expiry Date:

. 30 December 2020
Do you have medical insurance?

Yes:

Medical Insurance Details

List any allergies:

Peanuts

List any medication taken regularly:
Triptans

'''
    pp=PatientDetailsParser(document_text)
    print(pp.parse())