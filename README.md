<html>
  <body>
   <p><h1>How to use this app?</h1></p>
  
  <p><b>Heroku: This API Website is down due to the AWS RDS free trial has stopped this month.</b></p>
  
  <p><b>Create virtual environment</b></p>
  <p>https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#</p>
  
  <p>pip install -r requirements.txt</p>
  
  <p><b>Datebase</b></p>
   <p>https://github.com/snarayanank2/indian_banks</p>
   
   <p>In this project, I used AWS RDS PostgreSQL to store data</p>
   <p>https://aws.amazon.com/rds/postgresql/</p>
  
  <p><b>Given a bank branch IFSC code, get branch details</b></p>
  <p><i>api/bankbranches/?ifsc= for example: ifsc=SBIN0000583</i></p>
  
  <p><b>Given a bank name and city, gets details of all branches of the bank in the city</b></p>
  <p><i>/api/bankbranches/?city=&bank_name= for example: city=DELHI&bank_name=STATE</i></p>
  
  <p>bank_name is lookup_expr='icontains' as SQL equivalent ILIKE keyword</p>
  <p>https://docs.djangoproject.com/en/3.0/ref/models/querysets/#std:fieldlookup-icontains</p>
  
  <p><b>APIs: Support limit and offset parameters</b></p>
  <p><i>api/bankbranches/?bank_name=&limit=&offset= for example: bank_name=STATE&limit=10&offset=10</i></p>
  
  <p><b>Get data in JSON format</b></p>
  <p><i>api/bankbranches/?format=json</i> Or <i>api/bankbranches/?city=DELHI&format=json</i></p>
  
  <p><b>Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework authentication and need to access these URLs</b></p
  <p>"bank": "https://restapibanks.herokuapp.com/api/bank/"</p>
  <p>"branches": "https://restapibanks.herokuapp.com/api/branches/"</p>
  <p>How to curl the Simple JWT, 'an access token will have a validity of 5 days and a refresh token will have a validity of 6 days'</p>
  <p>Document: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#usage</p> 
  
   <p><b>Simple JWT authentication is not required to getting details of banks and through search parameters, city, bank name and ifsc code.</b></p>
   <p>"bankbranches": "https://restapibanks.herokuapp.com/api/bankbranches/"</p>  
  
   <p><b>Nested serializers representations</b></p>
  <p>https://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations</p
   
  <p><b>***NOTE***</b></p>
  <p>The queries are case sensitive, which those parameters must be an uppercase letter.</p>
  <p>All fields are not mandatory, bank name, ifsc and city</p>
  </body>
 </html>
