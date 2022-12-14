# AOC (Advent-of-Code) Repository Creation Utilities
Utilities to automatically create an advent of code repository with some nice Quality
of Life

## Installation
### 1. Clone this repository onto your system
Go to a directory of your choice and then clone this repository with the following command
```
git clone git@github.com:MBSck/aoc-repo-utilities.git
```
After doing this, follow the next steps in order

### 2. Create a Github token
> #### :warning: Treat this token as a password, because it is! Save it encrypted! :warning:
##### Click here for a step by step guide to create a Github-token: [Github token creating guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

When creating a Token, make sure to...

* Choose the option to **Generate new token (classic)**
* For the **scopes** choose:<br>
-- `repo`: Including all drop-down options (should be selected when the parent)<br>
-- `workflow`<br>
-- `delete_repo`<br>

Otherwise the script will not work

### 3. Create SSH-Key to access your repositories
> ##### :warning: This needs to be done to pull from and push to **any** Github-repositories
##### For this follow the steps to [generate an SSH-Key](https://docs.github.com/en/github-ae@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

Sometimes the command
```
ssh-add ~/.ssh/id_github
```
needs to be added to the `~/.bashrc` or `~/.zshrc` to be called with shell start


### 4. Get Info from AOC-Website
Follow the steps in this repository [advent-readme-stars](https://github.com/k2bd/advent-readme-stars)
to procure
* The `userId`: https://github.com/k2bd/advent-readme-stars/#userid
* The `sessionCookie`: https://github.com/k2bd/advent-readme-stars/#sessioncookie
* For `leaderboardId` ask the creator of the private leaderboard

### 5. Execute script
To automatically setup your (remote and local) Github repository for advent of code execute
```
python3 setup.py
```
This will set up a Github repository one folder up from this and will then push it to your
Github

The script will ask you for:

* Your **Github token**
* Your **AOC-ID**
* Your **AOC-Session-ID**
* Your **AOC-Leaderboard-ID**


### 5. Start with AOC. Enjoy!
