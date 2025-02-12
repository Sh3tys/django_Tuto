from datetime import datetime
from django.shortcuts import render # type: ignore


def index(request):
    date = datetime.today()
    return render(request, "TutoDjango/index.html", context={"date" : date})