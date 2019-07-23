#!/usr/bin/env python3

import urllib.request
import json

## Define NEOapi
neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = 'start_date=2018-06-01'
enddate = '&end_date=END_DATE'
mykey = '&api_key=oYHVOw7QNEVeRe89VLD3aQZrXTJG3TGCIEsKCDGO'

neourl = neourl + startdate + mykey

## Call the webservice
neourlobj = urllib.request.urlopen(neourl)

## read the file-like object
neoread = neourlobj.read()

## decode json to phython data structure
decodeneo = json.loads(neoread.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(decodeneo)


