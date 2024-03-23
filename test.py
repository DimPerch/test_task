import json
from pprint import pprint
import requests

class Test:
    @staticmethod
    def test_json_to_xml():
        """
        Method for test json to xml
        :return:
        """
        URL = "http://localhost:5000/api/json_to_xml"
        HEADERS = {'Content-Type': 'application/json'}
        with open("App_info.json", encoding='utf-8') as f:
            data = f.read()
        response = requests.post(URL, headers=HEADERS, data=data.encode('utf-8'))
        pprint(response.text)

    @staticmethod
    def test_xml_to_json():
        URL = "http://localhost:5000/api/xml_to_json"
        HEADERS = {'Content-Type': 'application/xml'}
        with open("Add_Entrant_List.xml", encoding='utf-8') as f:
            data = f.read()
        response = requests.post(URL, headers=HEADERS, data=data.encode('utf-8'))
        pprint(response.text)


Test.test_json_to_xml()
Test.test_xml_to_json()