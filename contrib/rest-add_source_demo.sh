#! /bin/bash

JSON_DATA="{\"source_name\": \"Demo\", \
            \"source_url\": \"http://demo.opennms.org/opennms/rest\", \
            \"source_user\": \"demo\", \
            \"source_filter\": \"\", \
            \"source_password\": \"demo\"}"

curl \
    -Haccept:application/json \
    -Hcontent-type:application/json \
    -X POST \
    --data "${JSON_DATA}" \
    http://localhost:5000/sources/add
