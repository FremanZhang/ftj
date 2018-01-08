# ftj

# 2017/11/23 test vscode integration successfully 

- The {% static %} function call should be used whenever you wish to reference static media within a template.

- When the application is deployed it is not secure to leave DEBUG equal to True. When you set DEBUG to be False, then you will need to set the ALLOWED_HOSTS variable in settings.py

- Remember to use the {% load staticfiles %} and {% static "filename" %} commands within the template to access the static files.

- Whenever you add to existing models, you will have to repeat this process running python manage.py makemigrations <app_name> first, and then python manage.py migrate