from django import forms
from .models import Article, Category, Tag

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'image', 'category', 'tags', 'published']
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name'] 