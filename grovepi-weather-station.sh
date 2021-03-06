#!/bin/sh
#
# init script for grovepi weather station
# Based on https://blog.lanyonm.org/articles/2015/01/11/raspberry-pi-init-script-python.html
#

### BEGIN INIT INFO
# Provides:          grovepi-weather-station
# Required-Start:    $remote_fs $syslog $network
# Required-Stop:     $remote_fs $syslog $network
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: init script for the grovepi weather station
# Description:       We'll have to fill this out later...
### END INIT INFO

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
NAME=grovepi-weather-station
DAEMON=/home/pi/git/grovepi/weather-station.py
DAEMONARGS="" # API KEY
PIDFILE=/var/run/$NAME.pid
LOGFILE=/var/log/$NAME.log

. /lib/lsb/init-functions

test -f $DAEMON || exit 0

case "$1" in
    start)
        start-stop-daemon --start --background \
            --pidfile $PIDFILE --make-pidfile --startas /bin/bash \
            -- -c "exec stdbuf -oL -eL $DAEMON $DAEMONARGS > $LOGFILE 2>&1"
        log_end_msg $?
        ;;
    stop)
        start-stop-daemon --stop --pidfile $PIDFILE
        log_end_msg $?
        rm -f $PIDFILE
        ;;
    restart)
        $0 stop
        $0 start
        ;;
    status)
        start-stop-daemon --status --pidfile $PIDFILE
        log_end_msg $?
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 2
        ;;
esac

exit 0