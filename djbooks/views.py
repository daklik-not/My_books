from doctest import SKIP
from faulthandler import disable
from http.client import HTTPResponse
from tkinter import DISABLED
from unicodedata import name
from unittest import result, skip
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, Book, Publisher, UsersLink
from django.http import HttpResponseRedirect
from .forms import PublisherForm, AuthorForm, UsersLinkForm, Userform
from django.urls import is_valid_path, reverse
from django.views import View
from django.contrib.auth.models import User

def home(request):
    publisher_queryset = Publisher.objects.all()
    if 'msg' in request.session.keys():
        msg = request.session['msg']
        request.session['msg'] = ''
    else:
        msg = ''
    return render(request, 'djbooks/home.html', {'publisher_queryset': publisher_queryset, 'msg': msg})


def publisher(request, pub_id):
    pub_inf = Publisher.objects.get(id=pub_id)
    return render(request, 'djbooks/publisher.html', {'pub_inf': pub_inf})


def book(request, book_id):
    book_queryset = Book.objects.get(id=book_id)
    return render(request, 'djbooks/book.html', {'book_query': book_queryset})


def book_list(request):
    book_queryset = Book.objects.order_by('title')
    return render(request, 'djbooks/books.html', {'book_queryset': book_queryset})





def get_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            publisher = Publisher(name=form.cleaned_data['name'], address=form.cleaned_data['address'], city=form.cleaned_data['city'],
                                  country=form.cleaned_data['country'], website=form.cleaned_data['website'])  # тут ошибка была - не cleaned_data.name, а cleaned_data['name']
            publisher.save()
            request.session['msg'] = f"New publisher {form.cleaned_data['name']} has been added. Congratulations!"
            return redirect("home")
    else:
        form = PublisherForm()

    # тут ошибка - в адресе не было djbooks/
    return render(request, 'djbooks/addpublisher.html', {'form': form})


def get_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['msg'] = f"New author {form.cleaned_data['salutation']} {form.cleaned_data['name']} has been added."
            return redirect('authors')
    else:
        form = AuthorForm()

    return render(request, 'djbooks/addauthor.html', {'form': form})

class Link(View):
    template_name = 'djbooks/links.html'
    initial = {'url': 'http://'}
    form_class = UsersLinkForm
    
    

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        links_queryset = UsersLink.objects.all()
        return render(request, self.template_name, {'form': form,'links_queryset': links_queryset})

    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('links')
        else:
            form = self.form_class()
        return render(request, self.template_name, {'form': form})


class NewAuthor(View):
    template_name = 'djbooks/authors.html'
    initial = {'key': 'value'}
    form_class = AuthorForm
    
    
    def get(self, request, *args, **kwargs ):
        form = self.form_class()
        authors_queryset = Author.objects.order_by('name')
        if 'msg' in request.session.keys():
            msg = request.session['msg']
            request.session['msg'] = ''
        else:
            msg = ''
        return render(request, self.template_name, {'authors_queryset': authors_queryset, 'msg': msg, 'form': form})

    def post(self, request, *args, **kwargs ):
        form= self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
        return render(request, self.template_name, {'form': form} )


class EditAuthor(View):
    template_name ="djbooks/editauthor.html"
    form_class = AuthorForm

    def get(self, request, author_id, *args, **kwargs):
        author = Author.objects.get(pk=author_id)
        f = self.form_class(instance=author)

        return render(request, self.template_name, {"f": f})
        
    def post(self, request, author_id,  *args, **kwargs):
        f = self.form_class(request.POST, instance=Author.objects.get(pk=author_id))
        if f.is_valid():
            f.save()
            return redirect('authors')
        return render(request, self.template_name, {"f":f})

def delete_author(request, author_id):
    Author.objects.get(pk=author_id).delete()
    return redirect('authors')


class ProfileView(View):
    template_name="djbooks/profile.html"
    form_class = Userform
    def get(self,  request,*args, **kwargs):
        user = User.objects.get(username=request.user.username)
        f=self.form_class(instance=user) 
        return render(request, self.template_name, {"user":user,"f":f})

    def post(self, request,*args, **kwargs):
        pass
    





