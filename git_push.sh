#!/usr/bin/env bash

function push() {
    echo "Commiting and pushing..."
    cd $1
    git add .; git commit -m "Init commit"
    git remote add origin $2
    git push --set-upstream origin master
    echo "All done!"
}

push $1 $2
