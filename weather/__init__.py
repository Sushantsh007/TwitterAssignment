from flask import *
import urllib.request
weather = Blueprint('weather',__name__)

@weather.route('/',methods=['GET'])
def giveResponse():
    try:
        lat = request.args.get("lat")
        lon = request.args.get("lon")
        API_key = "f0611943c14794692c197d5b3ebf5694"
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
        print(url)
        response = urllib.request.urlopen(url)
        data = response.read()
        
        data = data.decode('UTF-8')  

        return data
    except:
        data = {'error': "Invalid data sent"}
        status_code = 404
        response = make_response(jsonify(data), status_code)
        return response 