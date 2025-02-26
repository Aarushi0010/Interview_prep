## what we intially did : <br>
1. Install venv - pip install virtualenv <br>
2. Rename venv - virtualenv "venv" <br>
3. open env - env_name\Scripts\Activate<br>
4. Install Django - pip install Django <br>
<br>
# Running the Django project <br>
1. create project - django-admin startproject project-name <br>
2. move to project - cd project-name <br>
3. run the py file - python manage.py runserver <br><br>
Note: The dafault server for running the django file is - 8000
<br><br>
Creating an app:<br>
1. Main thing - to stay in venv & make sure the directory has manage.py file <br>
2. run cmd - python manage.py startapp app-name <br>
So project gets to know that there is an app in it. Also we use DTL(jinja - refer documentation) <br>
