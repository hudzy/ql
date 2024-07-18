#!/bin/bash

dir_shell=/ql/shell
. $dir_shell/env.sh
. $dir_shell/share.sh

fix_config
pm2 l &>/dev/null
patch_version
reload_update
reload_pm2

sed -i 's/^RepoFileExtensions=.*/RepoFileExtensions="js mjs py pyc sh"/' /ql/data/config/config.sh
/ql/shell/update.sh repo https://github.com/hudzy/ql.git                   "task_"
/ql/shell/update.sh repo https://github.com/6dylan6/jdpro.git              "jd_|jx_|jddj_" "backUp" "^jd[^_]|USER|JD|function|sendNotify|utils"
/ql/shell/update.sh repo https://github.com/RayWangQvQ/BiliBiliToolPro.git "bili_task_"
