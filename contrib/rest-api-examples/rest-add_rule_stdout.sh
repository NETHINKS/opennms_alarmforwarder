#! /bin/bash

JSON_DATA="{\"rule_match\": \"alarm_uei~.*nodeDown\", \
            \"rule_delay\": \"300\", \
            \"rule_maxforwardings\": \"0\", \
            \"rule_target\": \"stdout\"}"

curl \
    -Haccept:application/json \
    -Hcontent-type:application/json \
    --user admin:admin \
    -X POST \
    --data "${JSON_DATA}" \
    http://localhost:5000/rules/add
