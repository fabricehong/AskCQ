#!/usr/bin/python
__author__ = 'fabrice'

import query
import sys

# xpath examples : https://code.google.com/p/jsonpath/wiki/Javascript
# querybuilder REST api : https://docs.adobe.com/docs/en/cq/current/dam/customizing_and_extendingcq5dam/query_builder.html

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "not enough arguments"
        exit(1)
    url = sys.argv[1] # example : http://localhost:4502/bin/querybuilder.json?type=nt:file&nodename=*.jar&orderby=@jcr:content/jcr:lastModified&orderby.sort=desc
    path = sys.argv[2] # example : hits.size
    if len(sys.argv) == 4:
        print "url : ", url
        print "path : ", path
    query.query(
        url,
        path
    )