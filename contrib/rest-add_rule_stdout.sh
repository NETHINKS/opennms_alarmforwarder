#! /bin/bash

JSON_DATA="{\"rule_match\": \"alarm_uei~.*nodeDown\", \
            \"rule_target\": \"stdout\"}"

curl \
    -Haccept:application/json \
    -Hcontent-type:application/json \
    -X POST \
    --data "${JSON_DATA}" \
    http://localhost:5000/rules/add
