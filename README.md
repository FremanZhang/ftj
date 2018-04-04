# ftj

## 2017/11/23 test vscode integration successfully

- The {% static %} function call should be used whenever you wish to reference static media within a template.

- When the application is deployed it is not secure to leave DEBUG equal to True. When you set DEBUG to be False, then you will need to set the ALLOWED_HOSTS variable in settings.py

- Remember to use the {% load staticfiles %} and {% static "filename" %} commands within the template to access the static files.

- Whenever you add to existing models, you will have to repeat this process running python manage.py makemigrations <app_name> first, and then python manage.py migrate

- The question_id='34' part comes from (?P<question_id>[0-9]+). Using parentheses around a pattern “captures” the text matched by that pattern and sends it as an argument to the view function; ?P<question_id> defines the name that will be used to identify the matched pattern; and [0-9]+ is a regular expression to match a sequence of digits.

        detail(request=<HttpRequest object>, question_id='34')
        url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

- V8.3
1. Cannot check existence.
2. String case seneitive. python, Python, pyTHON
3. Add datetime in Homepage: year_SN, week_SN, day_SN
4. TIME_ZONE = 'Asia/Shanghai', USE_TZ = True
5. add_page.html
6. add https compatibility
7. click 'create page' will add page repeatly. cookie?

- V9.5
1. Django build-in support: Note that we make use of the **user** object, which is available to Django’s template system via the context.

        {% if user.is_authenticated %}
        <h1>Rango says... hello {{ user.username }}!</h1>
        {% else %}
        <h1>Rango says... hello world!</h1>
        {% endif %}

- V10.5
1. These two sentances are different:
        return render(request, 'rango/login.html', {}) # working well
        return render(request, '/rango/login.html', {}) # this will cause TemplateDoesNotExist exception
2. <ExtendsNode: extends "base.html"> must be the first tag in the template.

- V11.6
1. Alternatively, persistent sessions are enabled by default, with SESSION_EXPIRE_AT_BROWSER_CLOSE either set to False, or not being present in your project’s settings.py file.
2. Django Doc suggests running this daily as a cron job:
        python manage.py clearsessions

- V19.2
1. Add like_category function

        base.html imports ajax -> category.html add display -> like_cateogry view -> urls -> rango-ajax.js