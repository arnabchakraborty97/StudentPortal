from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


class IndexView(ListView):
	model = Post
	template_name = 'forum/index.html'
	context_object_name = 'posts'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['range'] = range(context['paginator'].num_pages)
		return context


class PostDetailView(DetailView):
	model = Post
	context_object_name = 'post'


class PostCreateView(CreateView):
	template_name = 'forum/post_create.html'
	form_class = PostForm
	success_url = reverse_lazy('forum:index')


class PostUpdateView(UpdateView):
	template_name = 'forum/post_create.html'
	form_class = PostForm
	model = Post
	success_url = reverse_lazy('forum:index')


class PostDeleteView(DeleteView):
	model = Post
	success_url = reverse_lazy('forum:index')