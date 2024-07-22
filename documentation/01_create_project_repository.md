# Create a Repository and set up version control

## Create remote repository

1. GitHu.com, and create new repository
2. Name: pdi_weather_dashboard
    * Note: ask Russell, naming convention for GitHub Repo vs Python Project. I.e. `pdi_weather_dashboard` or `pdi-weather-dashboard`?
3. Create with Readme.md file
4. Create with `python .gitignore template`
5. Copy ssh key. `git@github.com:kenny-chua/pdi_weater_dashboard.git`

## Clone Remote Repository to Local Computer

1. Terminal
2. Clone:
  
    ``` sh title="Clone remote repository"
    git clone git@github.com:kenny-chua/pdi_weather_dashboard.git
    ```

    ``` sh title="Output"
    Cloning into 'pdi_weather_dashboard'...
    remote: Enumerating objects: 4, done.
    remote: Counting objects: 100% (4/4), done.
    remote: Compressing objects: 100% (4/4), done.
    remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
    Receiving objects: 100% (4/4), done.
    ```

3. Verify:

    ``` sh title="Verify clone"
    cd pdi_weather_dashboard
    ls -a
    git remote -v
    git status
    ```
