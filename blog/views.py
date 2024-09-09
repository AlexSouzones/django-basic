from django.shortcuts import render
from blog.data import posts


def blog(request):
    context = {
        # "text": "Olá blog",
        "posts": posts
    }
    return render(request, "blog/index.html", context=context)


def post(request, post_id):
    found_post = None

    for post in posts:
        if post["id"] == post_id:
            found_post = post
            break
        
    context = {
        # "text": "Olá blog",
        "posts": [found_post]
    }
    return render(request, "blog/index.html", context=context)


def exemplo(request):
    context = {"text": "Olá exemplo"}
    return render(request, "blog/exemplo.html", context=context)


# Create your views here.
