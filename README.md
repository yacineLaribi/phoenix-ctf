This CTF challenge is aimed at beginners.

There are 3 flags hidden throughout this web app.

- The first flag is hidden on every page
- The second flag is revealed if you create a post with over 10,000 points
- The third flag is the password of one of the users

/_How to run_/

as any django web app you need first to download python , than django , than venv to create a virtual env folder in your pc
then you are going to put this folder inyour venv folder and activate it , once activated (the venv) , you have to add the static files by typing the command:
python manage.py collectstatic
then you have refresh the database using the command:
python manage.py makemigrations
and
python manage.py migrate
and finally you can run the server using the command:
python manage.py runserver

/_WARNING_/

this CTF challenge was created for educational purposes no more , you don't want to host it anywhere!
