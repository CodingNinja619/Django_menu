from django.shortcuts import render

def page_view(request, page_slug):
    return render(request, f"{page_slug}.html")