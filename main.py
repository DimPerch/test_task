import xml.etree.ElementTree as ET
from flask import Flask, request, Response, jsonify
from converter import Converter


app = Flask(__name__)


@app.route('/', methods=['POST'])
def convert():
    direction = request.args.get('direction')

    if direction == 'json_to_xml':
        data = request.json
        response = Converter.json_to_xml(data)
        return Response(response, status=200, content_type='application/xml')
    elif direction == 'xml_to_json':
        data = request.data
        response = Converter.xml_to_json(data)
        print("xml to json")
        return jsonify(response), 200, {'Content-Type': 'application/json'}
    else:
        return "Invalid conversion direction", 400


if __name__ == '__main__':
    app.run(debug=True)
