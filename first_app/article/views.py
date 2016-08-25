from article.forms import CommentForm
from article.models import Article, Comments
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    articles = Article.objects.all()
    if 'q' in request.GET:
        articles=articles.filter(title=request.GET['q'])
    return render(request, 'article/index.html', {'articles': articles})

class ArticleView(TemplateView):
    template_name = 'article/inner_page.html'
    def get_context_data(self, id, **kwargs):
        kwargs['form']= CommentForm()
        kwargs['article']= get_object_or_404(Article, id=id)

    def post(self, request, id):
        article = get_object_or_404(Article, id=id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            form.save()

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
