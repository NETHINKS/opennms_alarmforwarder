#! /bin/bash
###################################################################################################
#                                                                                                 #
# phone-number-change.sh                                                                          #
# Script for changing the phone number of an opennms_alarmforwarder SmsEagle target               #
#                                                                                                 #
# Michael Batz <michael.batz@nethinks.com>                                                        #
#                                                                                                 #
###################################################################################################

# Config section
ALARMFORWARDER_URL="http://localhost:5000"
ALARMFORWARDER_USER="admin"
ALARMFORWARDER_PASSWORD="admin"
ALARMFORWARDER_TARGET="SmsEagle"
ALARMFORWARDER_TARGET_PARM="target"
PHONE_NEW=$1
PHONE_OLD=""
MSG_TO_OLD_AGENT="Agent logged out. New agent is now "
MSG_TO_NEW_AGENT="Agent logged in. Old agent was "


# get old phone number
REST_RESPONSE=`curl --silent -Haccept:application/json \
                    --user ${ALARMFORWARDER_USER}:${ALARMFORWARDER_PASSWORD} \
                    ${ALARMFORWARDER_URL}/targets/${ALARMFORWARDER_TARGET}`
ERROR_CODE=`echo ${REST_RESPONSE} | sed 's/.*error_code\": \([0-9]*\).*/\1/' | sed 's/.*\".*//'`
PHONE_OLD=`echo ${REST_RESPONSE} | sed 's/.*target\": \"\([0-9+]*\)\".*/\1/' | sed 's/.*\".*//'`
if [ -n "$ERROR_CODE" ]
    then
        echo "Error communicating with alarmforwarder. Exit"
        exit -1
fi


# send message to old agent
MSG_TO_OLD_AGENT="${MSG_TO_OLD_AGENT} ${PHONE_NEW}"
JSON_DATA="{\"message\": \"${MSG_TO_OLD_AGENT}\" }"
REST_RESPONSE=`curl --silent\
                    -Haccept:application/json \
                    -Hcontent-type:application/json \
                    --user ${ALARMFORWARDER_USER}:${ALARMFORWARDER_PASSWORD} \
                    -X POST \
                    --data "${JSON_DATA}" \
                    ${ALARMFORWARDER_URL}/targets/${ALARMFORWARDER_TARGET}/test`


# change phone number
JSON_DATA="{\"target_parms\": \
                {\"${ALARMFORWARDER_TARGET_PARM}\": \"${PHONE_NEW}\"}}"
REST_RESPONSE=`curl --silent\
                    -Haccept:application/json \
                    -Hcontent-type:application/json \
                    --user ${ALARMFORWARDER_USER}:${ALARMFORWARDER_PASSWORD} \
                    -X POST \
                    --data "${JSON_DATA}" \
                    ${ALARMFORWARDER_URL}/targets/${ALARMFORWARDER_TARGET}/edit`


# send message to new agent
MSG_TO_NEW_AGENT="${MSG_TO_NEW_AGENT} ${PHONE_OLD}"
JSON_DATA="{\"message\": \"${MSG_TO_NEW_AGENT}\" }"
REST_RESPONSE=`curl --silent\
                    -Haccept:application/json \
                    -Hcontent-type:application/json \
                    --user ${ALARMFORWARDER_USER}:${ALARMFORWARDER_PASSWORD} \
                    -X POST \
                    --data "${JSON_DATA}" \
                    ${ALARMFORWARDER_URL}/targets/${ALARMFORWARDER_TARGET}/test`

echo "Changed phone number: ${PHONE_OLD} -> ${PHONE_NEW}"
