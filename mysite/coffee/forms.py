from django import forms
from coffee.models import Post
from django.forms.widgets import TextInput
from django.core.validators import URLValidator


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=400, widget=TextInput(attrs={'placeholder': 'Title'}))
    body = forms.CharField(max_length=1000,widget=forms.Textarea )

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Post
        fields = ('title','body',)
