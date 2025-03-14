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
Note: The dafault server for running the django file is - 8000<br>
In case of demo application: Project - learning and App - chai
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
Note: make sure to add the app name in the settings file of project as without itm nothing would work <br>

<h2>Adding Tailwind to project</h2><br>
1. use cmd - pip install django-tailwind , inside the venv <br>
2. also install the reload feature - pip install 'django-tailwin[reload]' <br>
3. add 'tailwind' in settings file <br>
4. now initialize tailwind - python manage.py tailwind init <br>
5. give app name in prompt <br>
6. Also add two configs in the settings.py - TAILWIND_APP_NAME & INTERNAL_IPS<br>
7. install tailwind - python manage.py tailwind install <br>
<b>Tips before installing the tailwind</b> <br>
In settings.py file make sure to add the NPM_BIN_PATH (can get it from cmd prompt - npm where)<br>
Also add the path containing "cmd" eg. r"PATH\TO\NPM" , including r to resolve black-slash issues.<br>

<h2>Starting tailwind</h2><br>
1. Add the required css code in the file(index.html)<br>
2. start tailwind in venv - python manage.py tailwind start <br>
3. in another terminal inside venv run the project - python manage.py runserver <br>
4. for production we can use it in one terminal with cmd - python manage.py tailwind build <br><br>
<h2>Admin Panel</h2><br>
Firstly, run cmd python manage.py migrate to get the admin authentication and remove the migrate errors <br>
Also by default we have settings for admin <br>
For creating superuser for admin : <br> 
a. run cmd - python manage.py createsuperuser <br>
b. make sure you have run the 'migrate' command <br>
c. add the necessary details (username , pswd , etc) <br>
d. run the project and '/admin' , add details and you will get the superuser access <br>

<h2>Adding Images to project</h2><br>
1. add settings in model.py file <br>
2. install pillow - pip install Pillow<br>
3. add configurations in settings.py > urls.py<br>
4. make migrations for app - python manage.py makemigrations learning <br>
5. migrate - python manage.py migrate <br>
6. in admin.py import the model and use it as a superuser <br>


<h3>Future Add-on</h3><br>
Add the hot reload feature in this to see the frontend changes reflecting quickly to the project.<br>
