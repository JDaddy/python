#!/usr/bin/env python3

# yaml is NOT part of the standard library
# python3 -m pip install pyyaml
import yaml

def main():
    ## Open a blob of YAML data
    yammyfile = open("/home/student/python/yamlintro/myYAML.yml", "r")

    ## convert YAML into python data structures (lists and dictionairies)
    pyyammy = yaml.load(yammyfile)

    # display our new python data
    print(pyyammy)

main()
