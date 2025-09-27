from django.shortcuts import render
from blog.models import Article
from django.db.models import Q

# Create your views here.

def home(request):
    latest_articles = Article.objects.filter(published=True).order_by('-pub_date')[:5]
    query = request.GET.get('q', '')
    search_results = []
    if query:
        search_results = Article.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query),
            published=True
        ).order_by('-pub_date')
    return render(request, 'core/home.html', {
        'latest_articles': latest_articles,
        'query': query,
        'search_results': search_results,
    })
