from django.shortcuts import render
from django.http import JsonResponse
from .forms import SignupForm
from .tasks import send_welcome_email

def user_signup(request):
    if request.method == 'POST':
        # Bind the form to the POST data
        form = SignupForm(request.POST)
        
        if form.is_valid():
            # Extract the email from the form
            user_email = form.cleaned_data['email']

            # Call the Celery task asynchronously
            send_welcome_email.delay(user_email)

            # Respond with a success message
            return JsonResponse({"message": f"Welcome email task has been queued for {user_email}."})
        else:
            # If form is invalid, return errors
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        # If the request method is GET, show the empty form
        form = SignupForm()

    # Render the form template
    return render(request, 'signup.html', {'form': form})
