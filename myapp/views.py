from django.shortcuts import render , redirect
from django.http import HttpResponse
from myapp.models import Author ,Article
from django.core.exceptions import ObjectDoesNotExist
from myapp.forms import ArticleForm , AuthorForm
from django.views.generic import ListView , DetailView , FormView , CreateView ,UpdateView
from django.urls import reverse_lazy , reverse
# Create your views here.
def hello_world(request):
    return render(request, 'hello.html', {
        'name' : 'ibrahim',
        'categories' : [
            'Catagory 1',
            'Catagory 1',
            'Catagory 2',
            'Catagory 3',
            'Catagory 4',
        ]
    })




def home(request):
    article = Article()
    article.title = 'Python Article 2'
    article.content = 'Python article 2 content here.'
    article.auther = Author(2)
    article.save()
    return render(request , 'home.html')

def about(request):
     return render(request, "about.html")
# -----------------------------------------------------------------------------------------------------------------
 
# def articles(request):
#     # models = Article.objects.select_related("auther").all()[:10]
#     models = Article.objects.select_related('auther').prefetch_related("tags").all()[:10]
    
#     return render(request,'article/list.html', {
#         'articles': models
#     })

# def show_article(request , id):
    
    
#     article = Article.objects.get(pk = id)
    
   
#     return render(request, 'article/show_article.html', {
#         'article' : article
#     })


# def update_article(request , id):
    
#     Article.objects.filter(pk=id).update(auther= Author(2))
#     article = Article.objects.get(pk = id)
    
   
#     return redirect(f'/myapp/article/{id}')

def delete_article(request , id): 
    
    article = Article.objects.get(pk = id)
    article.delete()
    
   
    return redirect('/myapp/')


# def create_article(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             content = form.cleaned_data['content']
#             author = form.cleaned_data['author']
#             tags = form.cleaned_data['tags']
#             article = Article.objects.create(title=title, content=content, auther = author )
#             article.tags.set(tags )
#             return redirect('/myapp/')
#     else:
#         form = ArticleForm()
#     return render(request, 'article/create.html', {
#         'form' : form
#     })


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            Author.objects.create(
            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            birth_date = form.cleaned_data['birth_date'],
            bio = form.cleaned_data['bio'],
            )
            return redirect('/myapp/')
    else:
        form = AuthorForm()
    return render(request, 'author/create.html', {
        'form' : form
    })


class ArticleListView(ListView):
    model = Article
    template_name = 'article/list.html'
    # context_object_name = 'article'
    queryset = Article.objects.select_related('auther').prefetch_related("tags").all()


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/show_article.html'


# class ArticleCreateView(FormView):
#     form_class = ArticleForm
#     template_name = 'article/create.html'
#     # success_url = '/myapp/'

#     def get_success_url(self):
#         return reverse('article_list')
    

#     def form_valid(self, form):
#         article = Article.objects.create(
#         title = form.cleaned_data['title'],
#         content = form.cleaned_data['content'],
#         auther = form.cleaned_data['author'],
#         )
#         article.tags.set(form.cleaned_data['tags'] )
#         return super().form_valid(form)

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/create.html'
    success_url = reverse_lazy('article_list')
    

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/update.html'
    success_url = reverse_lazy('article_list')
