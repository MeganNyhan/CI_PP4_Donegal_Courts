# imports
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy


class HomeView(ListView):
    """
        Create view for blog post list in home page
    """
    model = Post
    template_name = 'home.html'
    ordering = ['post_date']


class PostDetailView(DetailView):
    """
        Create view for blog post details in post detail page
    """
    model = Post
    template_name = 'post_detail.html'


class AddPostView(CreateView):
    """
        Create Add post view for creating blog posts on the site
    """
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class UpdatePostView(UpdateView):
    """
        Edite post view for editing/updating blog posts on the site
    """
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


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


def contact(request):
    return render(request, 'contact.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send an email
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['john@codemy.com'], # To Email
			)

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})