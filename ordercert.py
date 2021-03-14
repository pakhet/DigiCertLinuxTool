import requests
import json


def ordercert(cn, c, st, l, o, csrpath):
    with open('package.json') as f:
        data = json.load(f)
    data.update(common_name=cn)
    url = "https://www.digicert.com/services/v2/order/certificate/ssl_basic"

    payload = data
    headers = {
        'X-DC-DEVKEY': "{{api_key}}",
        'Content-Type': "application/json"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    print(payload)
