from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm
from .models import Feedback
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_superuser

@login_required
def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Save the form without committing to the database yet
            feedback = form.save(commit=False)
            # Assign the currently logged-in user to the feedback
            feedback.user = request.user
            feedback.save()  # Now save to the database
            messages.success(request, 'Thank you for your feedback!')
            return redirect('feedback:submit_feedback')  # Change this to your desired redirect URL
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback/submit_feedback.html', {'form': form})

def view_feedback(request):
    if request.user.is_superuser:
        feedback_list = Feedback.objects.all().order_by('-submitted_at')
    else: 
        feedback_list = Feedback.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'feedback/view_feedback.html', {'feedback_list': feedback_list})