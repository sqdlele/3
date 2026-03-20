from django.shortcuts import render
from blog.models import Article, Category
from django.db.models import Q

# Create your views here.

def home(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')

    categories = Category.objects.order_by('name')
    articles_qs = Article.objects.filter(published=True)

    if category_id:
        articles_qs = articles_qs.filter(category_id=category_id)

    search_results = []
    latest_articles = articles_qs.order_by('-pub_date')[:8]
    if query:
        search_results = articles_qs.filter(
            Q(title__icontains=query) | Q(text__icontains=query),
        ).order_by('-pub_date')

    return render(request, 'core/home.html', {
        'latest_articles': latest_articles,
        'query': query,
        'categories': categories,
        'selected_category': category_id,
        'search_results': search_results,
    })
