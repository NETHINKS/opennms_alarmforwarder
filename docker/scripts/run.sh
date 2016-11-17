#!/bin/bash

# init environment variables
if [ -z ${INIT_DB_SERVER+x} ]; then INIT_DB_SERVER="postgres"; fi
if [ -z ${INIT_DB_NAME+x} ]; then INIT_DB_NAME="alarmforwarder"; fi
if [ -z ${INIT_DB_USER+x} ]; then INIT_DB_USER="postgres"; fi
if [ -z ${INIT_DB_PW+x} ]; then INIT_DB_PW="postgres"; fi
if [ -z ${INIT_ADMIN_PW_NEW+x} ]; then INIT_ADMIN_PW_NEW="admin"; fi
if [ -z ${INIT_ONMS_URL+x} ]; then INIT_ONMS_URL="http://opennms:8980/opennms/rest"; fi
if [ -z ${INIT_ONMS_USER+x} ]; then INIT_ONMS_USER="admin"; fi
if [ -z ${INIT_ONMS_PW+x} ]; then INIT_ONMS_PW="admin"; fi

# define other variables
ALARMFORWARDER_INITFLAG=/opt/initflag
ALARMFORWARDER_DIR=/opt/opennms_alarmforwarder

# waiting for PostgreSQL startup
sleep 10

# init AlarmForwarder and PostgreSQL on first start
if [ ! -e ${ALARMFORWARDER_INITFLAG} ]
then
    # create database
    echo "CREATE DATABASE ${INIT_DB_NAME}" | PGPASSWORD=${INIT_DB_PW} psql -h ${INIT_DB_SERVER} -U ${INIT_DB_USER}

    # update configuration with database URL
    sed -i 's#postgresql://.*#postgresql://'"$INIT_DB_USER"':'"$INIT_DB_PW"'@'"$INIT_DB_SERVER"'/'"$INIT_DB_NAME"'#g' \
                ${ALARMFORWARDER_DIR}/etc/alarmforwarder.conf

    # install database schema
    ${ALARMFORWARDER_DIR}/install.py

    # add init flag
    touch ${ALARMFORWARDER_INITFLAG}
fi

# start AlarmForwarder
${ALARMFORWARDER_DIR}/opennms_alarmforwarder.py
