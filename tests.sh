#!/bin/bash
# Add a record
add=$(/usr/bin/curl -X POST -H "Content-Type: application/json" -H "Cache-Control: no-cache"  -d '{"uid" : "1" , "name" : "John Doe", "date" : "2015-05-12T14:36:00.451765", "md5checksum" : "f6903e9838720c98ed4098d842264d7c"}' "http://127.0.0.1:8080/api/add")

if echo $add | grep f6903e9838720c98ed4098d842264d7c; then
	echo "Record Added" 
else
	echo failed
fi

count=$(curl -X GET -H "Content-Type: application/json" -H "Cache-Control: no-cache" -H "Postman-Token: be95b50b-8979-88b5-5b45-a22bf66e043c" "http://127.0.0.1:8080/api/count?uid=1&date=2015-05-12")

if echo $count | grep result; then
	echo "Count Succeeded" 
else
	echo failed
fi
