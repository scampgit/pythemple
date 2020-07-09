#!/usr/bin/env python3
""" examples w/ cli args """

import sys

def main():
    """ examples of entry point """

    if not sys.argv[1:]:
        raise RuntimeError('Usage: wordfreq FILE')

if __name__ == "__main__":
    main()
    sys.exit()
