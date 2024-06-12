from django.forms import ModelForm
from .models import Talk

class TaskForm(ModelForm):
    class Meta:
        model=  Talk
        fields= ['title', 'description','important']