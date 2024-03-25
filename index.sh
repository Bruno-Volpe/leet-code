#!/bin/bash

# Ask for commit message
echo "Please enter the commit message:"
read commit_message

# Add all changes to staging
git add .

# Commit with message
git add -A
git commit -m "$commit_message"

# Push to origin main
git push origin main