from django.shortcuts import render


def handler404(request, exception=None, template_name='404.html'):
    return render(request, template_name, status='404')
