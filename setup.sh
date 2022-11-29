#!/usr/bin/env bash

# Creates the .gitignore and README.md
function create_readme() {
    echo "# $1's advent of code" >> README.md
    cat $ ../aoc-repo-utilities/readme_template.md >> README.md
}

# Creates the advent-of-code day folders in the sub-folder of the individual person
function create_day_dirs() {
    for NUMBER in {1..25}
    do
        if (( $NUMBER < 10 )); then
            DAY_FOLDER='Day-0'$NUMBER
        else
            DAY_FOLDER='Day-'$NUMBER
        fi
        mkdir $DAY_FOLDER
        echo '# Placeholder' >> $DAY_FOLDER/.gitignore
    done
}

# Create a repository one folder up
function create_repository() {
    cd ..
    read -p "Enter your name: " NAME
    read -p "Enter the year: " YEAR
    read -p "Enter the SSH-address of the Github repository": GITHUB_REPO
    FOLDER_NAME="advent-of-code-$YEAR"
    mkdir $FOLDER_NAME; cd $FOLDER_NAME
    git init
    create_day_dirs
    create_readme $NAME
    git add .
    git commit -m "Init commit"
    git remote add origin $GITHUB_REPO
    git push --set-upstream origin master
}

create_repository $PERSON_LIST
