"""Views for blog; home, posts and promos"""

from django.shortcuts import render, redirect
# CBV
from django.views.generic.edit import DeleteView
# Decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# My models and forms
from blog.models import Post
from blog.forms import NuevoPost
from users.models import Avatar

def inicio(request):
    """Página home blog"""
    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    context = {
        'avatar': avatar,
        'title': 'Inicio',
        'message': 'Bienvenidos a Compara tu lava, primer blog de lavaderos de autos',
        'subtitle': '¿Planificando tu próximo lavado de auto? '
                'Lee las experiencias realizadas por los propios miembros del blog!',
        }
    return render(request, 'blog/inicio.html', context)

def posts(request):
    """View for posts page."""
    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    # Defino variable conteniendo todos los posts ordenados de mas nuevo a mas antiguo
    posts = Post.objects.order_by('-date_added')

    # Para buscar posts por ciudad
    city = request.GET.get('city')
    if city:
        posts = Post.objects.filter(city__icontains=city)
        context = {
            'name': 'name',
            'title': 'Posts',
            'city': city,
            'search': 'Buscar por ciudad',
            'posts': posts,
            'avatar': avatar,
        }
        return render(request, 'blog/posts.html', context)
    
    else:
        # Listar todos los posts
        context = {
            'posts': posts,
            'name': 'name',
            'title': 'Posts',
            'subtitle': '¡El listado completo de nuestros posts!',
            'search': 'Buscar por ciudad',
            'avatar': avatar,
        }
        return render(request, 'blog/posts.html', context)

@login_required
def agregar_post(request):
    """View to add new posts."""

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    if request.method != 'POST':
        # No data submited. Paso formulario vacio
        form = NuevoPost()
    
    else:
        # Data submitted. Paso formulario con datos ingresados por POST
        form = NuevoPost(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
           
            return redirect('blog:Posts')

    context = {
        'form': form, 
        'title': 'Nuevo Post',
        'avatar': avatar,
    }
    return render(request, 'blog/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """Edit an existing post."""

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    # Post que se va a editar
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        # No data submitted. Formulario ya poblado con los datos a editar (antes de enviar/guardar)
        form = NuevoPost(instance=post)

    else:
        # Data submitted. Formulario para guardar con los datos enviados por POST
        form = NuevoPost(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:Posts')

    context = {
        'title': 'Edit',
        'subtitle': post.title,
        'form': form,
        'avatar': avatar,
    }
    return render(request, 'blog/edit_post.html', context)

@login_required
def agregar_post(request):
    """View to add new posts."""

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    if request.method != 'POST':
        # No data submited. Paso formulario vacio
        form = NuevoPost()
    
    else:
        # Data submitted. Paso formulario con datos ingresados por POST
        form = NuevoPost(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
           
            return redirect('blog:Posts')

    context = {
        'form': form, 
        'title': 'Nuevo Post',
        'avatar': avatar,
    }
    return render(request, 'blog/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """Edit an existing post."""

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    # Post que se va a editar
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        # No data submitted. Formulario ya poblado con los datos a editar (antes de enviar/guardar)
        form = NuevoPost(instance=post)

    else:
        # Data submitted. Formulario para guardar con los datos enviados por POST
        form = NuevoPost(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:Posts')

    context = {
        'title': 'Edit',
        'subtitle': post.title,
        'form': form,
        'avatar': avatar,
    }
    return render(request, 'blog/edit_post.html', context)

@login_required
def post_detail(request, post_id):
    """Display full post."""
    
    # Post que se va a mostrar
    post = Post.objects.get(id=post_id)

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''
    
    context = {
        'title': 'Detail',
        'subtitle': post.title,
        'avatar': avatar,
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/pages/'


def about(request):
    """About context."""

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    context = {
        'avatar': avatar,
        'title': 'About',
        'message': 'Bienvenidos a compara tu lava',
        'subtitle': 'About'
        }
    return render(request, 'blog/about.html', context)