echo "Please enter the commit message:"
read commit_message

git add .

git add -A
git commit -m "$commit_message"

git push origin main