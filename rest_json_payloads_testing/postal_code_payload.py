from __future__ import print_function
import requests
import json
data =  { "pin_code": "",
         "city": "",
         "state": "rajasthan"
         }
mapped_data = {"3420":"jodhpur","3130":"udaipur", "3020":"jaipur"}
for i in range(1,30):
    tmp = "0" +str(i) if i < 10  else str(i)
    for key in mapped_data.keys():
        data["pin_code"] = key + tmp
        data["city"] = mapped_data[key]
        #print(data)
        resp =  requests.post("http://localhost:8000/api/postalcode/", data=json.loads(json.dumps(data)))
        print(resp, data["pin_code"])
