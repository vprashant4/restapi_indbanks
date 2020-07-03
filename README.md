<html>
  <body>
     <p>Django rest framework: This project is about getting details of Indian Banks</p>
     <p><b>To get branch details through IFSC code</b></p>
     <p><i>api/branches/{ifsc_code}</i></p>
     <p><b>To gets details of all branches of the bank in the city</b></p>
     <p><i>api/branches/?branch={branch_name}&ifsc={ifsc_code}&city={city_name_in_upper_case}</i></p>
     <p><i>Note: All fields are not mandatory, 'branch, ifsc and city'</i></p>
     <p><b>To use limit and offset</b></p>
     <p>api/branches/?branch={branch_name}&limit=100&offset=500</p>
     <p>Create virtual environment</p>
  <p>https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#</p>
  <p>pip install -r requirements.txt</p>
   <b><i>Documentation: Nested serializers representations</i></b>
  <p>https://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations</p>
  <p><i>Datebase:</i></p>
   <p>https://github.com/snarayanank2/indian_banks</p>
  <p>***NOTE***</p>
  <p>The queries are case sensitive, which you have to pass it upper case letters.</p>
  </body>
 </html>
