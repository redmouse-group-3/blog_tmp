from article.models import Article
from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
    # title = request.GET['title']
    # body = request.GET['body']
    # article = Article(title=title, body=body)
    # article.save()
    articles = Article.objects.all()
    return render(request, 'article/index.html', {'articles': articles})

def get_article(request, id):
    article = get_object_or_404(Article, id=id)
    # article = Article.objects.get(id=id)
    return render(request, 'article/inner_page.html', locals())
