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