# OpenNMS AlarmForwarder

OpenNMS AlarmForwarder is a small tool written in Python for doing notifications on OpenNMS alarms. In a configurable interval, alarms were read from one or multiple OpenNMS servers (using the OpenNMS REST API) and saved in a local database. You can define multiple targets for notifications (e.g. mail, SMS, OTRS ticket) and forwarding rules. The forwarding of alarms can be delayed and suppressed, if the alarm is resolved within this interval. A daemon handles the alarm forwarding and most of the configuration is done in a small WebUI (with REST API).

## Usage

### Start a Docker Container
There is a Docker Image for AlarmForwarder on Docker Hub. It will need a PostgreSQL database. You can use the following docker-compse.yml file:

```
version: "2"
services:
  alarmforwarder:
    image: nethinks/alarmforwarder
    build: ./
    ports:
      - "5000:5000"
    depends_on:
      - dbserver
    environment:
      INIT_DB_SERVER: "dbserver"
      INIT_DB_NAME: "alarmforwarder"
      INIT_DB_USER: "postgres"
      INIT_DB_PW: "secret1234"

  dbserver:
    image: postgres
    environment:
      POSTGRES_USER: "postgres"
      POSTGRES_PASSWORD: "secret1234"
```


### Manually setup your environment
AlarmForwarder is written in Python3. The following libraries are required:

* requests
* ldap3
* gunicorn
* flask
* sqlalchemy
* psycopg2

The data were stored in a PostgreSQL database. Please create an empty database and fill in the connection parameters in etc/alarmforwarder.conf. To install the database schema, please execute the install.py script:
```
./install.py
```

Now you can start AlarmForwarder by executing opennms_alarmforwarder.py:

```
./opennms_alarmforwarder.py
```

You can now log into the WebUI by accessing the URL http://<Host>:5000 with username admin and password admin.

You can also find examples for a systemd service definition and a SystemV init script for Debian/Ubuntu in the contrib directory.




## Documentation
The documentation is provided with the tool and can also seen on [GitHub](https://github.com/NETHINKS/opennms_alarmforwarder/blob/master/docs/src/documentation.adoc)



## Support
If you have questions, found a bug or have an idea to enhance AlarmForwarder, please open an issue at the https://github.com/NETHINKS/opennms_alarmforwarder[GitHub project].
