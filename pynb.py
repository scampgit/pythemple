#!/usr/bin/env python

import pynetbox
import sys

def main():
    print(f"arg: {sys.argv} ... ")
    if len(sys.argv) < 3: 
        print(f"sorry, {sys.argv[0]} dorsn't have enought tips")
        sys.exit(-1)
    nb_url = sys.argv[1]
    nbox = pynetbox.api(url=nb_url, token=sys.argv[2])
    #all_prefixes = nbox.ipam.prefixes.all()
    try:
        get_devs = nbox.dcim.devices.filter('gpn')
    except pynetbox.core.query.RequestError as e:
        print(f"wooops bad bad - {e}")
        sys.exit()

    moned = []
    not_moned = []
    indicies = []

    for key,val in enumerate(get_devs):
        if "mon" in val.tags:
            #print("already monitored:")
            print(f"monitored - name: {val.name} / tags: {val.tags} / index = {key}")
            moned.append(val)
        else:
            #print("oops not moned:")
            print(f"not monitored - index = {key} / name: {val.name} / tags: {val.tags}")
            not_moned.append(val)
            indicies.append(key)
            val.tags.append("mon")

    #print(f"moned: {moned}")
    #print(f"not moned: {not_moned}")
    x = input("save? (Y/N): ")
    if x == "Y": 
        print("YED!")
        for _ in indicies:
            print(f"{_}: name: {get_devs[_].name} / tags: {get_devs[_].tags}")
            y = input("\n\n save save? (Y/N)")
            if y == "Y": get_devs[_].save()
    else: print("No...")

if __name__ == '__main__':
    main()
    exit()
