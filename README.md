
# Covid Stories

This project was built for week 5 of the CodeClan Software Developer course. The objective was to build a full stack web application. 

![](https://github.com/ByAnthony/covid_stories/blob/main/static/images/Screenshot%202021-10-01%20at%2010.40.01.png?raw=true)

## Contents
* [Brief](#Brief)
* [Technologies](#Technologies)
* [Setup](#Setup)

## Brief

The idea was to produce an app that could be used to support charities by sharing memories of contributors' experience during Covid.

From the contributors side:
- The app should allow the user to create, read, update and delete their profile;
- The user should be able to create, read, update and delete memories;
- Each memory should be associated with a charity;
- Their profile should display the charities supported, the memories published and the events they have booked in.

From the charities side:
- The app should allow the charity to create, read, update and delete their profile;
- The charity should be able to create, read, update and delete events;
- Their profile should display their supporters, the memories published and the contributors booked in in an event.

## Technologies
The project was created with:
- Python 3
- psycog2
- postgreSQL
- HTML/CSS
- Flask

## Setup
Pre-requisites and usage:
- Install Python3 and pip3
- Install postgreSQL
- Install Flask: pip3 install flask
- Install psycopg2: pip3 install psycopg2
- Clone/download the project and navigate to that directory in your terminal client
- Create the database: 
```
createdb covid_stories
```
- Create the database table structure: 
```
psql -d stories -f db/covid_stories.sql
```
- Import the seed console: python3 console.py
- Start Flask: 
```
flask run
```
- Navigate to the site in your browser at http://localhost:5000/
