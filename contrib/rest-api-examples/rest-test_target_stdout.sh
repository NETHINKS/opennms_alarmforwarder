#! /bin/bash

JSON_DATA="{\"message\": \"Testing the StdoutForwarder with custom message\" }"

curl \
    -Haccept:application/json \
    -Hcontent-type:application/json \
    --user admin:admin \
    -X POST \
    --data "${JSON_DATA}" \
    http://localhost:5000/targets/stdout/test
