from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Comments, Category
from .forms import Create_new_article, Edit_existing_article, CommentForm
from django.contrib import messages

# Create your views here.
def article_view(request):
    articles = Article.objects.all()
    edit_permission = False

    context = {
        'articles': articles,
        'edit_permission': edit_permission,
    }
    return render(request, 'article_layouts/article.html', context)

def article_detail(request, id):
    article = get_object_or_404(Article, article_id=id)
    comment = Comments.objects.all()
    edit_permission = False
    comment_form = CommentForm()  # Inicializar el formulario fuera del bloque de autenticación

    if request.user.is_authenticated:
        if request.user.user_type in ['Collaborator', 'Superuser', 'Member']:
            edit_permission = True
            if request.method == 'POST' and 'delete_article' in request.POST:
                article.delete()
                messages.success(request, 'El articulo ha sido borrado correctamente')
                return redirect('articles')

            if request.method == 'POST' and 'comment_article' in request.POST:
                comment_form = CommentForm(request.POST)
                if comment_form.is_valid():
                    comment = comment_form.save(commit=False)
                    comment.related_article = article
                    comment.comment_ownership = request.user
                    comment.save()
                    messages.success(request, 'Creaste el comentario correctamente!')
                    return redirect('article_detail', id=id)

    context = {
        'article': article,
        'edit_permission': edit_permission,
        'comment_form': comment_form,
        'comment': comment
    }

    return render(request, 'article_layouts/article_detail.html', context)

@login_required
def edit_article(request, id):
    edit_form = get_object_or_404(Article, article_id=id)
    categories = Category.objects.all()
    
    if request.method == 'POST':
        edit_form = Edit_existing_article(request.POST,request.FILES, instance=edit_form )
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'El articulo ha sido editado correctamente')
            return redirect('article_detail', id=id)
        else:
            messages.error(request, 'Articulo inválido, intente otra vez')
            return redirect('edit_article', id=id)
    else:
        edit_form = Edit_existing_article(instance=edit_form)

    context = {
        'edit_form': edit_form ,
        'categories': categories
    }

    return render(request, 'article_layouts/edit_article.html', context )


@login_required
def create_article(request):
    if request.method == 'POST':
        form = Create_new_article(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.article_ownership = request.user
            article.save()
            messages.success(request, '¡El artículo ha sido creado exitosamente!')
            return redirect('articles')
        else:
            messages.error(request, 'Artículo inválido, por favor intente nuevamente.')
    else:
        form = Create_new_article()
    
    return render(request, 'article_layouts/create_article.html', {'form': form})


