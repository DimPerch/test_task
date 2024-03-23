import xmltodict
import json
import xml.etree.ElementTree as ET


class Converter:

    @staticmethod
    def xml_to_json(xml_string):
        """
        Converts an XML string to JSON format string.

            Parameters:
                xml_string (str): The XML string to convert to JSON.

            Returns:
                str: The JSON string containing the equivalent XML data."""

        def _element_to_dict(element):
            result = {}
            for child in element:
                if child:
                    result[child.tag] = _element_to_dict(child)
                else:
                    result[child.tag] = child.text
            return result

        root = ET.fromstring(xml_string)
        return _element_to_dict(root)

    @staticmethod
    def json_to_xml(json_data):
        """
        Converts JSON data to an XML string.

        Parameters:
            json_data (dict): The JSON string to convert to XML.

        Returns:
            str: The XML string containing the equivalent JSON data.
        """
        def _dict_to_xml(element, dictionary):
            for key, value in dictionary.items():
                if isinstance(value, dict):
                    sub_element = ET.SubElement(element, key)
                    _dict_to_xml(sub_element, value)
                else:
                    ET.SubElement(element, key).text = str(value)
        if json_data["passport_type_id"] == 1:
            data = {"SubdivisionCode": json_data["passport_org_code"],
                    "IdOksm": json_data["residence_country_id"],
                    "Surname": json_data["second_name"],
                    "Name": json_data["first_name"],
                    "Patronymic": json_data["middle_name"]}
        else:
            data = {}
        root = ET.Element("PackageData")
        _dict_to_xml(root, data)
        return ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
