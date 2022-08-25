""" Form models """
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment
from .models import Post


class CommentForm(forms.ModelForm):
    """
    Form class to add a comment
    """
    class Meta:
        """ Comment form model """
        model = Comment
        fields = ('name', 'body',)
        widgets = {
            'body': SummernoteWidget
        }


class EditForm(forms.ModelForm):
    """
    Form class to edit a comment
    """
    class Meta:
        """ Edit form model """
        model = Post
        fields = ('content',)
        widgets = {
            'content': SummernoteWidget
        }
