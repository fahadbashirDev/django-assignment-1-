import os
import joblib

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import SignUpForm, LoginForm, PostForm, ContactForm
from .models import Post, ContactMessage

# ---------- Load the trained ML model once when the server starts ----------
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'ml', 'iris_model.pkl')
_model_bundle = None
if os.path.exists(MODEL_PATH):
    _model_bundle = joblib.load(MODEL_PATH)


# ---------------------------- Home / Posts ----------------------------
def home(request):
    """Home page: shows the post form (if logged in) and all posts."""
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Please log in to create a post.')
            return redirect('login')
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post published!')
            return redirect('home')
    else:
        form = PostForm()

    posts = Post.objects.select_related('author').all()
    return render(request, 'core/home.html', {'form': form, 'posts': posts})


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated.')
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'core/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted.')
        return redirect('home')
    return render(request, 'core/confirm_delete.html', {'post': post})


# ---------------------------- Auth: Sign Up / Login / Logout ----------------------------
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


# ---------------------------- Contact Us ----------------------------
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks! Your message has been received.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})


# ---------------------------- Machine Learning ----------------------------
def ml_predict_view(request):
    """Takes 4 flower measurements from the user and returns a real
    prediction from the trained RandomForest Iris classifier."""
    prediction = None
    error = None

    if request.method == 'POST':
        try:
            sepal_length = float(request.POST.get('sepal_length'))
            sepal_width = float(request.POST.get('sepal_width'))
            petal_length = float(request.POST.get('petal_length'))
            petal_width = float(request.POST.get('petal_width'))

            if _model_bundle is None:
                error = 'Model not found. Please run core/ml/train_model.py first.'
            else:
                model = _model_bundle['model']
                target_names = _model_bundle['target_names']
                features = [[sepal_length, sepal_width, petal_length, petal_width]]
                pred_index = model.predict(features)[0]
                prediction = target_names[pred_index].capitalize()
        except (TypeError, ValueError):
            error = 'Please enter valid numeric values for all fields.'

    return render(request, 'core/ml_predict.html', {
        'prediction': prediction,
        'error': error,
    })
