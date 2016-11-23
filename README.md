# OpenNMS AlarmForwarder

OpenNMS AlarmForwarder is a small tool written in Python3 for doing notifications on OpenNMS alarms. In a configurable interval, alarms were read from one or multiple OpenNMS servers (using the OpenNMS REST API) and saved in a local database. You can define multiple targets for notifications (e.g. mail, SMS, OTRS ticket) and forwarding rules. The forwarding of alarms can be delayed and suppressed, if the alarm is resolved within this interval. A daemon handles the alarm forwarding and most of the configuration is done in a small WebUI (with REST API).

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


### Setup for Centos 7

#### Install the required software
At first, Python3 and PostgreSQL must be installed. As Centos 7 does not bring Python 3 by default, you need to install it for example using the IUS Repository:
```
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum install python35u.x86_64 python35u-pip.noarch python35u-devel.x86_64 postgresql-server.x86_64 postgresql.x86_64 postgresql-devel.x86_64 gcc
```

Use pip3.5 to install the required libraries:

```
pip3.5 install requests ldap3 gunicorn flask sqlalchemy psycopg2
```

Create a symlink for Python3:
```
ln -s /usr/bin/python3.5 /usr/bin/python3
```

#### Configure PostgreSQL
At first, the PostgreSQL database server must be initialized:

```
postgresql-setup initdb
systemctl enable postgresql
systemctl start postgresql
```

Now you can create a new user (e.g. _alarmforwarder_) and database (e.g. _alarmforwarder_) for PostgreSQL:

```
su postgres
createuser -P alarmforwarder
createdb -O alarmforwarder alarmforwarder
exit
```

In the configuration file _/var/lib/pgsql/data/pg_hba.conf_ the authentication methods were configured. Please change _ident_ to _md5_ here for the sources _127.0.0.1/32_ and _::1/128_

```
# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     peer
# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
# IPv6 local connections:
host    all             all             ::1/128                 md5
```

After the change, you need to reload PostgreSQL:
```
systemctl reload postgresql
```

#### Install AlarmForwarder
Now you can install AlarmForwarder. Please extract the downloaded archive to _/opt/opennms_alarmforwarder_.

Edit the /opt/opennms_alarmforwarder/etc/alarmforwarder.conf file and fill in the parameters of your database connection:

```
[DatabaseConnection]
url = postgresql://alarmforwarder:alarmforwarder@localhost/alarmforwarder

[...]
```

Now you can execute the install script:

```
/opt/opennms_alarmforwarder/install.py
```

Copy the systemd start script from the _contrib_ directory and start AlarmForwarder:

```
cp /opt/opennms_alarmforwarder/contrib/startscripts/systemd/alarmforwarder.service /etc/systemd/system/
systemctl enable alarmforwarder.service
systemctl start alarmforwarder.service
```


### Setup for Ubuntu 16
#### Install the required software
At first all the required software, like _pip_ and the PostgreSQL database server needs to be installed. The required Python libraries can be installed using _pip_:

```
apt install python3-pip postgresql postgresql-server-dev-all
pip3 install requests ldap3 gunicorn flask sqlalchemy psycopg2
```

#### Configure PostgreSQL
Now you can create a new user (e.g. _alarmforwarder_) and database (e.g. _alarmforwarder_) for PostgreSQL:

```
su postgres
createuser -P alarmforwarder
createdb -O alarmforwarder alarmforwarder
exit
```

#### Install AlarmForwarder
Now you can install AlarmForwarder. Please extract the downloaded archive to _/opt/opennms_alarmforwarder_.

Edit the /opt/opennms_alarmforwarder/etc/alarmforwarder.conf file and fill in the parameters of your database connection:

```
[DatabaseConnection]
url = postgresql://alarmforwarder:alarmforwarder@localhost/alarmforwarder

[...]
```

Now you can execute the install script:

```
/opt/opennms_alarmforwarder/install.py
```

Copy the systemd start script from the _contrib_ directory and start AlarmForwarder:

```
cp /opt/opennms_alarmforwarder/contrib/startscripts/systemd/alarmforwarder.service /etc/systemd/system/
systemctl enable alarmforwarder.service
systemctl start alarmforwarder.service
```



## Documentation
The documentation is provided with the tool and can also seen on [GitHub](https://github.com/NETHINKS/opennms_alarmforwarder/blob/master/docs/src/documentation.adoc)



## Support
If you have questions, found a bug or have an idea to enhance AlarmForwarder, please open an issue at the [GitHub project](https://github.com/NETHINKS/opennms_alarmforwarder).
