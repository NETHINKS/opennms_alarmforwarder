#! /bin/bash

curl -Haccept:application/json \
    --user admin:admin \
    http://localhost:5000/admin/users/demo/delete
