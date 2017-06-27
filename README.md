# InspiroBot Slackbot

First of all, I should say that I am not affiliated with the wonderful InspiroBot (http://inspirobot.me/).
But it picks me up when I'm feeling down and I want it to help my whole team. So this slackbot posts inspirational posters to my team's #inspiration channel once an hour. 

Prerequisites:
- Python 2.7
- slackclient module (https://pypi.python.org/pypi/slackclient)
- time module
- request module
- os module

Set up: 
- Create a new slack bot integration (https://api.slack.com/custom-integrations/bot-users)
- Add the new app token to your ~/.bashrc file: `export INSPIRO_API_TOKEN=[insert app token]`

Running:
- I use screen (https://www.gnu.org/software/screen/) to keep this running in the background:  

`screen -d -m -S inspiroBot python2 ~/slackbots/inspiro-slack-bot/run.py`
