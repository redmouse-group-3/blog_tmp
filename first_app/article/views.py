from article.forms import CommentForm
from article.models import Article, Comments
from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'article/index.html', {'articles': articles})


def get_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            form.save()
    form = CommentForm()

    return render(request, 'article/inner_page.html', locals())
