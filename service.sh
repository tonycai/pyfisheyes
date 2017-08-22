#!/bin/sh -e
PASTER="/home/tonycai/workspace/pylons/myenv/bin/paster"
WEBDIR="/home/tonycai/workspace/pyfisheyes"
project_name="pyfisheyes"
#EXEC="$PASTER serve --daemon --pid-file=${WEBDIR}/${project_name}.pid --log-file=${WEBDIR}/${project_name}.log development.ini "
EXEC="$PASTER serve --reload development.ini "
 
case "$1" in
  start)
    $EXEC start
    ;;
  stop)
    $EXEC stop
    ;;
  restart)
    $EXEC restart
    ;;
  force-reload)
    $EXEC restart
    ;;
  *)
    echo $"Usage: $0 {start|stop|restart|force-reload}"
    exit 1
esac
 
exit 0
