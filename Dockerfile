FROM ubuntu:latest
MAINTAINER Michael Batz <michael.batz@nethinks.com>

# copy repository to /opt
COPY ./ /opt/opennms_alarmforwarder

# install required software
RUN apt-get update -y \
    && apt-get install -y python3 python3-requests python3-flask python3-ldap3 \
                          python3-psycopg2 python3-sqlalchemy python3-gunicorn \
                          postgresql-client \
    && chmod +x /opt/opennms_alarmforwarder/docker/scripts/run.sh 

# start alarmforwarder
CMD /opt/opennms_alarmforwarder/docker/scripts/run.sh
