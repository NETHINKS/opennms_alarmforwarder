#!/bin/sh

### BEGIN INIT INFO
# Provides:          alarmforwarder
# Required-Start:    $network $local_fs $remote_fs
# Required-Stop:     $network $local_fd $remote_fs
# X-Start-Before: 
# X-Stop-After: 
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# X-Interactive:     false
# Short-Description: alarmRetarder init script
# Description:       This is the init script for alarmRetarder
### END INIT INFO

. /lib/lsb/init-functions

DAEMON_NAME=alarmforwarder
DAEMON=/opt/opennms_alarmforwarder/opennms_alarmforwarder.py
PIDFILE=/var/run/alarmforwarder.pid

case "${1}" in
    start)
        log_daemon_msg "Starting ${DAEMON_NAME}" "${DAEMON_NAME}"
        start-stop-daemon --start --quiet --exec ${DAEMON} --background --make-pidfile --pidfile ${PIDFILE} > /dev/null || exit 1
        log_end_msg 0
        ;;

    stop)
        log_daemon_msg "Stopping ${DAEMON_NAME}" "${DAEMON_NAME}"
        start-stop-daemon --stop --quiet --retry=TERM/30/KILL/5 --pidfile ${PIDFILE}
        RETURN="${?}"
        [ "${RETURN}" = 2 ] && exit 2
        log_end_msg 0
        ;;

    force-reload|restart)
        ${0} stop
        ${0} start
        ;;

    status)
        status_of_proc ${DAEMON} && exit 0 || exit $?
        ;;

    *)
        log_success_msg "Usage: ${0} {start|stop|restart|force-reload|status}"
        exit 1
        ;;
esac
