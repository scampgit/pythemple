#!/usr/bin/env python3
""" simple task for mass nb routine """

import sys
import pynetbox

def main():
    """ all in one """

    print(f"arg: {sys.argv} ... ")
    if len(sys.argv) < 3:
        print(f"sorry, {sys.argv[0]} dorsn't have enought tips")
        sys.exit(-1)
    nb_url = sys.argv[1]
    nbox = pynetbox.api(url=nb_url, token=sys.argv[2])
    #all_prefixes = nbox.ipam.prefixes.all()
    try:
        get_devs = nbox.dcim.devices.filter('gpn')
    except pynetbox.core.query.RequestError as err:
        print(f"wooops bad bad - {err}")
        sys.exit()

    moned = []
    not_moned = []
    indicies = []

    for key, val in enumerate(get_devs):
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

    if input("save? (Y/N): ") == "Y":
        print("YED!")
        for _ in indicies:
            print(f"{_}: name: {get_devs[_].name} / tags: {get_devs[_].tags}")
            if input("save? (Y/N): ") == "Y":
                get_devs[_].save()
    else: print("No...")

if __name__ == '__main__':
    main()
    sys.exit()
