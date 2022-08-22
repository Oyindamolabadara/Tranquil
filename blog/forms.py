
from django import forms
from .models import Comment
from .models import Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    """
    Form class to add a comment
    """
    class Meta:
        model = Comment
        fields = ('body',)
        #widgets = {
            #'body': SummernoteWidget(),
            #'bar': SummernoteInplaceWidget(),
        #}

#class AnotherForm(forms.Form):
    #bar = forms.CharField(widget=SummernoteInplaceWidget())

class EditForm(forms.ModelForm):
     class Meta:
        model = Post
        fields = ('content',)
        widgets = {
            'content': SummernoteWidget
        }