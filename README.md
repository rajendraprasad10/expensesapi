![expences-api](https://user-images.githubusercontent.com/42211472/132987120-4a35f7ab-2d2e-4e53-816c-422d79765397.jpg)
![income-api](https://user-images.githubusercontent.com/42211472/132987139-ab528883-ca6f-499c-bdbd-1cfdee63cc45.jpg)
![expences-api](https://user-images.githubusercontent.com/42211472/132987149-afb617e7-37aa-4a3c-b83c-e484ded77db9.jpg)
![expences-api](https://user-images.githubusercontent.com/42211472/132987160-a1ba6aed-60fa-422e-98ed-f8eb52e6c747.jpg)
![expences-api-2](https://user-images.githubusercontent.com/42211472/132987162-e8af8426-0d40-4499-b439-e2a1a5040baa.jpg)
![income-api](https://user-images.githubusercontent.com/42211472/132987163-9e0a9228-d521-4230-9fc6-46dc37fb23db.jpg)
# expensesapi

### production link here.
https://rajexpensesapi.herokuapp.com/
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
