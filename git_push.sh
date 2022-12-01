#!/usr/bin/env bash

function push() {
    echo "Commiting and pushing..."
    git add .; git commit -m "Init commit"
    git remote add origin $3
    git push --set-upstream origin master
    echo "All done!"
}

push
