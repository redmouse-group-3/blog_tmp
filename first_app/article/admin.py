from article.models import Comments, Article
from django.contrib import admin

def make_published(modeladmin, request, queryset):
    for q in queryset:
        q.title = q.title + q.title
        q.save()
make_published.short_description = "Change title"

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    fields = ('body',)
    list_filter = ('title',)
    search_fields = ['title', ]
    actions = [make_published]
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comments)