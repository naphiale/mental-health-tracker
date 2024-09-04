from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306224556',
        'name': 'Nafia Levana Aulia',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)