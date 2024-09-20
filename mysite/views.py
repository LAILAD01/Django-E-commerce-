from django.contrib import messages
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.conf import settings
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
# Create your views here.
def home(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        # ... other context data ...
    }
    return render(request, 'Home.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'Shop.html',{'products':products})

def blog(request):
    return render(request, 'Blog.html')

def about(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'Contact.html')

def cart(request):
    # Assuming you have a Cart model with a related product field and quantity
    cart_items = Cart.objects.filter(user=request.user)  # Adjust this query based on your Cart model structure
    
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'Cart.html', context)

def checkout(request):
    # your view logic here
    return render(request, 'checkout.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})
    
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                try:
                    login(request, user)
                    return redirect('home')  # Redirect to your home page
                except Exception as e:
                    messages.error(request, f"An error occurred: {str(e)}")
            else:
                messages.error(request, "Invalid login credentials.")
        else:
            messages.error(request, "Form is not valid. Please check your inputs.")
    else:
        form = LoginForm()
    return render(request, 'Login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print('User created successfully')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("User logged in successfully")
                return redirect('home')  # Redirect to your home page
        else:
            print("Form is not valid")
    else:
        form = SignUpForm()
    return render(request, 'Signup.html', {'form': form})