# IRCBot

### Run the bot
  1) Install dependencies with: sudo python3 -m pip install -r https://raw.githubusercontent.com/ProgVal/Limnoria/master/requirements.txt --upgrade
  2) In your git directory run: python3 ./bin/scripts/supybot-wizard 
  3) Then to run the bot run: screen python3 ./bin/scripts/supybot YourBotName.conf

### Setup repository
#### Workflow through the web-interface.
##### Setup your own repository.
  1) Login to your own github account. 
  2) Navigate to the main repository https://github.com/thevillagecoders/IRCBot
  3) On the top right corner click Fork

##### Change files. Make your own featurebranch and push to main branch
  1) Goto your own repository/
  2) Create a new Branch by clicking the main-branch and entering a new feature-name.
  3) Update files
  4) Commit Changes
  5) Click Contribute
  6) Push the changes.

#### Workflow through commandline

##### Clone your personal github
  1) git clone https://github.com/username/IRCBot.git

##### Setup the new required OAuth
  1) Read "Github CLI" on https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git

##### Create a new branch
  2) git checkout -b your-feature-name
  3) git push origin your-feature-name
  4) git push --set-upstream origin your-feature-name

##### Workflow editing your-feature-name
  1) edit files
  2) git commit files -m "message"
  3) git push

##### When the feature is complete
  1) git checkout main
  2) git merge your-feature-name
  3) git push

