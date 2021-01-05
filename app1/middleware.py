import requests
import json

class Cov19Middleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("i am constructor")
        cov19()



    def __call__(self,request, *args, **kwargs):
        response = self.get_response(request)
        print("i am call")
        return response

def cov19():
    response = requests.get("https://api.covid19india.org/state_district_wise.json")
    print(response.status_code)
    dict_data = json.loads(response.text)
    json.dump(dict_data, open("app1/raw/cov19.json", "w"))
    print("data is written")
