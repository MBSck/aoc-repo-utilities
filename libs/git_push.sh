#!/usr/bin/env bash

function push() {
    cd $1
    git init
    git add .; git commit -m "Init commit"
    git remote add origin $2
    git push --set-upstream origin master
}

push $1 $2
