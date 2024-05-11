from django.contrib.auth import logout
from django.core.mail import message
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import TagForm, QuoteForm, AuthorForm
from .models import Tag, Author, Quotes
from django.contrib.auth.decorators import login_required


def logout_view(request):
    message.info(request, 'You have logout')
    logout(request)
    return redirect('/')

def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes/author_info.html', {'author': author})

def main(request, page=1):
    #db = get_mongodb()
    #quotes = db.quotes.find()
    #quotes = Quotes.objects.order_by('id')[:5]

    quotes = Quotes.objects.filter(user=request.user).all() if request.user.is_authenticated else []
    #return render(request, 'noteapp/index.html', {"notes": notes})
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)


    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_author.html', {'form': form})

    return render(request, 'quotes/add_author.html', {'form': AuthorForm()})

@login_required
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            #form.save()
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/tag.html', {'form': form})

    return render(request, 'quotes/tag.html', {'form': TagForm()})

@login_required
def add_quote(request):
    tags = Tag.objects.filter(user=request.user).all()
    auths = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
            new_note = form.save(commit=False)
            new_note.user = request.user
            new_note.save()
=======
            new_note = form.save()
>>>>>>> 1211100f671db9290fb9a536d2722fa708423fae
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_note.tags.add(tag)

            au = Author.objects.get(fullname=request.POST.get('author'))
<<<<<<< HEAD

            # создание товара определенной компании

            au.quotes_set.add(new_note, bulk=False)
            #author = get_object_or_404(Author, fullname=request.POST.get('author'))
            #new_note.author = author
=======
            au.quotes_set.add(new_note, bulk=False)
>>>>>>> 1211100f671db9290fb9a536d2722fa708423fae

            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/note.html', {"tags": tags, "authors": auths, 'form': form})

    return render(request, 'quotes/note.html', {"tags": tags, "authors": auths, 'form': QuoteForm()})
