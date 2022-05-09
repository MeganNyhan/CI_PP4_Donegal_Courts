# Imports
from django import forms
from .models import Post, Comment


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


class ContactForm(forms.Form):
    """
    This is Contact Form 
    This uses a Field level Validation
    """
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())

    def clean_email(self):  # Returns clean data
        email_passed = self.cleaned_data.get("email")

        return email_passed
