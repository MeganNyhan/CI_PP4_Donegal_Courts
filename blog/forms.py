# Imports
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
        This is the form for the create a news story post
    """
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'snippet', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is the Title Input'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is the Title_Tag Input'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'This is the Author Input'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'This is the Body Text Input'})
        }


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



