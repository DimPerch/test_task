import xmltodict
import json
import xml.etree.ElementTree as ET


class Converter:
    @staticmethod
    def xml_to_json(xml_string):
        xml_dict = xmltodict.parse(xml_string)
        json_data = json.dumps(xml_dict)
        return json_data

    @staticmethod
    def json_to_xml(json_data):
        def build_xml(parent, data):
            if isinstance(data, dict):
                for key, value in data.items():
                    if isinstance(value, (dict, list)):
                        child = ET.SubElement(parent, key)
                        build_xml(child, value)
                    else:
                        ET.SubElement(parent, key).text = str(value)
            elif isinstance(data, list):
                for item in data:
                    build_xml(parent, item)

        root = ET.Element('root')
        build_xml(root, json_data)
        return ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
