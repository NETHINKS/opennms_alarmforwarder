#! /bin/bash

JSON_DATA="{\"user_name\": \"demo\", \
            \"user_password\": \"demo\"}"

curl \
    -Haccept:application/json \
    -Hcontent-type:application/json \
    --user admin:admin \
    -X POST \
    --data "${JSON_DATA}" \
    http://localhost:5000/admin/users/add
