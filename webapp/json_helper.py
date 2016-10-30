"""JSON helper methods"""

from flask import jsonify
from flask import request

def json_check():
    """helper method: check if client requests JSON output"""
    best_mime = request.accept_mimetypes.best_match(["application/json", "text/html"])
    if best_mime == "application/json":
        return True
    return False

def json_error(error_msg, error_code):
    output = {}
    output["error_code"] = error_code
    output["error_msg"] = error_msg
    return jsonify(output), error_code

def json_result(result_msg, result_code):
    output = {}
    output["result_code"] = result_code
    output["result_msg"] = result_msg
    return jsonify(output), result_code
