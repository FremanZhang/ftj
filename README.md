# ftj

## 2017/11/23 test vscode integration successfully

- The {% static %} function call should be used whenever you wish to reference static media within a template.

- When the application is deployed it is not secure to leave DEBUG equal to True. When you set DEBUG to be False, then you will need to set the ALLOWED_HOSTS variable in settings.py

- Remember to use the {% load staticfiles %} and {% static "filename" %} commands within the template to access the static files.

- Whenever you add to existing models, you will have to repeat this process running python manage.py makemigrations <app_name> first, and then python manage.py migrate

- The question_id='34' part comes from (?P<question_id>[0-9]+). Using parentheses around a pattern “captures” the text matched by that pattern and sends it as an argument to the view function; ?P<question_id> defines the name that will be used to identify the matched pattern; and [0-9]+ is a regular expression to match a sequence of digits.

        detail(request=<HttpRequest object>, question_id='34')
        url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),