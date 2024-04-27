from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
import json
import requests
from schemas.properties import PropertiesForSale

router = APIRouter()

import random
file = open('routers/file.txt', 'r')
proxies = ['{}:{}@{}:{}'.format(v.split(':')[2], v.split(':')[3].strip(), v.split(':')[0], v.split(':')[1]) for v in file.readlines() if v.strip()]
file.close()

proxy = random.choice(proxies)
proxies = {
    'http':'http://{}'.format(proxy),
    'https':'http://{}'.format(proxy)
}





@router.post("", status_code=status.HTTP_200_OK)
async def properties_for_sale(params:PropertiesForSale):
    """
    This API is used to get the data
    of Properties Data for Sale
    """
    added = params.added
    bed_max = params.bedsMax
    bed_min = params.bedsMin
    includeRetirementHomes = params.includeRetirementHomes
    includeSharedOwnership = params.includeSharedOwnership
    includeSold = params.includeSold
    isAuction = params.isAuction
    location_identifier = params.location_identifier
    location_value = params.location_value
    newHomes = params.newHomes
    page = params.page
    priceMax = params.priceMax
    priceMin = params.priceMin
    radius = params.radius
    propertySubType = params.propertySubType
    url = f'https://www.zoopla.co.uk/api/search/mobile/?added={added}&bedsMax={bed_max}&bedsMin={bed_min}&includeRetirementHomes={includeRetirementHomes}&includeSharedOwnership={includeSharedOwnership}&includeSold={includeSold}&isAuction={isAuction}&location.identifier={location_identifier}&location.value={location_value}&newHomes={newHomes}&page={page}&priceMax={priceMax}&priceMin={priceMin}&propertySubType={propertySubType}&radius={radius}&section=for-sale&sortOrder=newest_listings'
    headers = {
        'x-api-key': 'ipqd2r4biqve2yh49sjxaujvpppey8s',
        'Host': 'www.zoopla.co.uk',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.2'
    }
    from base64 import b64decode

    import requests

    api_response = requests.post(
        "https://api.zyte.com/v1/extract",
        auth=("fa3af43178494478b7b971f0076e4d38", ""),
        verify=False,
        json={
            "url": url,
            "httpResponseBody": True,
            "customHttpRequestHeaders": [
                {
                    "name": 'x-api-key',
                    "value": 'ipqd2r4biqve2yh49sjxaujvpppey8s',
                },
                {
                    "name": 'Host',
                    "value": 'https://www.zoopla.co.uk',
                },
                {
                    "name": 'User-Agent',
                    "value": 'okhttp/4.9.2',
                },
            ]
        }
    )
    
    return JSONResponse({"data": json.loads(api_response.text)}, status_code=status.HTTP_200_OK)