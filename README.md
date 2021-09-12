# expensesapi

This is sample project for including swagger doc as API testing, it has integrated with django and python and swagger functionality.  
and it was deployed in heroku cloud as pipe line build, and integrated with docker as well.

### starting this app
1. clone from here git clone
2. pip install -r requirements.txt
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py runserver

open app 

localhost:8000

u must mention this in .env file in project root folder
SECRET_KEY= django-insecure-ma!)b5heg#y$vvq3%1&o0vo543hc&k+a#fb-5rvterekno&fje
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=



now u can see the swagger doc for apis testing.

here you have to check gmail config's, gmail 

after configeration is done 

create the user using register endpoint  
erifiy the email and login u will get a jwt token 

authenticate with that token as given in swagger doc autherize type Bearer and token.

now can able to access the all endpoint's 
