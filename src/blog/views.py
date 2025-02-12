from django.shortcuts import render # type: ignore

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def article(request, numero_article):
    if numero_article in ["01", "02", "03"]:
        return render(request, f"blog/article_{numero_article}.html", context={})
    return render(request, "blog/404.html") # type: ignore