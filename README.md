This CTF challenge is aimed at beginners.

There are 5 flags hidden throughout this web app.

- The first flag is obvious .
- The second flag is revealed when you do some specific thigs .
- The third flag is the password of one of the users .
- The fourth flag is in a page in one of the hidden urls.
- The fifth flag is in one of the images

Note
====

If you are looking for the solution of this ctf check `WRITEUP.md` file !

How to run
==========

as any django web app you need first to download python , than django , than venv to create a virtual env folder in your pc
then you are going to put this folder in your venv folder and activate it , once activated (the venv) , you have to add the static files by typing the command:
```
python manage.py collectstatic
```
then you have refresh the database using the command:
```
python manage.py makemigrations
```
and
```
python manage.py migrate
```
and finally you can run the server using the command:
```
python manage.py runserver
```

WARNING
=======

this CTF challenge was created for educational purposes no more , you don't want to host it anywhere! (only if it's for a legal competition )


CHECK IT IF YOU WANT 
====================


URL : https://phoenixesgee.pythonanywhere.com/
