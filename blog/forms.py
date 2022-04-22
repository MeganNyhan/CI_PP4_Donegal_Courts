# Imports
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
        This is the form for the create a news story post
    """
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is the Title Input'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is the Title_Tag Input'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'This is the Author Input'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'This is the Body Text Input'})
        }



