This project works with Django 1.11;  Python 3.6;  Postgres and pgAdmin 4.2

Informations about Project Structure : 
the project contains Two apps : accounts & shops
	-accounts is dedicated to login and registrations forms and views.
	-shops is where the whole traitement is done: like shop, preferred shop, remove shop..


1)- On pgAdmin Create database : "shop_db"
2)- After downloading the project, please make sure to run migrations.
	python manage.py makemigrations
	python manage.py migrate
3)- On table shop_model2 insert some random data : 
	shop name and location example : 
		shop_name="Bim" location="(1.42,3)"
		shop_name="Carrefour" location="(56.01123,3)"
4)-Run  python manage.py runserver 
5)- Access to http://127.0.0.1:8000/
6)-Begin with Registring.
7)-Enjoy testing functionalities
	As a User, I can sign up using username, my email & password
	As a User, I can sign in using my username & password
	As a User, I can like a shop, so it can be added to my preferred shops:
		Acceptance criteria: liked shops shouldn’t be displayed on the main page
	[BONUS] As a User, I can display the list of preferred shops.
	[BONUS] As a User, I can remove a shop from my preferred shops list (if removed it will be displayed on the main page automatically)





