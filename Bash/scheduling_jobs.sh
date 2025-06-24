#!/bin/zsh

# AT #
# "at" -- used to run script at a later time. Use "which at" to confirm if its installed
# "at 17:29 -f ./scheduling_jobs.sh"  --- to run this script at given time automatically
# "atq" -- at commands in queue
# "atrm 3" -- remove job at queue no. 3

logfile=job_results.log
echo "The script ran at following time: $(date)" > $logfile

# CRON JOBS #
# crontab -e (open a cronjob file in /tmp folder)
# 30 1 * * 5 /usr/local/bin/script -- run this script every Friday(5) 1 30 in morning. (Sat-6, Sun-0...)
# min hr dom mon dow command
# 0 5 * * 1 tar -zcf /var/log/log.log /home

#sudo crontab -u bob -e   --- to giver permission of your cronjob to another user