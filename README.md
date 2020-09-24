![site logo](https://res.cloudinary.com/duo4xxmj8/image/upload/v1600950745/MasterPlan/MasterPlanLogo_dveiou.png)

## MasterPlan

MasterPlan is a hyper focused project management solution for Project and Production Managers in the corporate entertainment industry.

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

