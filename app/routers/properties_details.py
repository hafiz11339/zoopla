from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
import json
import requests
from schemas.properties import PropertyDetails

router = APIRouter()


@router.post("", status_code=status.HTTP_200_OK)
async def fetch_properties(params:PropertyDetails):
    """
    This API is used to get the data
    detail of properties
    """

    listing_details_api = 'https://api-graphql-lambda.prod.zoopla.co.uk/graphql/'
    headers = {
        'accept': '*/*',
        'x-api-key': '3Vzj2wUfaP3euLsV4NV9h3UAVUR3BoWd5clv9Dvu',
        'cookie': 'zooplasid=73483403cf484419a32a325535aec20a;zooplapsid=6495751daf594668a0b7d6a875abb2af;',
        'origin': 'zoopla-mobile-app',
        'Content-Type': 'application/json',
        'Content-Length': '8436',
        'Host': 'api-graphql-lambda.prod.zoopla.co.uk',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.2',
    }
    payload = {
        "operationName": "getListingDetails",
        "variables": {
            "listingId": params.listId,
            "include": ["EXPIRED"]
        },
        "query": "query getListingDetails($listingId: Int!, $include: [ListingInclusion]) {\n  listingDetails(id: $listingId, include: $include) {\n    ...LISTING\n    ... on ListingResultError {\n      errorCode\n      message\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment LISTING on ListingData {\n  listingId\n  administrationFees\n  detailedDescription\n  metaTitle\n  metaDescription\n  category\n  listingUris {\n    detail\n    __typename\n  }\n  title\n  publicationStatus\n  counts {\n    numBedrooms\n    numBathrooms\n    numLivingRooms\n    __typename\n  }\n  viewCount {\n    viewCount30day\n    __typename\n  }\n  ntsInfo {\n    title\n    value\n    __typename\n  }\n  derivedEPC {\n    efficiencyRating\n    __typename\n  }\n  ...AGENT_BRANCH\n  ...LISTING_ANALYTICS_TAXONOMY\n  ...LISTING_ADTARGETING\n  ...LISTING_ANALYTICS_ECOMMERCE\n  ...PRICING\n  ...ENERGY_PERFORMANCE_CERTIFICATE\n  ...LISTING_FEATURES\n  ...FLOOR_PLANS\n  ...FLOOR_AREA\n  ...MEDIA\n  ...MAP\n  ...EMBEDDED_CONTENT\n  ...POINTS_OF_INTEREST\n  ...PRICE_HISTORY\n  ...LISTING_SUMMARY\n  __typename\n}\n\nfragment AGENT_BRANCH on ListingData {\n  branch {\n    ...AGENT_BRANCH_FRAGMENT\n    __typename\n  }\n  __typename\n}\n\nfragment AGENT_BRANCH_FRAGMENT on AgentBranch {\n  branchId\n  address\n  branchDetailsUri\n  branchResultsUri\n  logoUrl\n  phone\n  name\n  postcode\n  memberType\n  attributes {\n    embeddedContentIsBlacklisted\n    showOverseasListingExactLocation\n    __typename\n  }\n  profile {\n    details\n    __typename\n  }\n  __typename\n}\n\nfragment LISTING_ANALYTICS_TAXONOMY on ListingData {\n  analyticsTaxonomy {\n    ...LISTING_ANALYTICS_TAXONOMY_FRAGMENT\n    __typename\n  }\n  __typename\n}\n\nfragment LISTING_ANALYTICS_TAXONOMY_FRAGMENT on ListingAnalyticsTaxonomy {\n  acorn\n  acornType\n  areaName\n  bedsMax\n  bedsMin\n  branchId\n  branchLogoUrl\n  branchName\n  brandName\n  chainFree\n  companyId\n  countryCode\n  countyAreaName\n  currencyCode\n  displayAddress\n  furnishedState\n  groupId\n  hasEpc\n  hasFloorplan\n  incode\n  isRetirementHome\n  isSharedOwnership\n  listingCondition\n  listingId\n  listingsCategory\n  listingStatus\n  location\n  memberType\n  numBaths\n  numBeds\n  numImages\n  numRecepts\n  outcode\n  postalArea\n  postTownName\n  priceActual\n  price\n  priceMax\n  priceMin\n  priceQualifier\n  propertyHighlight\n  propertyType\n  regionName\n  section\n  sizeSqFeet\n  tenure\n  uuid\n  zindex\n  __typename\n}\n\nfragment LISTING_ADTARGETING on ListingData {\n  adTargeting {\n    ...LISTING_ANALYTICS_TAXONOMY_FRAGMENT\n    __typename\n  }\n  __typename\n}\n\nfragment LISTING_ANALYTICS_ECOMMERCE on ListingData {\n  analyticsEcommerce {\n    ...LISTING_ANALYTICS_ECOMMERCE_FRAGMENT\n    __typename\n  }\n  __typename\n}\n\nfragment LISTING_ANALYTICS_ECOMMERCE_FRAGMENT on ListingAnalyticsEcommerce {\n  brand\n  category\n  id\n  name\n  price\n  quantity\n  variant\n  __typename\n}\n\nfragment PRICING on ListingData {\n  pricing {\n    ...PRICING_FRAGMENT\n    __typename\n  }\n  __typename\n}\n\nfragment PRICING_FRAGMENT on ListingPricing {\n  isAuction\n  qualifier\n  priceQualifierLabel\n  internalValue\n  rentFrequencyLabel\n  valueLabel\n  currencyCode\n  originalCurrencyPrice {\n    internalValue\n    rentFrequencyLabel\n    unitsLabel\n    label\n    valueLabel\n    currencyCode\n    __typename\n  }\n  pricePerFloorAreaUnit {\n    internalValue\n    rentFrequencyLabel\n    unitsLabel\n    label\n    valueLabel\n    currencyCode\n    __typename\n  }\n  alternateRentFrequencyPrice {\n    internalValue\n    rentFrequencyLabel\n    unitsLabel\n    label\n    valueLabel\n    currencyCode\n    __typename\n  }\n  __typename\n}\n\nfragment ENERGY_PERFORMANCE_CERTIFICATE on ListingData {\n  epc {\n    image {\n      caption\n      filename\n      __typename\n    }\n    pdf {\n      caption\n      original\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment LISTING_FEATURES on ListingData {\n  detailedDescription\n  features {\n    ...LISTING_FEATURES_FRAGMENT\n    __typename\n  }\n  __typename\n}\n\nfragment LISTING_FEATURES_FRAGMENT on Features {\n  bullets\n  flags {\n    furnishedState {\n      name\n      label\n      __typename\n    }\n    studentFriendly\n    tenure {\n      name\n      label\n      __typename\n    }\n    availableFromDate\n    __typename\n  }\n  highlights {\n    description\n    label\n    __typename\n  }\n  __typename\n}\n\nfragment FLOOR_PLANS on ListingData {\n  floorPlan {\n    ...FLOOR_PLANS_FRAGMENT\n    __typename\n  }\n  __typename\n}\n\nfragment FLOOR_PLANS_FRAGMENT on FloorPlan {\n  image {\n    filename\n    caption\n    __typename\n  }\n  links {\n    url\n    label\n    __typename\n  }\n  pdf {\n    original\n    caption\n    __typename\n  }\n  __typename\n}\n\nfragment FLOOR_AREA on ListingData {\n  floorArea {\n    ...FLOOR_AREA_FRAGMENT\n    __typename\n  }\n  __typename\n}\n\nfragment FLOOR_AREA_FRAGMENT on FloorArea {\n  label\n  range {\n    maxValue\n    maxValueLabel\n    minValue\n    minValueLabel\n    __typename\n  }\n  units\n  unitsLabel\n  value\n  __typename\n}\n\nfragment MEDIA on ListingData {\n  content {\n    virtualTour {\n      ...MEDIA_FRAGMENT\n      __typename\n    }\n    floorPlan {\n      ...MEDIA_FRAGMENT\n      __typename\n    }\n    audioTour {\n      ...MEDIA_FRAGMENT\n      __typename\n    }\n    __typename\n  }\n  propertyImage {\n    ...MEDIA_FRAGMENT\n    __typename\n  }\n  additionalLinks {\n    ...MEDIA_FRAGMENT\n    ... on AdditionalLink {\n      href\n      label\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment MEDIA_FRAGMENT on Media {\n  original\n  caption\n  url\n  filename\n  type\n  __typename\n}\n\nfragment MAP on ListingData {\n  location {\n    ...LISTING_LOCATION_FRAGMENT\n    __typename\n  }\n  __typename\n}\n\nfragment LISTING_LOCATION_FRAGMENT on ListingLocation {\n  coordinates {\n    isApproximate\n    latitude\n    longitude\n    __typename\n  }\n  postalCode\n  streetName\n  countryCode\n  propertyNumberOrName\n  townOrCity\n  __typename\n}\n\nfragment EMBEDDED_CONTENT on ListingData {\n  embeddedContent {\n    videos {\n      ...MEDIA_FRAGMENT\n      __typename\n    }\n    tours {\n      ...MEDIA_FRAGMENT\n      __typename\n    }\n    links {\n      ...MEDIA_FRAGMENT\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment POINTS_OF_INTEREST on ListingData {\n  pointsOfInterest {\n    ...POINTS_OF_INTEREST_FRAGMENT\n    __typename\n  }\n  __typename\n}\n\nfragment POINTS_OF_INTEREST_FRAGMENT on PointOfInterest {\n  title\n  address\n  type\n  latitude\n  longitude\n  distanceMiles\n  __typename\n}\n\nfragment PRICE_HISTORY on ListingData {\n  priceHistory {\n    firstPublished {\n      firstPublishedDate\n      priceLabel\n      __typename\n    }\n    lastSale {\n      date\n      newBuild\n      price\n      priceLabel\n      recentlySold\n      __typename\n    }\n    priceChanges {\n      isMinorChange\n      isPriceDrop\n      isPriceIncrease\n      percentageChangeLabel\n      priceChangeDate\n      priceChangeLabel\n      priceLabel\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment LISTING_SUMMARY on ListingData {\n  listingId\n  displayAddress\n  category\n  location {\n    postalCode\n    streetName\n    uprn\n    __typename\n  }\n  section\n  branch {\n    logoUrl\n    name\n    __typename\n  }\n  counts {\n    numBedrooms\n    numBathrooms\n    numLivingRooms\n    __typename\n  }\n  featurePreview {\n    iconId\n    content\n    __typename\n  }\n  floorArea {\n    label\n    range {\n      maxValue\n      maxValueLabel\n      minValue\n      minValueLabel\n      __typename\n    }\n    units\n    unitsLabel\n    value\n    __typename\n  }\n  imagePreview {\n    caption\n    src\n    __typename\n  }\n  propertyImage {\n    caption\n    original\n    __typename\n  }\n  listingUris {\n    contact\n    detail\n    __typename\n  }\n  pricing {\n    label\n    internalValue\n    __typename\n  }\n  tags {\n    label\n    __typename\n  }\n  title\n  transports {\n    distanceInMiles\n    poiType\n    title\n    __typename\n  }\n  publicationStatus\n  publishedOn\n  numberOfImages\n  statusSummary {\n    label\n    __typename\n  }\n  ...LISTING_ANALYTICS_TAXONOMY\n  __typename\n}"
    }

    resp = requests.post(url=listing_details_api, headers=headers, data=json.dumps(payload), verify=False, timeout=10)

    return JSONResponse({"data": json.loads(resp.text)['data']}, status_code=status.HTTP_200_OK)