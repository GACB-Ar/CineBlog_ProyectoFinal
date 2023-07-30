from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Create_new_article
from django.contrib import messages

# Create your views here.
def article_view(request):
    return render(request, 'article_layouts/article.html')

@login_required
def create_article(request):
    if request.method == 'POST':
        form = Create_new_article(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.article_ownership = request.user
            article.save()
            return redirect('home')
        else:
            messages.error(request, 'Articulo inválido, intente otra vez')
    else:
        form = Create_new_article()
    
    return render(request, 'article_layouts/create_article.html', {'form': form})