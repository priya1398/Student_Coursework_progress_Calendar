


1.	Download python 3.7.7 web-based installer from https://www.python.org/downloads/release/python-377/. 
In the Command Prompt->
2.	python -m pip install virtualenvwrapper-win
3.	pip install Django==2.0.0
4.	pip install virtualenvwrapper-win
5.	Install MySQL Database Connector -> pip install mysqlclient
6.	pip install PyMySQL==0.9.3
7.	pip install pytz==2019.2
8.	pip install six==1.12.0

9.	Create the Database in MySQL 5.5 command line client 
CREATE DATABASE scpc;
      SHOW DATABASES;
Ensure the scpc database is among the databases.
 
USE scpc;

10.	Edit the MySQL Database Connection to your Application Django_CRUD/settings.py:
Set Username to root (<your mysql username>), password to root (<your mysql passowrd>) and database_name to scpc.
 


11.	Testing the application
In Command Prompt->
•	Navigate to the directory
cd Desktop\Student_Coursework_progress_Calendar-master\SCP_Calendar_APP
•	python manage.py makemigrations
•	python manage.py migrate
•	Insert table values in MySQL 5.5 command line client 



show tables;
insert into crud_teacher_courses values(1, 'Computer Science','4', 'F20BD','Big Data Management');
insert into crud_teacher_courses values(2, 'Computer Science','4', 'F28DM','Data Management System');

•	Back to Command Prompt-> python manage.py createsuperuser
Set:
username: test
email:test@gmail.com
password: test1234567890
•	python manage.py runserver
•	Open application in the browser : http://127.0.0.1:8000/admin
 
•	Log in using username: test and password: test1234567890
•	Add a student 
Click Users-> Add username: student, password: test1234567890
 
Ensure that that staff status is not clicked.
 
•	Open application in the browser: http://127.0.0.1:8000/ . 
 
•	Log in with username: test and password: test1234567890 to get to the Professor’s Interface and log in with username: student and password: test1234567890 to view the Student’s Interface.    

