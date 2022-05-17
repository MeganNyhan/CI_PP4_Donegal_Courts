# imports
from django.shortcuts import render,redirect, get_object_or_404 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse_lazy, reverse
from django import forms
from django.contrib import messages


def contact(request):
    """
        Create view for contact page
    """
    if request.method == "POST":
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ('Your message has been sent successfully!'))
        return render(request, 'contact.html')
    else: 
        return render(request, 'contact.html')


class HomeView(ListView):
    """
        Create view for blog post list in home page
    """
    model = Post
    template_name = 'home.html'
    ordering = ['post_date']
    paginate_by = 6


class PostDetailView(DetailView):
    """
        Create view for blog post details in post detail page
    """
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data()

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context


class UpdatePostView(UpdateView):
    """
        Edite post view for editing/updating blog posts on the site
    """
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # Success Message


class DeletePostView(DeleteView):
    """
        Edite post view for editing/updating blog posts on the site
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCommentView(CreateView):
    """
        Create Add post view for creating blog posts on the site
    """
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

