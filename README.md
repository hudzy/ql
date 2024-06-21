```bash
ql repo https://github.com/hudzy/ql.git "task_"
```

```bash
# Setup notification token for specified task
case $1 in
    *task_validateCookie* )
		export PUSH_PLUS_TOKEN="123321123321"
        ;;
    *)
		export PUSH_PLUS_TOKEN=""
        ;;
esac
```
