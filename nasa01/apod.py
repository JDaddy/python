#!/usr/bin/env python3

import urllib.request
import json
import webbrowser
from pprint import pprint as pp # part of the standard library
## define some constants
## Define APOD
apodurl = 'https://api.nasa.gov/planetary/apod?'
NASAAPI= 'https://api.nasa.gov/planetary/apod?'
#mykey = 'api_key=DEMO_KEY'  ## your key goes in place of DEMO_KEY'
mykey = 'api_key=oYHVOw7QNEVeRe89VLD3aQZrXTJG3TGCIEsKCDGO'  ## your key goes in place of DEMO_KEY'
MYKEY= 'api_key=oYHVOw7QNEVeRe89VLD3aQZrXTJG3TGCIEsKCDGO'  ## this is our api key 

def main():
    nasaapiobj = urllib.request.urlopen(NASAAPI+ MYKEY) # call the webservice
    apodread = nasaapiobj.read() # parse the JSON blob returned`
    convertedjson= json.loads(apodread.decode('utf-8')) # convert json
    
    # Show Pretty Print json
    pp(convertedjson) # display the value for the key explanation
    input('\nPress ENTER to view this photo of the day') # pause for ENTER

    webbrowser.open(convertedjson['hdurl'])

main()


