from typing import Any
from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from blogs.models import Blog,BlogComments,Category,Tag
from smartedu.views import BaseView
from pageDesign.models import *
from django.db.models import Q
from .models import Blog
from django.contrib import messages
from blogs.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class BlogList(BaseView):
    template_name = 'blog.html'
    items_per_page   =   10
    def get(self, request, category_slug=None, tag_slug=None, 
            *args: Any, **kwargs: Any):
        category_page = None
        tag_page = None
        current_user = request.user

        if category_slug is not None:
            category_page = get_object_or_404(Category, slug=category_slug)
            self.blogs         = Blog.objects.filter(category=category_page)
        elif tag_slug is not None:
            tag_page = get_object_or_404(Tag, slug=tag_slug)
            self.blogs    = Blog.objects.filter( tags=tag_page)
        else:
            self.blogs   =   Blog.objects.all()

        paginator   =   Paginator(self.blogs,self.items_per_page)
        page        =   request.GET.get("page")

        try:
            self.blogs =   paginator.page(page)
        except PageNotAnInteger:
            self.blogs     =   paginator.page(1)
        except EmptyPage:
            self.blogs     =   paginator.page(paginator.num_pages)

        return render(request, self.template_name, 
                      self.get_context_data(blogs=self.blogs))

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories']   =   Category.objects.all()
        context['tags']         =   Tag.objects.all()
        context["banner"]       =   Banners.objects.filter(name="Blogs").first()
        context["blogs"]        =   self.blogs
        context["references"]   =   References.objects.all()
        return context

class BlogDetail(BaseView):
    template_name = "blog-single.html"
    def get_context_data(self, **kwargs):
        cate    = Category.objects.filter(slug=self.category_slug).first()
        context = super().get_context_data(**kwargs)
        context["blog"] = Blog.objects.get(id=self.blog_id)
        context["blogs"] = self.blogs
        context["tags"] = Tag.objects.all()
        context["categories"] = Category.objects.all()
        context["comment_form"] =  CommentForm() # Yorum formunu ekleyin
        context["comments"]     =   BlogComments.objects.filter(blog_id=self.blog_id).all()
        context["current_user"] =   self.request.user

        context["cate_blogs"]   =   Blog.objects.filter(category=cate.id).all()
        
        context["comments_len"] = len(BlogComments.objects.filter(blog_id=self.blog_id).all())
        return context

    def get(self, request, category_slug, blog_id, *args, **kwargs):
        self.category_slug = category_slug
        self.blog_id = blog_id
        self.blogs = Blog.objects.all()

        current_user = request.user

        return render(request, self.template_name, self.get_context_data())

    def post(self, request, category_slug, blog_id, *args, **kwargs):
        blog = get_object_or_404(Blog, id=blog_id)
        current_user    =   request.user
        if request.method == "POST":
            if request.user.is_authenticated:
                form = CommentForm(request.POST)
                if form.is_valid():
                    try:
                        message = form.cleaned_data["message"]
                        mail = form.cleaned_data["email"]
                        author = form.cleaned_data["author"]
                        username    =   form.cleaned_data["username"]

                        # Assuming you have a model named BlogComments with fields 'text', 'author', 'email'
                        blog_comment = blog.blogcomments_set.create(text=message, author=author, email=mail, username=username)
                        if blog_comment:
                            messages.success(request, "Your comment was posted successfully!")
                            return redirect("blog_detail", category_slug=category_slug, blog_id=blog_id)
                        else:
                            messages.warning(request, "An error occurred while processing your comment. Please try again later.")
                            return HttpResponse("An error occurred while processing your comment. Please try again later.")
                    except Exception as e:
                        # Log the exception for further analysis
                        print(f"Error: {str(e)}")
                        messages.warning(request, "An error occurred while processing your comment. Please try again later.")
                        return HttpResponse("An error occurred while processing your comment. Please try again later.")
                else:
                    messages.warning(request, "Please correct the errors in the form and try again.")
                    return redirect("blog_detail", category_slug=category_slug, blog_id=blog_id)
            else:
                return redirect("register")  # Redirect to register page if the user is not authenticated
        else:
            # Handle the case when the request method is not POST
            return HttpResponse("Invalid request method.")
class Search(BaseView):
    template_name = "blog.html"
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        request = self.request
        search_term = request.GET.get('search', '')
        
        # Use Q objects to combine multiple conditions with OR
        context["blogs"] = Blog.objects.filter(
            Q(header__icontains=search_term) | 
            Q(description__icontains=search_term) | 
            Q(tags__name__icontains=search_term)
        ).distinct()  # Use distinct() to remove duplicates
        
        context["categories"] = Category.objects.all()
        context["tags"] = Tag.objects.all()

        return context