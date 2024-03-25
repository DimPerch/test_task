from flask import Flask, request, Response, jsonify
from converter import Converter


app = Flask(__name__)


@app.route('/api/json_to_xml', methods=['POST'])
def json_to_xml():
    """
    method for convertation json to xml
    """
    data = request.json
    response = Converter.json_to_xml(data)
    return Response(response.encode('utf-8'), status=200, content_type='application/xml')


@app.route('/api/xml_to_json', methods=['POST'])
def xml_to_json():
    """
    method for convertation xml to json
    """
    data = request.data
    response = Converter.xml_to_json(data)
    return jsonify(response), 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
