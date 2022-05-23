# Coding with Mitch 23/06/2022
## Building a blog using Django
### (fresher_mwanzo -- make sure you have checkout to that branch)
- Installing python into your operating system
- Installing virtualenv wrapper allowing us to recreate different python environments for our different projects
- Creating a virtualenv environment and installing the required packages or dependencies using ``pip install or pip3 install``.
- Starting or setting up our first django project using the ``django-admin startproject <nameofproject> <workingdirectory>``.
### Requirements
- The projects requirements are the core basic for any project since they determine the behaviour of the project as they are the libraries that constitute to the building block of the project.
- The good use case for requirements for our django project comes in handy in these two notable scenerios.
	- When you are working in team (more than 1 ) the chances of being in sync is high and therefore we expect that each team member needs to have equal identical requirements in their machine setups.This is achieved by storing the project requiremnts in a txt file called requirements(can be called anything) and storing it in the project root directory.
	- The second scenerio is where we want to move to production and we want to have an identical setup as the one we had in our machine.This therefore allows us to store this information in a txt file called requirements which we will use to install our requirements/dependencies/packages/libraries that our webapp depends on.
-  `pip freeze ` - this list all the dependencies that a given project depends on and their versions.
-  `pip freeze > <filename>` the > greater than sign redirects the output of the pip freeze command to be written and stored in a file provided by the end user.
more research on the output redirection operator can be found here: https://www.makeuseof.com/tag/save-command-line-output-file-windows-mac-linux/
- Now once that is done, the question is mind is how are we now able to install or download our requirements back to our project.How do we do it?
So a simple command `pip install -r <requirements filename>` will ensure we are installing our projects dependencies from the provided requirements file.
### Development
- We realise that django works with sub-project category which is called apps. A project can have apps inside it that can do different tasks and can be consilidated to communicate with each other inorder to make the web app functional.
- We create an app in django using the command `python manage.py startapp <nameoftheapp>` or `django-admin startapp <nameofapp>`. Once you create the app, you are suppose to map it in the settings.py file in the installed_apps variable which is a list.
- Then we have to navigate inside our newly created app directory and look at the files we have, at the moment , we will focus with the views.py file since it comes to say that a faster and good production norm is to start with the view or rather the layout determining what you want to visualize and how you are going to achieve that, that literallly gives you a clear aspect of what you want to build and how you are going to achieve it.
- We will navigate to the root of our base directory or rather inside the mitchblog directory and create a folder called template.This folder can contain a master blueprint of how our views is going to look like from the footer and header and also the body which can contain alot of dynamic data change.
- We will create a file inside the template directory structure called base.html.Inside base.html we will write the following code which represents the django template language that will help us to write html code or rather frontend code in a fun way that is less verbose and quick.
```
{# this is a comment inside the base.html file #}
<!DOCTYPE html>
<html>
<head>
<title> This is the page's title </title>
<h1>This is the title</h1>
</head>
<body>
{# This section is dynamic and so we will use the block content syntax #}
{% block content %}
{% end block content %}
</body>
<footer>
<h1>This is the footer</h1>
</footer>
</html>
```
- The above code looks and feels just like normal html just that we have some new introductons in the html eco-system.They are the Django Template Language constructs(construction blocks).The synatx in curly braces are simple syntax for DTL and DTL is one of django major template backend engine which as 4 constructs namely:
	- Variables : They are deal with storing data which can be accessed , read and manipulated.
		- example = ``{{ firstname }}`` -- they have double curly braces.
	- Tags : They deal with the logic that can be placed on data such as if - endif , for etc.
		- example = ``{% block content %}``
	- Filters - They deal with how data is presented.
		- example = ``{{firstname|title}}``
	- Comments - They are normally not rendered or displayed on the screen since they are just guidelines to help other developers or even guide you as a developer when you are developing you idea.
		- exmple= `{ # this is a comment # }`
-Once that is done, we have to navigate to the settings file found in our config directory where we will change the template dictionary under the key DIR where we will use os library so as to map our directories path.You can use any library you desire such as Path to achieve the same.
`os.path.join(BASE_DIR, templates)` the Base_DiR points to root directory.
#### Views.py
- Heading to our Views file inside our personal app folder structure we will write a functional view which is able to show parameters of the request varible on the linux terminal.We will also render our base html and see how it looks.
```python
# This is the views.py folder
from django.shortcuts import render

# your views goes here
def home_screen_view(request):
	print(request.headers) 
	# you can do dir(request) and see other methods viable
	return render(request, "base.html", {})
```
request .headers output
```
{'Content-Length': '', 
'Content-Type': 'text/plain', 
'Host': '127.0.0.1:8000', 
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 
'Accept-Language': 'en-US,en;q=0.5', 
'Accept-Encoding': 'gzip, deflate, br', 
'Connection': 'keep-alive', 
'Upgrade-Insecure-Requests': '1', 
'Sec-Fetch-Dest': 'document', 
'Sec-Fetch-Mode': 'navigate', 
'Sec-Fetch-Site': 'none', 
'Sec-Fetch-User': '?1', 
'Cache-Control': 'max-age=0'}
```
- The above code tells us that request varible has some methods that contain some project specific infomation.We are able to know what the request variable holds by doing a simple `dir(request)` this is going to help us know methods that a particular variable posses.
- Our final line which is being returned invokes the render function(Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text. )
```
return render(request, "base.html", {})
```
	- request is the HttpResponse object.
	- base.html is the template that will hep in visualizing the data.
	- {} is a dictionary representing context.Context is a dictionary that has data which can be read and accessed by the template via the context keys.

### Templating
- This represents the html files which depend on Django templating engine inorder to help in visualizing manipulating html files with data and logic.Django uses the DTL - Django templating language which has djangoTL as its engine that helps in generating html dynamically covering for both static data and dynamically rendered data.Django can work with or without a templating engine and it goes the extra mile of supporting 3rd templating engine such as Jinja2 which is another famous template engine.
- In our project we created a folder inside our root project as shown below:
![70bb29e6ee0ac2feb2d1ea39853e2715.png](:/d1d1b9f25b0648b980cbe98d96418f03)
- The templates folder will constitute or house our templates files.Inside the templates folder, we have one universal html file called base.html file.This file is responsible for housing the common layout structure allowing us to reuse and write less code.This strongly improve efficiency.
![924d5d33bfa200fc0fc38ca0c91e6d07.png](:/496cf1a586e747d1bb1e8a16a11779fd)
- Inside Base.html we have the following code with dtl syntax.
```
<!DOCTYPE html>
<html lang="en">
<head>
    <title>This is the header</title>
    <div style ="border: 2px solid #000;">
        <h1>This is the header</h1>
    </div>
</head>
<body>
    {% block content %}

    {% endblock content %}
</body>
<footer>
    <div style="border: 2px solid #000;">
        <h3>This is the footer</h3>
    </div>
</footer>
</html>
```

- This code is going to be inherited with our templates created within the project scope. Inside each app I went ahead and created a folder called templates which contains html files unique to a given app in the project.This however makes our code decoupled and tidy in line to DRY principles as shown below.
![a8184f81a6e1d12ad8412836faf853d8.png](:/eceec1c274b44a6295f988d8adc7edc9)
(close up)
![1588801adbdadf9c56965054dfe62e07.png](:/ce3cd7bf4b43485ca9863b3a589164d7)
- As you can see we have home.html and also we have a folder called snippets that is responsible for a template html file called snippets which is supposed to help us design and shape layouts which are reusable by coding and designing them in a common file making it easy to edit the file.
![bbc520b75023a6ce40308fa0ef8b16af.png](:/c811c6a89e0e42afb49d41fed6d93383)
	- Extends base.html means that we are able to acquire any declaration or code of base.html and we are able to add more functionality our new file without wrting things from scratch. 
	- Block content and end block represents the sections that will go to be replace in the base.html.Rember in our base.html file we made some section empty saying that dynamic data can be rendered here?
	- include is how we are able to port or add a file inside our file.Hence snippets.
	- for and end for represents a loop structure allowing us to loop through our data in a simple fashion and through the help of the snippet allow us to determine how each element looks.
	![4d52601ee65c44aa58893549255c7fde.png](:/9b68c3f062c5483886ab5eeb3aba4774)
- Inside it we have another folder called the personal folder and inside the personal folder we have a html file which is our first template.The Question that might arise is why did we create another folder inside our templates folder.The answer to that is that we want to create separate folders representing all the different apps we have for this project containing individual tempatles for each app.
-Inorder for templates to work, navigating to the settings file we have to chnage the templates directory path setttings inorder for django to be able to load templates into the project.
![2b7e232c5c52f7fcef19425645462937.png](:/5c2c10f803134aada8b279fdd36aaefa)
- Now we are navigatting deeper into templates and therefore one key take away is that we have the 4 constructs of templating and they all come into play in the following ways :
	- varible -  remember a varibale take the syntax ``{{varibale_name}}``.This can be seen in the home.html file. This varible comes from the context dictionary that is present in the views.py file.Since it is a dictionary we can have a dictionary of lists or a dictionary of dictionaries etc as long as we index it properly.
```python
from django.shortcuts import render

# Create your views here.
# functional views
def home_screen_view(request):
    context = {}
    # context['somekeystring'] = "Some value to the view"
    # context['some_number'] = 12

    context ={
        'somekeystring':"Some value to the view",
        'some_number':12
    }
	
    list_of_values = []
    list_of_values.append("first entry")
    list_of_values.append("second entry")
    list_of_values.append("third entry")
    list_of_values.append("fourth entry")
    context['list_of_values'] =  list_of_values
    return render(request, "personal/home.html", context)
```

### Admin section
- Every project you need a user to allow you to access the admin section.
```sh
python manage.py createsuperuser
```

- The above script allows you to create a user for ur project.We can navigate to the admin section using the /admin endpoint or url.
- Afterwards, we are able to do migrations allowing us to port changes we have done on the django orm to translate on our database.
``python manage.py makemigrations``

### Models.py
- Inside the models.py in the personal folder, we created a model and in simpler term a model is class that represents a table in the actual database.Each class instance is a row for that table and each row inherits or is affected by the defined class methods determining how each row of data will be manipulated.We normally start by inheriting the models library from django , as shown below
```
from django.db import models

# Create your models here.
class Question(models.Model):
	pass

```
- This allows us to us Django inbuilt field types all representing how we are able to represent data of different characteristics for example we have intergers , we have text field , we have character fields etc.
```
class Question(models.Model):
    title =  models.CharField(max_length=100)
    question = models.TextField(max_length=400)
    priority = models.CharField(max_length=12, choices=PRIORITY)
```
- The above represents just a portion of the field type we have in django, since they are alot.More info about that section can be found here: https://docs.djangoproject.com/en/4.0/ref/models/fields/#model-field-types 
- We also define class methods and the class Meta so as to add more functionality affecting the behaviour of data.
```
from django.db import models
#choice list with tuples
PRIORITY = [
("LOW","low"),
("MEDIUM","medium"),
("HIGH","high")
]
  
# Create your models here.
class Question(models.Model):
    title =  models.CharField(max_length=100)
    question = models.TextField(max_length=400)
    priority = models.CharField(max_length=12, choices=PRIORITY)

    def __str__(self): 
	# determines how each instance will appear in the admin section
        return self.title
    class Meta:
	# describes more information about model in the admin section
        verbose_name = "Their Questions"
        verbose_name_plural = "People Questions"
```

### admins.py
- Inside the admins.py file we have to register our model so that it can appear in the admin section and we are able to manipulate that file.
```
from django.contrib import admin
from personal.models import Question

admin.site.register(Question)
```

### views.py
- Inside our views file , we are able to query the data from the model and pass it into the context as a key value pair and use a for loop in our templates to render that particular data.We are able to access properties of the model data by being able to query data of each column of the model and make it appear on the screen.
```
from django.shortcuts import render
from .models import Question
# Create your views here.
# functional views
def home_screen_view(request):


    data_qst = Question.objects.all()
    context ={
        'somekeystring':"Some value to the view",
        'some_number':12
    }

    context['questions'] =  data_qst
    return render(request, "personal/home.html", context)
	
```

- templates
```
{% extends 'base.html' %}


{% block content %}

<div style="border: 2px solid #000;">
    <h1>This is the body</h1>
    <p>This is the part of the code that changes</p>
    <p>{{somekeystring}} {{some_number}}<p>
{# doig loops in django template #}
<ul>
    {% for question in questions %}
    <li>{% include "personal/snippets/body_snippets.html" with value=question %}</li>
    {% endfor%}
</ul>

</div>

{% endblock content %}
```
snippets file
```
<h3>{{value.title}} | {{value.priority}}<h3>
<p style="margin-left: 10px;">{{value.question}}</p>
```
The above is the end of this fresher tutorial,
Next we are embarking on the actuall building of the blog.
This will be in a branch called -fresher_mwanzo
