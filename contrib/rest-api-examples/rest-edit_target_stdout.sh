#! /bin/bash

JSON_DATA="{\"target_name\": \"stdout\", \
            \"target_class\": \"StdoutForwarder\", \
            \"target_parms\": \
                {\"AlertMessage\": \"Forward Alarm: %alarm_logmsg%\", \
                 \"ResolvedMessage\": \"Resolve Alarm: %alarm_logmsg%\"}}"

curl \
    -Haccept:application/json \
    -Hcontent-type:application/json \
    --user admin:admin \
    -X POST \
    --data "${JSON_DATA}" \
    http://localhost:5000/targets/stdout/edit
