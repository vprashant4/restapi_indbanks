<html>
  <body>
   <p><h1>How to use this app?</h1></p>
  
  <p><b>Create virtual environment</b></p>
  <p>https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#</p>
  
  <p>pip install -r requirements.txt</p>
  
  <p><b>Datebase</b></p>
   <p>https://github.com/snarayanank2/indian_banks</p>
  
  <p><b>Given a bank branch IFSC code, get branch details</b></p>
  <p><i>api/bankbranches/?ifsc= for example: ifsc=SBIN0000583</i></p>
  
  <p><b>Given a bank name and city, gets details of all branches of the bank in the city</b></p>
  <p><i>/api/bankbranches/?city=&bank_name= for example: city=DELHI&bank_name=STATE</i></p>
  
  <p>bank_name is lookup_expr='icontains' as SQL equivalent ILIKE keyword</p>
  <p>https://docs.djangoproject.com/en/3.0/ref/models/querysets/#std:fieldlookup-icontains</p>
  
  <p><b>APIs: Support limit and offset parameters</b></p>
  <p>api/branches/?bank_name=&limit=&offset= for example: bank_name=STATE&limit=10&offset=10</p>
  
  <p><b>APIs: Login authentication required for CRUD operations</b></p>
  <p>"bank": "https://restapibanks.herokuapp.com/api/bank/"</p>
  <p>"branches": "https://restapibanks.herokuapp.com/api/branches/"</p>
    
   <p><b>APIs: No need login authentication to getting details through city, bank name and ifsc code</b></p>
   <p>"bankbranches": "https://restapibanks.herokuapp.com/api/bankbranches/"</p>  
  
   <b><i>Documentation: Nested serializers representations</i></b>
  <p>https://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations</p
   
  <p><b>***NOTE***</b></p>
  <p>The queries are case sensitive, which those parameters must be an uppercase letter.</p>
  <p>All fields are not mandatory, bank name, ifsc and city</p>
 
  
  </body>
 </html>
