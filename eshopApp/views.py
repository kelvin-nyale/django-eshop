# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect #get_object_or_404
from django.contrib import messages
# from eshopApp.models import Products, Services, Categories
from django.contrib.auth.hashers import make_password
from .models import Users
from django.contrib.auth import authenticate, login #as auth_login



# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if user with this email already exists
        if Users.objects.filter(username=username).exists():
            messages.error(request, "User with this username already exists")
            return redirect('register')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # Create new user
        user = Users.objects.create(
            username=username,
            email=email,
            role=role,
            password=make_password(password)
        )
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')

    return render(request, 'register.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         # Authenticate user
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             # Login user
#             login(request, user)
#             messages.success(request, "Login successful!")
#             return redirect('dashboard')

#     return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f'{username} {password}')
        # Validate username and password input
        if not username or not password:
            messages.error(request, "Both email and password are required.")
            return redirect('login')
        print(">>>>>>>>>>>>Username and password validation complete")
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print(">>>>>Trying to log user")
            login(request, user)  # Log the user in
            print(">>>>>>>Checking role for redirections")
#             # Redirect based on user role
            if hasattr(user, 'role'):
                if user.role == 'admin':
                    messages.success(request, "Welcome back, Admin!")
                    return redirect('admin_dashboard')
                elif user.role == 'seller':
                    messages.success(request, "Welcome back, Seller!")
                    return redirect('seller_dashboard')
                elif user.role == 'user':
                    print("user role hit======awaiting redirect")
                    messages.success(request, "Welcome back, User!")
                    print(">>>>>redirect reached")
                    return redirect('user_dashboard')

            # Default fallback if no specific role logic is set
            messages.success(request, "Login successful!")
            return redirect('user_dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')