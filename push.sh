#!/bin/bash
set -euo pipefail

GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

git checkout --orphan temp-branch
git add -A
git commit -m "update on $(date -u +%Y-%m-%dT%H:%M:%SZ)" --no-verify
git branch -D "$GIT_BRANCH"
git branch -m "$GIT_BRANCH"
git push -f origin "$GIT_BRANCH"
git gc --aggressive --prune=all
