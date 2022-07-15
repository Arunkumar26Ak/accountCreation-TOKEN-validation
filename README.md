# accountCreation-With-TOKEN-validation

#########################################
  
  Name : Arunkumar A
  
  Email : arunanbu.ani97@gmail.com
    
  Date : July/15/2022

#########################################


# Software requirement

Back-end :Python - Django (DRF)

Database : MySql

mySql dump file name : commercial_database.sql


# Environment setup
Install :

python3 -m venv ecartEnv

pip3 install -r requirements.txt

Run : python3 manage.py migrate

python3 manage.py makemigrations

python3 manage.py runserver


# Sample Api Request and response

# createAccount request :
url : http://localhost:8000/createAccount

request : 

{
  "method": "createUser",
  "request": {
    "user_name": "arunkumar",
    "password": "password123",
    "email_id": "arunanbu.ani97@gmail.com"
  }
}

Response : 

{
    "Response_status": true,
    "Response_data": {
        "status": "User Created successfully"
    }
}

#########################################

# Signin to create Token:
URL : http://localhost:8000/signin

Request :
{
  "method": "signin",
  "request": {
    "username": "arunkumar",
    "password": "password123"
  }
}


Response : 
{
    "user": {
        "id": 1,
        "username": "sathi",
        "email": "admin"
    },
    "expires_in": "3599999.995568",
    "token": "2eb914929744cf7ce501226049c4cb7bb69e25c3"
}

#########################################

# Sample CURD oprations moduele with token validation 

Sample token headers : 

Content-Type:application/json

Authorization:Token 2eb914929744cf7ce501226049c4cb7bb69e25c3 



URL : http://localhost:8000/product 


Add product to cart sample request and response:

Request : 
{
  "method": "addProduct",
  "request": {
    "category": "1",
    "customer_id": "1",
    "product_name": "iphone"
  }
}

Response :
{
    "Response_status": true,
    "Response_data": {
        "product_id": 10,
        "status": "Product added to Cart"
    }
}

