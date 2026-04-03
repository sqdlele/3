from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db.models import Sum
from .forms import UserRegisterForm, UserLoginForm, ProfileForm, UserProfileUpdateForm
from .models import Profile
from blog.models import Article

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('core:home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('core:home')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@require_POST
def logout_view(request):
    logout(request)
    return redirect('core:home')

@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    user_articles = Article.objects.filter(author=request.user).order_by('-pub_date')
    published_count = user_articles.filter(published=True).count()
    drafts_count = user_articles.filter(published=False).count()
    total_views = user_articles.aggregate(total=Sum('views'))['total'] or 0
    recent_articles = user_articles[:5]

    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'published_count': published_count,
        'drafts_count': drafts_count,
        'total_views': total_views,
        'recent_articles': recent_articles,
    })

@login_required
def profile_edit_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = UserProfileUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль обновлен!')
            return redirect('accounts:profile')
    else:
        user_form = UserProfileUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
