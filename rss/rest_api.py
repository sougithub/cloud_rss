# -*- coding: utf-8 -*-
import azure_rss, aws_status, gcp_rss
import time
from flask import Flask, jsonify, abort, make_response

api = Flask(__name__)

@api.route('/cloud_status/', methods=['GET'])
def cloud_status():
    start = time.time()
    response = {}
    response['azure'] = azure_rss.read()
    response['aws'] = aws_status.read()
    response['gcp'] = gcp_rss.read()
    response['time'] = time.time() - start
    return make_response(jsonify(response))
    # Unicodeにしたくない場合は↓
    # return make_response(json.dumps(result, ensure_ascii=False))

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@api.errorhandler(500)
def server_error(error):
    return make_response(jsonify({'error': error}), 500)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)