#!/bin/bash

dir_shell=/ql/shell
. $dir_shell/env.sh
. $dir_shell/share.sh

reload_pm2

ql repo https://github.com/6dylan6/jdpro.git              "jd_|jx_|jddj_" "backUp" "^jd[^_]|USER|JD|function|sendNotify|utils"
ql repo https://github.com/RayWangQvQ/BiliBiliToolPro.git "bili_task_"
