#!/bin/bash

msg="$1"

git add .

if git diff --cached --quiet; then
    echo "No changes to commit."
else
    git commit -m "$msg"
    git push origin main
fi