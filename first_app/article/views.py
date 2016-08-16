from article.models import Article
from django.shortcuts import render

# Create your views here.
def index(request):
    title = request.GET['title']
    body = request.GET['body']
    article = Article(title=title, body=body)
    article.save()
    articles = Article.objects.all()
    return render(request, 'article/index.html', {'articles': articles})

def get_article(request, id):
    article = Article.objects.get(id=id)
    article = Article.objects.filtr
    return render(request, 'article/inner_page.html', {'article': article})
