git pull &&
git add . &&
git commit -m "$1" &&
git push origin master &&
git push origin master:deploy
