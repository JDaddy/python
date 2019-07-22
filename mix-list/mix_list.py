#!/usr/bin/env python3

my_list = [ "192.168.0.5", 5060, "UP" ]
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
string2 = " I am unable to ping ports "
print("When I ssh into IP addresses " + new_list[3] + " or " + new_list[4] + string2 + str(new_list[0]) + " , " + new_list[1] + " , " + str(new_list[2]) + ".")

#print("The first item in the list (IP): " + my_list[0] )
#print("The second item in the list (Port): " + str(my_list[1]) )
#print("The last item in the list (IP): " + my_list[2] )
