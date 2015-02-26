#!/bin/bash

function jar_sizes {
    url="http://localhost:4502/bin/querybuilder.json?type=nt:file&nodename=*.jar&orderby=@jcr:content/jcr:lastModified&orderby.sort=desc"
    path="$..size"
    result=`./ask.py "$url" "$path"`
    echo "result : $result"
}

function search {
    toSearch=$1
    path="http://localhost:4502/bin/querybuilder.json?fulltext=${toSearch}&orderby=@jcr:score&orderby.sort=desc"
    path="$..path"
    result=`./ask.py "$url" "$path"`
    echo "$result"
}