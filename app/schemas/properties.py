from typing import Optional
from pydantic import BaseModel, Field, StringConstraints


class SoldProperties(BaseModel):
    location: str
    pageNumber: Optional[int] = 1


class FetchProperties(BaseModel):
    UPRN: int


class Suggestion(BaseModel):
    location: str


class PropertiesForSale(BaseModel):
    added: str = "" #'3_days',  # optional
    bedsMax:str = "" # '10',  # optional
    bedsMin: str = "" # '1',  # optional
    includeRetirementHomes:bool  # optional
    includeSharedOwnership: bool  # optional
    includeSold: bool  # optional
    isAuction: bool   # optional
    location_identifier: str # 'london',
    location_value: str # 'London',
    newHomes: str = "" # 'only',  # optional
    page: int = 1 # '1',  # optional default=1
    priceMax: int = 15000000 # '15000000',  # optional
    priceMin: int = 10000 # '10000',  # optional
    propertySubType: str # 'park_home%2Cbungalow%2Cfarms_land%2Cflats%2Cterraced%2Csemi_detached',  # optional
    radius: str  = "" # '0.25',  # optional
    # section: 'for-sale',  # Always
    # sortOrder: 'newest_listings'



class PropertyDetails(BaseModel):
    listId :int