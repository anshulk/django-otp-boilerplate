django-otp-boilerplate
---

Djnago boilerplate with -

* OTP login class (just add SMS logic)
* Custom User with phone as primary key
* User picture upload
* Login via password/OTP
* Django REST Framework JSON APIs
* Oauth 2.0 using django-oauth-toolkit

Steps for trying out - 

1. `virtualenv -p python3 env`
2. `. env/bin/activate`
3. `pip install -r requirements.txt`
4. `./manage.py migrate`
5. `./manage.py createsuperuser`
6. `./manage.py runserver`

Navigate to http://127.0.0.1:8000/admin/ and login.