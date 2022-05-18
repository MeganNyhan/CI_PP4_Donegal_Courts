# Imports
from django import forms
from .models import Post, Comment


class EditForm(forms.ModelForm):
    """
        This is the EDIT form for the create a news story post editor
    """
    class Meta:
        model = Post
        fields = ('title', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is the Title Input'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'This is the Body Text Input'})
        }
    

class CommentForm(forms.ModelForm):
    """
        This is the EDIT form for the create a news story post editor
    """
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }

