![site logo](https://res.cloudinary.com/duo4xxmj8/image/upload/v1600950745/MasterPlan/MasterPlanLogo_dveiou.png)

## MasterPlan

`What:` `MasterPlan` is a focused project management solution for Project and Production Managers in the corporate entertainment industry.

`Why:` As someone who has filled this position many times, I always found it daunting to use other Project Management systems because the templates were always very generic. This required me to create the same fields for every project I worked on, allowing for human error, and forgetting essential data. 

`How:` Through referencing past events and my planning method, I compiled a list of particular fields that applied to every project. Using that list, I created a very industry specific solution for covering and gathering data for all critical aspects for planning a successful event. This ultimately helps save an immense amount of time and money as any missed details can cause significant delays while executing the event.

## Steps to get your project started:

* Clone down the repo and `cd` into it

* Create your OSX/Linux OS virtual environment in Terminal:

  * `python -m venv masterplanenv`
  * `source ./masterplanenv/bin/activate`

* Install the app's dependencies:

  * `pip install -r requirements.txt`

* Build your database from the existing models:

  * `python manage.py makemigrations masterplanapp`
  * `python manage.py migrate`

* Create a superuser for your local version of the app:

  * `python manage.py createsuperuser`

* Populate your database with initial data from fixtures files: (_NOTE: The order you add these fixtures is important_)

  * `python manage.py loaddata clients`
  * `python manage.py loaddata houseAV`
  * `python manage.py loaddata union`
  * `python manage.py loaddata venue`
  * `python manage.py loaddata projects`

* Start your dev server!

  * `python manage.py runserver`

