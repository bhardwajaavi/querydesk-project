from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import QueryTicket, Profile
from .forms import ProfileForm, CustomUserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# --- QUICK FIX: USER CREATION HACK ---
# This code runs on server startup to ensure the user exists.
# DELETE THIS FUNCTIONALITY AFTER YOU LOG IN SUCCESSFULLY!
try:
    if not User.objects.filter(username='bhardwajaneesh').exists():
        User.objects.create_user(
            username='bhardwajaneesh',
            email='test@gmail.com',
            password='Anee1234@'
        )
        print("TEMPORARY USER CREATED: bhardwajaneesh")
    else:
        print("TEMPORARY USER EXISTS: bhardwajaneesh")
except Exception as e:
    # This prevents the whole server from crashing if the database is not ready
    print(f"Error during quick-fix user creation: {e}")
# --- END QUICK FIX ---

# --- Main Page Views ---

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

# --- Auth Views ---

def register_view(request):
    # This registration form logic is now irrelevant as the user exists.
    # It remains here to avoid crashes, but the user is already created.
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    
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


### Final Steps: Pushing and Logging In

'''1.  **Replace** the code in your `tickets/views.py` file with the code above.
2.  **Save** the file.
3.  Go to your terminal and **push** this final change to GitHub:
    ```bash
    git add .
    git commit -m "Final quickfix: Inject test user via views.py"
    git push origin main
    ```
4.  **Render** will redeploy. Wait for it to say "Deploy live."
5.  Go to your login page on the live site and use these credentials:
    * **Username:** `bhardwajaneesh`
    * **Password:** `Anee1234@`

This will allow you to log in instantly. Once you are logged in, **you must delete the user creation code** in `views.py` and push the changes for security.'''