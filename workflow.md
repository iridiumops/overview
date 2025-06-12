# First time setup
1) Install [Git](https://git-scm.com/) and clone the repository `git clone https://github.com/iridiumops/overview.git`
2) Install [Anaconda or Miniconda](https://www.anaconda.com/download/success). Create Python environment and setup dependencies via `requirements/create.bat` script

# Workflow
1) Get latest data:
   1) Run `git fetch origin main` inside the repository. Git will fetch new changes from the Github repository for main branch if there are any.
   2) Get latest SDE data via `data/download.bat`. Curl will download latest SDE export files that we need in `csv` format from Fuzzwork into the `data` directory.
2) Find new type IDs:
   1) Run `git diff origin/main data/invGroups.csv` to view new inventory group type IDs by comparing newly download SDE data with data fetched from main branch on the Github repository.
   2) Check ingame overview settings for any other newly added inventory group types that aren't yet in the Fuzzwork SDE export. Get their IDs by searching their names on [EVE Ref](https://everef.net/). 
   3) Alternatively open ingame overview settings, view the `All: All` filter and tick all types. On `Misc` tab click `Export Settings`, select only the `All: All` filter and export it to a file under any name you wish. On Windows it will be located in `%USERPROFILE%\Documents\EVE\Overview\`. You can compare the new file with `parts\filter All All.yaml` to find new IDs.
3) Update the overview filters:
   1) Modify or update YAML files in `parts` directory to your liking with the new IDs.
   2) Optionally update the Python build script `src/build.py` if other changes are needed.
4) Generate YAML files:
   1) Run `build.bat` to build YAML files from parts. It will call `src/build.py` and generate new YAML files in the `output` directory, ready to be imported ingame.
   2) Import generated YAML files into EVE Online.
      1) Copy the newly generated YAML files from `output` directory to `%USERPROFILE%\Documents\EVE\Overview\` 
      2) Open ingame overview settings, on the `Misc` tab click `Reset All Settings` then click `Import Settings`, select desired file from the list, tick `Check All` and click `Import` to load it.
      3) Check that the overview changes are correct. Repeat step above with other variants of the overview.
5) Release new version:
   1) Decide on version number (use semantic versioning).
   2) Update `changelog.md`, describe your changes.
   3) Release it ingame:
      Note: if you are not approved channel operator you won't be able to update the MOTD.
      1) Obtain new shareable links for all variants of the overview:
         1) Open ingame overview settings. On `Misc` tab click `Import Settings`, select the main YAML file on the left, tick `Check All` and click `Import`. Without clicking on anything else in the settings, close the overview settings window and open it again to avoid a bug where some settings do not load right.
         2) On `Misc` tab click `Export Settings`, select `General Overview Settings` and `Overview Profile` and up to 16 filters.
            1) For part 1 select filters used by the tabs by default (should be already selected).
            2) For part 2 select `Ships: Enemy...` filters.
            3) Fort part 3 select remaining filters that you didn't select in part 1 or 2.
            4) For version with Tab Icons repeat import but select icon YAML file instead, repeat selecting filters just like for part 1.
            5) For Carbon Mode version repeat import but select carbon YAML file instead, repeat selecting filters just like for part 1.
         3) Click the text left of the `Share` button at the top to rename the shareable link.
         4) Drag the `Share` button to ingame notepad to create shareable link. 
         5) Repeat previous steps for all variants.
         6) Select the links in the ingame notepad, right click and use `Copy Selected With Formatting`. Paste the links in a text editor to see the actual link URI for each link, it will look like `overviewPreset:e68.....675//1`.
      2) Open `motd/motd.html` in a text editor. Update information and replace old links with new ones from the step above. Make sure it it less than 4000 bytes so it fits in the ingame MOTD. Note: html formatting used by the game is simplified and non-standard.
      3) Open ingame chat channel configuration - right click on the channel tab, select `Configuration`. Copy the HTML and paste it in MOTD field. Test that all links work and point to the new version. Click `OK` to publish.
   4) Release on Github:
      Note: if you are not approved contributor, you should instead push to your own fork and then submit pull request as you will not have necessary privileges to push to main branch.
      1) Copy YAML files from `output` directory to `releases` directory and rename them based on the version.
      2) Run `git status` to see all changes
      3) Run `git add .` to add tracking for new and changed files and stage them for commit.
      4) Run `git commit -m "MESSAGE"` where message is short description of what changed.
      5) Run `git tag v1.0.0`  where 1.0.0 is the new version number to apply the tag to the last commit.
      6) Run `git rebase`  in case there are diverging changes between your local repository and Github repository. This will merge changes from last commit on the end of main branch.
      7) Run `git push origin main --dry-run` to to confirm that there are no conflicts.
      8) Run `git push origin main `  to update Github repository.
      9) Run `git push origin --tags` to update tags in the Github repository.
      10) On Github create a new release. Select the added tag. Write release description or copy information from changelog, select individual YAML files from for the release or upload a zip containing them all. Set the release as latest.
   5) Notify `Thomas Iridium` to update overview page on the iridiumops website and discord.

