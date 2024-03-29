
import sys
from pathlib import Path
import pytest



sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from backend.src.parser_prescription import PrescriptionParser
@pytest.fixture()
def doc_1_maria():
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
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_2_virat():
    document_text = '''
Dr John >mith, M.D

2 Non-Important street,
New York, Phone (900)-323- ~2222

Name:  Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

Omeprazole 40 mg

Directions: Use two tablets daily for three months
Refill: 3 times
'''
    return PrescriptionParser(document_text)
@pytest.fixture()
def doc_3_empty():
    return PrescriptionParser('')
# def test_get_name(doc_1_maria,doc_2_virat,doc_3_empty):
#     assert doc_1_maria.get_match('patient_name')== 'Marta Sharapova'

#     assert doc_2_virat.get_match('patient_name')== 'Virat Kohli'

#     assert doc_3_empty.get_match('patient_name')== None

# def test_get_address(doc_1_maria,doc_2_virat,doc_3_empty):
#     assert doc_1_maria.get_match('patient_address')== '9 tennis court, new Russia, DC'

#     assert doc_2_virat.get_match('patient_address')== '2 cricket blvd, New Delhi'
#     assert doc_3_empty.get_match('patient_address')== None


def test_get_medicines(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_match('medicines')== 'Prednisone 20 mg,Lialda 2.4 gram'
    assert doc_2_virat.get_match('medicines')== 'Omeprazole 40 mg'
    assert doc_3_empty.get_match('medicines')== None
def test_get_directions(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_match('directions')== '''Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks -
Lialda - take 2 pill everyday for 1 month'''
    assert doc_2_virat.get_match('directions')== 'Use two tablets daily for three months'
    assert doc_3_empty.get_match('directions')== None

def test_get_refill(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_match('refill')== '3'
    assert doc_2_virat.get_match('refill')== '3'
    assert doc_3_empty.get_match('refill')== None

def test_parse(doc_1_maria, doc_2_virat, doc_3_empty):
    record_maria = doc_1_maria.parse()
    assert record_maria['patient_name']== 'Marta Sharapova'
    assert record_maria['patient_address'] == '9 tennis court, new Russia, DC'
    assert record_maria['medicines'] == 'Prednisone 20 mg,Lialda 2.4 gram'
    assert record_maria['directions']== '''Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks -
Lialda - take 2 pill everyday for 1 month'''
    assert record_maria['refill'] == '3'

    record_virat = doc_2_virat.parse()
    assert record_virat == {
        'patient_name': 'Virat Kohli',
        'patient_address': '2 cricket blvd, New Delhi',
        'medicines': 'Omeprazole 40 mg',
        'directions': 'Use two tablets daily for three months',
        'refill': '3'
    }

    record_empty = doc_3_empty.parse()
    assert record_empty == {
        'patient_name': None,
        'patient_address': None,
        'medicines': None,
        'directions': None,
        'refill': None
    }

# print(str(Path(__file__).resolve().parent))
# print(str(Path(__file__).resolve().parent.parent))
# print(str(Path(__file__).resolve().parent.parent.parent))
# print(str(Path(__file__).resolve().parent.parent.parent.parent))
# print(str(Path(__file__).resolve().parent.parent.parent.parent.parent))

#sys.path.append(str(Path(__file__).resolve().parent))
#sys.path.append(str(Path(__file__).resolve().parent.parent))
# sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
# sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent.parent))

# print(sys.path)
# # Add the project root to sys.path
# # sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
# # sys.path.append(str('c:\\Users\\Sushma\\anaconda3\\envs\\codeb\\Medical Project\\backend\\tests'))
# from backend.src.parser_generic import MedicalDocParser
# # os.chdir(r'C:\Users\Sushma\anaconda3\envs\codeb\Medical Project\backend\tests')
# # # Now import the PrescriptclearionParser class