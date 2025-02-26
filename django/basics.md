## what we intially did : <br>
1. Install venv - pip install virtualenv <br>
2. Rename venv - virtualenv "venv" <br>
3. open env - env_name\Scripts\Activate<br>
4. Install Django - pip install Django <br>
<br>
<h2>Running the Django project </h2><br>
1. create project - django-admin startproject project-name <br>
2. move to project - cd project-name <br>
3. run the py file - python manage.py runserver <br><br>
Note: The dafault server for running the django file is - 8000
<br><br>
<h2>Creating an app:</h2><br>
1. Main thing - to stay in venv & make sure the directory has manage.py file <br>
2. run cmd - python manage.py startapp app-name <br>
So project gets to know that there is an app in it. Also we use DTL(jinja - refer documentation) <br>

<h2>templates and urls:</h2><br>
1. Inside <b>main project</b> - layout.html : contains the base html code used in other files<br>
2. For project, create index.html file and then pass it in views.py file in project <br>
3. Make sure to add path to views in the urls.py file of Main project <br>
4. so flow goes like : layout.html > index.html > views.py > urls.py <br>
<br>
For <b>App</b> created in the project : <br>
1. we can extend the layout.html file in the chai.html file <br>
2. the html files should be inside the templates folder <br>
3. add view, render the file- 'chai/name.html' <br>
4. now view to be passed in urls <br>
5. In main Project make sure to add path to 'chai.urls' by using include import<br>