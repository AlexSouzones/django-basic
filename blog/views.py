from django.shortcuts import render


def blog(request):
    context = {"text": "Olá blog",
               "title": "Blog "}
    return render(request, "blog/index.html", context=context)


def exemplo(request):
    context = {"text": "Olá exemplo",
               "title": "Blog Exemplo"}
    return render(request, "blog/exemplo.html", context=context)


# Create your views here.
