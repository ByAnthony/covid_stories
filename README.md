
# Covid Stories

This project was built for week 4 of the CodeClan Software Developer course.

The objective was to build a full stack web application. 

## Brief

The idea was to produce an app that could be used to support charities during the hard time of Covid by sharing stories and memories, allowing a user to add, edit/update, remove memories/charities/events.

It is based on 

>### Travel Bucket List
>Build an app to track someone's travel adventures.

>MVP:
>The app should allow the user to track countries and cities they want to visit and those they have visited.
>The user should be able to create and edit countries
>Each country should have one or more cities to visit
>The user should be able to create and delete entries for cities
>The app should allow the user to mark destinations as visited or still to see

>Possible Extensions:
>Have separate pages for destinations visited and those still to visit
>Add sights to the destination cities
>Search for destination by continent, city or country
>Any other ideas you might come up with

It was built using Flask, PostgreSQL, psycopg2, Python and HTML/CSS.

## Setup and running

Pre-requisites and usage

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
- Navigate to the site in your browser at http://localhost:5000
