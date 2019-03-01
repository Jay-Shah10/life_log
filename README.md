# life_log

## Overview
This Django project is created to learn django. 
* life_log - contains all django files. 
* life_logs - is the app. 
* life_logs/templates/life_logs - contains all html templates. 
* manage.py - Allows you to control django functions. 
* ll_env - virtual env for this project. 


### Requirements
```
Python 3.7
Django 2.1
virtualenv
```
Download virutalenv after installing python.   
```
pip install virtualenv
```


### How to
You can clone this repository.
```
git clone
```
or you can remote add this repos in your local dir.

```
git remote add origin <url>
```

Once you have this pulled to you local machine. you will need to activate the virutal env that is included with this.   
ll_env is the virtual env for this app. Use the following command.  
```
ll_env\Scripts\activate   
```
or the following for linux. 

```
source ll_env/bin/activate
```
Once the environment is running navigate into the life_log and find "manage.py" file. Turn on the Django server using the following command. 
```
python manage.py runserver.  
```


