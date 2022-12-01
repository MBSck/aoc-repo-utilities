# AOC (Advent-of-Code) Repository Creation Utilities
Utilities to automatically create an advent of code repository with some nice Quality
of Life

## Installation
### 1. Create a Github token
> #### :warning: Treat this token as a password, because it is! Save it encrypted! :warning:
Click here for a step by step guide to create a Github-token: [Github token creating guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

When creating a Token, make sure to...

* Choose the option to **Generate new token (classic)**
* For the **scopes**, choose `admin::repo_hook` and `delete_repo`, `repo` should be
  automatically selected

### 2. Get Info from AOC-Website
Follow the steps in this repository [advent-readme-stars](https://github.com/k2bd/advent-readme-stars)
to procure
* The `userId`: https://github.com/k2bd/advent-readme-stars/#userid
* The `sessionCookie`: https://github.com/k2bd/advent-readme-stars/#sessioncookie
* For `leaderboardId` ask the creator of the private leaderboard

### 3. Execute script
To automatically setup your (remote and local) Github repository for advent of code execute
```
python3 setup.py
```
This will set up a Github repository one folder up from this and will then push it to your
Github

The script will ask you for:

* Your **Name**
* Your **Github token**
* Your **AOC-ID**
* Your **AOC-Session-ID**
* Your **AOC-Leaderboard-ID**


### 4. Start with AOC. Enjoy!
