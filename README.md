```bash
ql repo https://github.com/hudzy/ql.git "task_"
```

```bash
# Setup notification token for specified task
case $1 in
    *task_validateCookie* )
		export PUSH_KEY="1"
        ;;
    *)
		export PUSH_KEY=""
        ;;
esac
```
