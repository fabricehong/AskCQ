__author__ = 'fabrice'

import urllib2
import pythonpath
import json
import pprint

def query(url, jsonPath):
    response = getHttpResponse(url)
    object = json.loads(response)
    result = pythonpath.jsonpath(object, jsonPath)
    pprint.pprint(result)



def getHttpResponse(url):
    manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
    manager.add_password(None, 'http://localhost:4502/', 'admin', 'admin')
    handler = urllib2.HTTPBasicAuthHandler(manager)


    # create "opener" (OpenerDirector instance)
    opener = urllib2.build_opener(handler)

    # use the opener to fetch a URL
    result = opener.open(url)
    return result.read()

    # result.read() will contain the data
    # result.info() will contain the HTTP headers

    # To get say the content-length header
    # length = result.info()['Content-Length']
    #return result
