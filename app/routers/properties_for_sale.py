from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
import json
import requests
from schemas.properties import PropertiesForSale

router = APIRouter()


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
    url = 'https://www.zoopla.co.uk/api/search/mobile/?added=3_days&bedsMax=10&bedsMin=1&includeRetirementHomes=true&includeSharedOwnership=true&includeSold=true&isAuction=true&location.identifier=london&location.value=London&newHomes=only&page=1&priceMax=15000000&priceMin=10000&propertySubType=park_home%2Cbungalow%2Cfarms_land%2Cflats%2Cterraced%2Csemi_detached&radius=0.25&section=for-sale&sortOrder=newest_listings'
    headers = {
        'x-api-key': 'ipqd2r4biqve2yh49sjxaujvpppey8s',
        'Host': 'www.zoopla.co.uk',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.2'
    }
    resp = requests.get(url=url, headers=headers, verify=False, timeout=10)
    return JSONResponse({"data": json.loads(resp.text)['data']}, status_code=status.HTTP_200_OK)