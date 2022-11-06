from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, ListView
from .models import addReport
from .forms import PostForms
from django.views.generic.edit import CreateView
from django.contrib import messages #import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])

            if user is not None:
                login(request, user)

                return HttpResponse("You are authenticated")

            else:
                return HttpResponse("Invalid login")

    else:
        form = LoginForm()

        return render(request, 'login.html', {'form': form})



class CreateProduct(CreateView, SuccessMessageMixin):
    model = addReport
    template_name = 'home.html'
    form_class = PostForms
    success_url = "."
    success_message = "Votre raport a ete enregistrer"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super().form_valid(form)

@login_required
def article_form(request):
    if request.method == 'POST':
        article_form = PostForms(request.POST)

        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.utilisateur = request.user
            article.save()
            return redirect('home')
    else:
        article_form = PostForms()
    return render(request,'home.html',{'article_form':article_form})