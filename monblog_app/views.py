from django.shortcuts import render, get_object_or_404
from .models import Article

# Page d'accueil : liste de tous les articles
def liste_articles(request):
    articles = Article.objects.all().order_by('-date_creation')
    return render(request, 'liste.html', {'articles': articles})

# Page d'un article individuel
def detail_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'detail.html', {'article': article})
from django.core.mail import send_mail
from django.shortcuts import redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                nom=form.cleaned_data['nom'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
            )
            return redirect('confirmation')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def confirmation(request):
    return render(request, 'confirmation.html')
