# # # some of import method to Use

# # .\myenv\Scripts\activate

# # pip install django

# # pip install djangorestframework

# # django admin

# # django-admin startproject drinks . (to create a new project name drink in the current directory)

# # python manage.py runserver (to start the server)

# # python manage.py createsuperuser (a user to acces django admin dashboard)

# create a file model.py (to create our databse from django.db import models, the create the class of the model with model.Model)

# create the file admin.py to manage the admin by importing admin from django.contrib and also import the model, then register the model with the admin by using (admin.site.register(model name))

# # python mange.py makemigrations drinks (drinks our first model - to make a migration of it)

# # python mange.py migrate (to apply all the changes to the server)

# then create a serializers file to convert the python object use to represent then data on the model to json by importing serializer from rest_framework and also import the model then create a class of modelserializer with serializer.modelserializer method, after which youll create the Meta class that contains the models and the fields required

# then we create our endpoints imside a view.py file, by importing jsonresponse from django.http, import the model, import the serializer. deefine a function to get all that accept rrquest as arguement create the drinks variable by getting the drinks from the model Drink.object.all, then we pass them into the serializer, then we return the jsonresponse of the serializer

# then we create a url path foor our endpoints in tthe file url.py

python manage.py startapp Employee (to create a new app)

- register the app in the required module located in settings.py (installed app)

- add the cors header to the mildleware
- add cors instrustion to allow all domain to access the app (CORS_ORIGIN_ALLOW_ALL = true)
- connect your mongo db database (connect with atlas compass then connect to app drivers)

authMechanism": "SCRAM-SHA-1" (for atlas cloud db)
