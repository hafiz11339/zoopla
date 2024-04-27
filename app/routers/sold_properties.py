from fastapi import APIRouter,status,HTTPException
from fastapi.responses import JSONResponse
import json
import requests
from schemas.properties import SoldProperties
router = APIRouter()

@router.post("", status_code=status.HTTP_200_OK)
async def sold_properties(properties_data:SoldProperties):
    """
    This API is used to get the data of sold properties
    """
    
   


    url = 'https://api-graphql-lambda.prod.zoopla.co.uk/graphql/'
    headers = {
        "accept": "*/*",
        "x-api-key": "3Vzj2wUfaP3euLsV4NV9h3UAVUR3BoWd5clv9Dvu",
        "origin": "zoopla-mobile-app",
        "Content-Type": "application/json",
        "Content-Length": "2595",
        "Host": "api-graphql-lambda.prod.zoopla.co.uk",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/4.9.2"
    }


    pg_num = (properties_data.pageNumber - 1) * 12
    if pg_num > 10000:
        pg_num = 0
    payload = {
                    "operationName": "propertiesSearchResults",
                    "variables": {
                        "geoIdentifier": properties_data.location.lower().replace(' ', '-'),
                        "first": 12,
                        "after": str(pg_num)
                    },
                    "query": "query propertiesSearchResults($geoIdentifier: GeoIdentifier, $geoString: NonEmptyString, "
                            "$houseType: HouseType, $rangeMonths: MarketActivityWindow, $after: ID, $first: PositiveInt, "
                            "$fromLastSaleDate: String, $propertyTypeCode: String, $sortDirection: String, $sortOrder: "
                            "String, $toLastSaleDate: String) {\n  propertiesSearch(\n    after: $after\n    first: "
                            "$first\n    input: {geoIdentifier: $geoIdentifier, fromLastSaleDate: $fromLastSaleDate, "
                            "propertyTypeCode: $propertyTypeCode, sortDirection: $sortDirection, sortOrder: $sortOrder, "
                            "toLastSaleDate: $toLastSaleDate}\n  ) {\n    ...PropertiesSearchConnection\n    "
                            "...PropertiesSearchResponseError\n    __typename\n  }\n  area(geoIdentifier: $geoIdentifier) "
                            "{\n    geoType\n    id\n    name\n    shortName\n    __typename\n  }\n  marketActivity(\n    "
                            "geoIdentifier: $geoIdentifier\n    geoString: $geoString\n    houseType: $houseType\n    "
                            "rangeMonths: $rangeMonths\n  ) {\n    data {\n      averagePricePaid\n      propertiesSold\n "
                            "     __typename\n    }\n    __typename\n  }\n}\n\nfragment PropertiesSearchConnection on "
                            "PropertiesSearchConnection {\n  pageInfo {\n    hasPreviousPage\n    hasNextPage\n   "
                            " startCursor\n    endCursor\n    __typename\n  }\n  totalResults\n  edges {\n    cursor\n    "
                            "node {\n      propertyId\n      uprn\n      address {\n        fullAddress\n        postcode\n"
                            "        country\n        outcode\n        latitude\n        longitude\n        __typename\n   "
                            "   }\n      attributes {\n        bathrooms\n        bedrooms\n        livingRooms\n        "
                            "propertyType\n        tenure\n        __typename\n      }\n      history {\n        "
                            "historicSales {\n          date\n          price\n          percentageChange\n         "
                            " numericChange\n          __typename\n        }\n        soldPricesDataSource\n        "
                            "__typename\n      }\n      saleEstimate {\n        lowerPrice\n        currentPrice\n       "
                            " upperPrice\n        confidenceLevel\n        __typename\n      }\n      rentEstimate {\n     "
                            "   currentPrice\n        lowerPrice\n        upperPrice\n        __typename\n      }\n      "
                            "trackedProperty {\n        isTracked\n        permissions {\n          hasPermissions\n        "
                            "  ids\n          __typename\n        }\n        relationship\n        __typename\n      }\n    "
                            "  __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment "
                            "PropertiesSearchResponseError on PropertiesSearchResponseError {\n  errors {\n    message\n   "
                            " __typename\n  }\n  __typename\n}"
                }

    resp = requests.post(url=url, headers=headers, data=json.dumps(payload), verify=False, timeout=20)
    return JSONResponse({"data":json.loads(resp.text)['data']}, status_code=status.HTTP_200_OK)