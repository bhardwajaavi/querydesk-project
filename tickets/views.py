from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import QueryTicket, Profile
from .forms import ProfileForm, CustomUserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# --- Main Page Views ---

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

# --- Auth Views ---

def register_view(request):
    if request.method == 'POST':
        # Use our new, custom form
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        # Use our new, custom form
        form = CustomUserCreationForm()
    
    # This is the correct path to your template
    return render(request, 'register.html', {'form': form})

def custom_logout_view(request):
    logout(request)
    return redirect('home')

# --- User Dashboard Views ---

@login_required
def dashboard_view(request):
    profile = request.user.profile
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)

    query_count = QueryTicket.objects.filter(submitted_by=request.user).count()

    context = {
        'form': form,
        'query_count': query_count
    }
    return render(request, 'user_dashboard.html', context)


@login_required
def my_queries_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        if subject and description:
            QueryTicket.objects.create(
                submitted_by=request.user,
                subject=subject,
                description=description
            )
            return redirect('my-queries')

    my_queries = QueryTicket.objects.filter(submitted_by=request.user).order_by('-created_at')
    
    return render(request, 'my_queries.html', {'queries': my_queries})