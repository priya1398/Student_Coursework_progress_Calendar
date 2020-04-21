# Student Coursework Progress Calendar


1.	Download python 3.7.7 web-based installer from the link https://www.python.org/downloads/release/python-377/. 
In the command prompt->
2.	python -m pip install virtualenvwrapper-win
3.	pip install Django==2.0.0
4.	pip install virtualenvwrapper-win
5.	pip install mysqlclient
6.	pip install PyMySQL==0.9.3
7.	pip install pytz==2019.2
8.	pip install six==1.12.0
MySQL server 5.5 and  Django 2.0 works together.
MySQL->
9.	import the sql file into your MYSQL database

10.	In event_calendar/settings.py -> Databases section-> change ->
Username to root (<your mysql username>),
 password to root (<your mysql passowrd>) 
database_name : student_coursework_progress_calendar.
 
11.	Running the application
In command prompt->
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
