from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Article, Category, Tag
from .forms import ArticleForm, CategoryForm, TagForm
from django.db.models import Q

def is_admin(user):
    return hasattr(user, 'profile') and user.profile.role == 'admin'

def article_list(request):
    articles = Article.objects.filter(published=True).order_by('-pub_date')
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, published=True)
    article.views += 1
    article.save(update_fields=['views'])
    return render(request, 'blog/article_detail.html', {'article': article})

@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()
            messages.success(request, 'Статья создана!')
            return redirect('blog:article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form})

@login_required
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья обновлена!')
            return redirect('blog:article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article_form.html', {'form': form})

@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Статья удалена!')
        return redirect('blog:article_list')
    return render(request, 'blog/article_confirm_delete.html', {'article': article})

@user_passes_test(is_admin)
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})

@user_passes_test(is_admin)
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория создана!')
            return redirect('blog:category_list')
    else:
        form = CategoryForm()
    return render(request, 'blog/category_form.html', {'form': form})

@user_passes_test(is_admin)
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория обновлена!')
            return redirect('blog:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'blog/category_form.html', {'form': form})

@user_passes_test(is_admin)
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Категория удалена!')
        return redirect('blog:category_list')
    return render(request, 'blog/category_confirm_delete.html', {'category': category})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})

def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Тег создан!')
            return redirect('blog:tag_list')
    else:
        form = TagForm()
    return render(request, 'blog/tag_form.html', {'form': form})

def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.success(request, 'Тег обновлен!')
            return redirect('blog:tag_list')
    else:
        form = TagForm(instance=tag)
    return render(request, 'blog/tag_form.html', {'form': form})

def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        messages.success(request, 'Тег удален!')
        return redirect('blog:tag_list')
    return render(request, 'blog/tag_confirm_delete.html', {'tag': tag})

def article_search(request):
    query = request.GET.get('q', '')
    articles = Article.objects.filter(
        Q(title__icontains=query) | Q(text__icontains=query),
        published=True
    ).order_by('-pub_date') if query else []
    return render(request, 'blog/article_search.html', {'articles': articles, 'query': query})
