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
    echo "Setting up repository!"
    mkdir $2; cd $2
    git init
    create_day_dirs
    create_readme $1
    git add .; git commit -m "Init commit"
    git remote add origin $3
    git push --set-upstream origin master
    echo "All done!"
}

create_repository $PERSON_LIST
