#!/usr/bin/env python

from __future__ import print_function
from sys import exit, stderr
try:
    from urllib.request import urlopen, HTTPError, URLError
except ImportError:
    from urllib2 import urlopen, HTTPError, URLError

try:
    from ssl import SSLError
except ImportError:
    class SSLError():
        pass

def errorExit(err, status):
    print(err, file=stderr)
    exit(status)

def getHTML(url):
    try:
        html = urlopen(url)
    except SSLError as err:
        print("\n" + err)
        return
    except HTTPError as err:
        print("\n" + err)
        return
    except URLError as err:
        errorExit(
                (
                    "Unable to connect to %s\n"
                    "Site may be down or refusing connections\n"
                    "%s" % (archive, err)
                ),
                1
        )

    return html.read().decode('utf-8')

