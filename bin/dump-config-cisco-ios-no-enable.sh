#!/bin/bash

USER=$1
HOST=$2
PASSWORD=$3

expect -c "
set timeout 5
spawn ssh -o \"StrictHostKeyChecking no\" ${USER}@${HOST}

expect -nocase \"password:\"
send \"${PASSWORD}\n\"

expect \"#$\"
send \"terminal length 0\n\"

expect \"#$\"
send \"show run\n\"

expect \"end\r\n\"
expect \"#$\"
exit
" | grep -A -1 "Current" | grep -B -1 "^end\r$"
