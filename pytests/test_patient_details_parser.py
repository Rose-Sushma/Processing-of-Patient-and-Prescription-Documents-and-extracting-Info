
import sys
from pathlib import Path
import pytest
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from backend.src.parser_patient_details import PatientDetailsParser
@pytest.fixture()
def doc_kathy():
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
    return PatientDetailsParser(document_text)

@pytest.fixture()
def doc_3_empty():
    return PatientDetailsParser('')

def test_get_name(doc_kathy,doc_3_empty):
    assert doc_kathy.get_match('patient_name')== 'Kathy Crawford'
    assert doc_3_empty.get_match('patient_name')== None


def test_get_phone(doc_kathy,doc_3_empty):
    assert doc_kathy.get_match('patient_phone')== '(737) 988-0851'
    assert doc_3_empty.get_match('patient_phone')== None


def test_get_vaccination(doc_kathy,doc_3_empty):
    assert doc_kathy.get_match('vaccination')== 'No'
    assert doc_3_empty.get_match('vaccination')== None

def test_get_medication_list(doc_kathy,doc_3_empty):
    assert doc_kathy.get_match('medication_list')== 'Triptans'
    assert doc_3_empty.get_match('medication_list')== None
