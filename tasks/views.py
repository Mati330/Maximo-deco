
from django.shortcuts import render, redirect
# cuando ejecuta devuelve un formulario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# Create your views here.
"""
def helloworld(request):
    title = 'helloworld'
    return render(request, 'index.html', {'mytitle': title
    })
Vemos que dentro de esto, se va renderizar un html, y tenemos una variable,
llamada title, que dentro del html podemos llamarla como 'mytitle'.
"""
## BASE HTML CONTENT ##
def base(request):
    logo = Logo.objects.all
    return render(request, 'base.html', 
                  {'logo': logo})
## HTMLS TEMPLATES ## 
def home(request):
    product = Product.objects.all
    return render(request, 'index.html', 
                  {"product": product})
###################### LOGS HTML #####################
def signup(request):
    # aca indicamos, si entra por POST realiza el envio de datos para la bd
    if request.method == 'POST':
        # Si password1 es igual a password2 entonces intentamos guardar
        if request.POST['password1'] == request.POST['password2']:
            # Hacemos un try except para que la app no rompa todo la pagina en el caso de error, porque al generar dos ->
            # Usuarios  iguales podes tener error 'unique' que se genera cuando creas dos usuarios iguales y no es posible eso en la db
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                # Crea   la cokie de login, para que el navegador sepa que estas logeado
                user.save()
                login(request, user)
                return redirect('index')  # Redirect to home page

            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Failed to signup username'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'password does not match'
        })

    else:  # Aca indicamos que si entra por GET nos haga el render de form
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })

def signout(request):
    logout(request)
    return redirect('index')

def signin(request):
    # Si entramos por GET, mandamos a la persona al form
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })

    else:
        # Si entramos por POST, tomamos los datos del form, usuario+pasword e igualamos, vemos que sean correctos.
        user = authenticate(request, username=request.POST.get(
            'username'), password=request.POST.get('password'))
        if user is None:
            # Si no son correctos lo mandamos a la vista de logeo.
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Invalid username or password'
            })

        else:
            # Si son correctos, guarda su sesion, en cokies, y direccionalo al home.
            login(request, user)
            return redirect('index')
################### FUNCIONALIDADES ####################
def cart(request):
    return render(request, 'cart.html')
def checkout(request):
    return render(request, 'checkout.html')
def product(request):
    return render(request, 'product-details.html')
@login_required
def shop(request):
    product = Product.objects.all
    return render(request, 'shop.html', {"product": product})


