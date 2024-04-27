from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
import json
import requests
from schemas.properties import Suggestion

router = APIRouter()


@router.post("", status_code=status.HTTP_200_OK)
async def suggestion(params:Suggestion):
    """
    This API is used for suggestion
    """

    suggestion_api = 'https://api-graphql-lambda.prod.zoopla.co.uk/graphql/'
    headers = {
        'accept': '*/*',
        'x-api-key': '3Vzj2wUfaP3euLsV4NV9h3UAVUR3BoWd5clv9Dvu',
        'origin': 'zoopla-mobile-app',
        'Content-Type': 'application/json',
        'Content-Length': '271',
        'Host': 'api-graphql-lambda.prod.zoopla.co.uk',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.2'
    }
    payload = {
        "operationName": "getSearchSuggestions",
        "variables": {
            "locationPrefix": params.location
        },
        "query": "query getSearchSuggestions($locationPrefix: String!) {\n  geoSuggestion(locationPrefix: $locationPrefix) {\n    geoIdentifier\n    geoLabel\n    geoSubLabel\n    __typename\n  }\n}"
    }

    resp = requests.post(url=suggestion_api, headers=headers, data=json.dumps(payload), verify=False, timeout=10)
    print(resp)
    return JSONResponse({"data": json.loads(resp.text)['data']}, status_code=status.HTTP_200_OK)