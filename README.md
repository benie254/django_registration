# django_registration
### A django_registration issues/challenges documentation with a Django boilerplate
### Created with [Django](https://) v. 4.0.5
#### Author [Benson Langat](https://github.com/benie254)

### Discalimer!

    This project sample is in DEV MODE 
    
    This project does not run because of settings modifications 

#### Use

* You can use this repo as a reference for your Django project.
* You can also use it as a starting point for your next project

#### To benefit better from this resource...

Consider changing only the following sections in this project's settings.py: 

>* line 63: Secret Key: (Importance: Crucial)
>* line 74: Installed apps (Importance: Crucial)

    * line 83-86: Installed apps (Optional)

>* line 109: Root URLConf (Importance: Crucial)
>* line 140: WSGI App (Importance: Crucial)
>* line 149-151: Databases (Importance: Crucial)
    
    * line 205-212: Location field configs (Optional)

>* line 215-219: cloudinary configs (Importance: Crucial)


## It will help a ton if you check out these sections:
>* line 23--helpful message
>* line 52--helpful message 
>* line 56--helpful message

### Consider this:

* If you wish to work between development & production now & then, 
* or after deployment, you would like to test something out in dev mode... 
* you can always switch between DEV and PROD. 
* This may not work for everyone, for reasons I am not yet sure, but try: 

>* The tip in line 23 of my settings.py + the tip in line 52 + the tip in line 56 

Despite contrary belief, you do not need to modify anything else. Well, that works for me. 

### Consider installing the following: 
>* cloudinary `pip install cloudinary` 
>* dj-database-url `pip install dj-database-url`
>* django-bootstrap5 `pip install django-bootstrap-v5`
>* django-bootstrap-form `pip install django-bootstrap-form` -- if you do not mind outdated -- check out [crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) as an alternative
>* django-columns `pip install django-columns`
>* django-heroku `pip install django-heroku`
>* django-registration v3.3 `pip install django-registration==3.3`
>* django-tinymce `pip install django-tinymce`
>* gunicorn `pip install gunicorn`
>* Pillow `pip install Pillow`
>* psycopg2 `pip install psycopg2`
>* python-decouple `pip install python-decouple`
>* pytz `pip install pytz`
>* whitenoise `pip install whitenoise`

## Consider the following documentations/links to help with using your resources: 

>* [Cloudinary](https://www.section.io/engineering-education/uploading-images-to-cloudinary-from-django-application/#setting-up-cloudinary) (not a documentation, but quite helpful)
>* [Django-bootstrap5](https://django-bootstrap-v5.readthedocs.io/en/latest/)
>* [Django-bootstrap-forms](https://django-bootstrap-form.readthedocs.io/en/latest/) (outdated) -- if you do not mind outdated. (worth considering: [crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/))
>* [Django-columns](https://django-columns.readthedocs.io/en/latest/readme.html)
>* [Django-registration v3.3](https://django-registration.readthedocs.io/en/3.3/quickstart.html#configuring-the-one-step-workflow)
>* Read this with django-registration: [Django Authentication System](https://docs.djangoproject.com/en/4.0/topics/auth/default/)

# Django Registration 
## You may face some challenges working with django registration. 
### In this section... 

* We will focus on only the url patterns and template structures. 

But first... 

### Which version of django-registration should you use? 
##### Consider, then decide:

* django-registration==2.4.1
  * **downgrades django to 1.1.1**


    yourproject/urls.py

    urlpatterns = [
        url(r'^accounts/', include('registration.backends.simple.urls')),
    ]

**Your templates will need:**
>* a registration subfolder `templates/registration`
>  * a registration_form template `templates/registration/registration_form.html`
>  * login template `templates/registration/login.html`

* django-registration==3.3
  * requires **django v4.0.4** or later 
  * will install **django 4.0.4** if you're using an older version 


#### OPTION 1

    yourproject/urls.py

    # You will need all these

    urlpatterns = [
        path('accounts/', include('django_registration.backends.one_step.urls')),
        path('accounts/', include('django.contrib.auth.urls')),
        path('accounts/profile/', auth_views.LoginView.as_view(template_name='user/profile.html')),
        path('logout/', auth_views.LogoutView.as_view(template_name='registration/login.html')),
    ]

>your templates will need all these:
>* a django_registration subfolder `templates/django_registration`
>  * a registration_form template `templates/django_registration/registration_form.html`
>  * a registration_complete template `templates/django_registration/registration_complete.html`
>* a registration subfolder `templates/registration`
>  * a login template `registration/login`
>* a user subfolder `templates/user`
>  * a profile template `templates/user/profile.html`

#### OPTION 2 

    urlpatterns = [
        path('accounts/', include('django_registration.backends.one_step.urls')),
        path('accounts/', include('django.contrib.auth.urls')),
        path('accounts/profile/', auth_views.LoginView.as_view(template_name='content/index.html')),  
        path('logout/', auth_views.LogoutView.as_view(template_name='registration/login.html')),
    ]

>your templates will need all these:
>* a django_registration subfolder `templates/django_registration`
>  * a registration_form template `templates/django_registration/registration_form.html`
>  * a registration_complete template `templates/django_registration/registration_complete.html`
>* a registration subfolder `templates/registration`
>  * a login template `registration/login`


#### You will notice something with the as_view() function 
##### that we use in our paths. 

* The function defines a template that we want to render our view in... 
* so, you can route users to any template in only the case of the paths: 
* `'accounts/profile/'` and `'logout/'`. 
* The same will not work for `registration` or `registration_complete`, 
* because Django has predefined the templates that should render these. 

#### Note that 
* our login view has a predefined route `'accounts/profile/'` 
* which Django will try to find for a successful render. 

#### Also, important to keep in mind is that... 
* if you choose to redirect users to a particular template, your route will remain the same. 
* This is important in deciding the content of the template you route your users to. 
##### What I mean in practical terms is... 
* if for the path predefined by django, `'accounts/profile'` , 
* which ideally logs users in, 
* you choose to render a template like your home page at 'index.html'... 
* your route at the browser address bar will read `'.../accounts/profile'` 
* ... which I find awkward for a Home page or any other page that does not serve a user profile logic. 
* This is why I prefer routing to a user subfolder, 
* which holds a `'profile.html'` template--
* this template will serve the purpose that the route suggests. 
* On top of it, if I add a navbar to the user profile template, 
* users can navigate from that point to anywhere else in the app. Just a thought. 

## Screenshots 
### 1. We will try to log in:
<img src='https://user-images.githubusercontent.com/99865051/171784545-2a16ef2c-289d-4ed9-8cf1-266ef4eafec4.png'>

### 2. Here, we route users to the home page 
#### using this pattern: path('accounts/profile/', auth_views.LoginView.as_view(template_name='content/index.html'))
<img src='https://user-images.githubusercontent.com/99865051/171785014-619563af-4e8c-48b7-b5b0-b49563464e29.png'>

#### can you see the address bar? It reads '...accounts/profile'

### 3. Here, we route users to the Profile page
#### using this pattern: path('accounts/profile/', auth_views.LoginView.as_view(template_name='user/profile.html')),
<img src='https://user-images.githubusercontent.com/99865051/171785368-6cd0801b-9f3a-4e71-9ef5-02528643a7ad.png'>

#### the address bar reads '...accounts/profile' -- and the page renders logic relevant to the route


## Something else... 
### Assuming you have worked out some registration & login forms... 
### Do not forget to add some content to your registration_complete page 

* This page is easy to overlook, before you test everything out. 
* But remember, django-registration v3.3 predefines a route for `registration_complete`.
* Meaning that after a successful registration, users will always be redirected
* to the registration_complete page at `templates/django_registration/registration_complete.html`
* I am not yet sure how to override this, but there is an option. Perhaps, checkout the docs [here](https://django-registration.readthedocs.io/en/3.3/quickstart.html#configuring-the-one-step-workflow) or [here](https://docs.djangoproject.com/en/4.0/topics/auth/default/)
* If you do not mind having the page,
* or if you find it helpful, like I do...
  * consider adding some content.
  * something simple, with a helpful redirect link to any page will do.
  * you can also add your navbar to this page 
  * and, considering no limitations, what about a few more quick links?

#### That is all from me. I will update this when something comes up, changes, or adds to what I can share. 
#### Feel free to contribute, share your thoughts, or highlight an issue. 

Reach out to [Benie-throughmail](davinci.monalissa@gmail.com)

Until next time, happy coding!

#### Cheers! 

[Benie](https://github.com/benie254)