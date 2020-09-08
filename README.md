
[![build](https://travis-ci.org/ikatyang/emoji-cheat-sheet.svg?branch=master)](https://travis-ci.org/ikatyang/emoji-cheat-sheet)  [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) 

# **Edu-News**
- A web app for all the News and Notifications from all the institution of India to stay updated about all the upcoming events from any collges and Universities at one place.
<img align="center" src="https://github.com/ManishShah120/news-scrap/blob/master/Demo/ProjectDemo.gif" width="90%"/>

## How to run
1. `mkdir Edu-News`
2. `cd Edu-News`
3. `virtualenv -p python3 env` 
4. `source env/bin/activate`
5. `git clone https://github.com/ManishShah120/news-scrap.git`
6. `cd news-scrap`
7. `pip install r requirements.txt`
8. `python manage.py runserver`
9. Go to your browser and enter this URL `127.0.0.0:8000`

## HOW IT WORKS
- Ther are lot of small chunks of scraping scripts at the backend which refreshes itself whenever the website is refreshed, also while refreshing if the BOT[small scraping scripts] founds any new news or notification on the traget URL then it loads that information in the database.
 
## Built With
1. Python 3.8
2. Linux
3. Django
4. Leaflet.js
5. Html, css
6. SQLite

## Contributing
> **Contribution are wellcomed.**

## Authors
[**Manish Kumar Shah**](https://github.com/ManishShah120)

# License [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[**MIT**](https://github.com/ManishShah120/news-scrap/blob/master/LICENSE)

# Project Status/TODO
1. Add all the indian as well as international Institution on the Map[Marker Icon] with a pop up message and a hyperlink to register themselves.
2. Add an option for registration of any events posted on this site and store the data in the database.
3. Add more scraping scripts for all the institutions.
4. Add the backend of the footer scetion for mailing list to work.
5. For the Post Event[Feature] in future make a field to collect the geo-coordinates of the venue where the institution is or where the event will take place and display that on the portal so that anybody can follow the route on MAP and visit the location without any worries.
6. Add a section for the registered user so that they can see the news or events they have posted and allows them to edit or delete from front END.
7. Solve the issue with the  Mailing List feature present in the footer section.
8. Finally Containerise the entire project and push it to `Docker Hub`.