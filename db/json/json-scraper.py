#!/opt/homebrew/bin/python3


import requests
import json


def send_request(pageNumberVar):
    print(pageNumberVar)

    try:
        response = requests.post(
            url="https://treaties.fcdo.gov.uk/awweb/awfp/search/1",
            headers={
                "Cookie": "JSESSIONID=49BF32AC229DA2A741FC4BAF9836C239;",
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps(
                {
                    "searchDetails": {
                        "sortBy": [
                            {
                                "sequence": 0,
                                "keyType": 1,
                                "isAscending": True,
                                "fieldName": "signed_event_date",
                            }
                        ],
                        "queryStr": "*",
                        "pageNumber": 1,
                        "searchMode": {"mode": "SEARCH"},
                        "offset": pageNumberVar,
                        "pageSize": 100,
                    },
                    "searchLibraryList": ["library2_lib"],
                    "isReturnFacets": True,
                }
            ),
        )
#         print(response.content)
        with open(str(pageNumberVar) + '_batch.json', 'w') as f:
            print(response.text, file=f)
    except requests.exceptions.RequestException:
        print("HTTP Request failed")

for x in range(21000, 21437):
    send_request(x)