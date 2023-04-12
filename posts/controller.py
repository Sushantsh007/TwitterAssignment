from posts.models import create as Create, get as Get
from flask import *
import jsonpickle

def create():
    try:
        message = request.form['message']
        if len(message) == 0:
            message = None
        lat = request.args.get("lat")
        if len(lat) == 0:
            lat = None
        lon = request.args.get("lon")
        if len(lon) == 0:
            lon = None
        Create(message,lat,lon)
        data = {
            'message': 'Successfully posted this text'
        }
        status_code = 201
        response = make_response(jsonify(data), status_code)
        return response
    except:
        data = {'error': "Couldn't post the text"}
        status_code = 404
        response = make_response(jsonify(data), status_code)
        return response    

def get():
    try:
        lat = request.args.get("lat")
        if len(lat) == 0:
            lat = None
        lon = request.args.get("lon")
        if len(lon) == 0:
            lon = None

        if(lat == None or lon == None):
            data = {'error': "Data is missing"}
            status_code = 404
            response = make_response(jsonify(data), status_code)
            return response

        data = Get(lat,lon)
        
        response = {
            "data": data,
            "success": "True"
        }
        json_data = jsonpickle.encode(response)
        response = Response(response=json_data, status=200)
        return response
    except:
        data = {'error': "Couldn't get the results"}
        status_code = 404
        response = make_response(jsonify(data), status_code)
        return response 