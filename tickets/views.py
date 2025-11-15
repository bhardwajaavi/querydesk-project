from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import QueryTicket, Profile
from .forms import ProfileForm

# --- Main Page Views ---

def home_view(request):
    # This is your Redtape-inspired homepage
    return render(request, 'home.html')

def about_view(request):
    # This is your "About Us" page
    return render(request, 'about.html')

# --- Auth Views ---

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Profile is created automatically by the signal in models.py
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def custom_logout_view(request):
    logout(request)
    return redirect('home')

# --- User Dashboard Views ---

@login_required
def dashboard_view(request):
    # This is the NEW "My Dashboard" (Profile Page)
    profile = request.user.profile
    
    if request.method == 'POST':
        # This handles UPDATING the profile
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard') # Redirect back to the same page
    else:
        # This shows the form with existing details
        form = ProfileForm(instance=profile)

    # Get the query count
    query_count = QueryTicket.objects.filter(submitted_by=request.user).count()

    context = {
        'form': form,
        'query_count': query_count
    }
    return render(request, 'user_dashboard.html', context)


@login_required
def my_queries_view(request):
    # This is the OLD dashboard (Query List & Submission)
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