#!/usr/bin/env python3

def main():
    ## create a dictionary
    switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

    ## display parts of the dictionary
    print( switch['hostname'] )
    print( switch['ip'] )

    ## request a 'fake' key
    #print( switch['lynx'] )

    print( "First test - .get()" )
    print( switch.get('lynx') )

    print( "Second test - .get()" )
    print( switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE ") )

    print( "Third test - .get()" )
    print( switch.get('version') )

    print( "Forth test - .keys()" )
    print( switch.keys() )

    print( "Fifth test - .values()" )
    print( switch.values() )
    
    print( "Sixth test - .pop()" )
    print( switch.pop('version') ) # removes this key (and value) pair
    print( switch.keys() )
    print( switch.values() )

    print( "Seventh test - Add a new value " )
    switch['adminlogin'] = 'karl08'
    print( switch.keys() )
    print( switch.values() )
    
    print( "Eighth test - ADD a new value " )
    switch['password'] = 'querty'
    print( switch.keys() )
    print( switch.values() )

main()
