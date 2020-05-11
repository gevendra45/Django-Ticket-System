from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			#print("hi i am in POST")
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Your account has been created Please use Credentials to login!!!')
			return redirect('login')
		#else:
		#	messages.warning(request, 'You didnt fulfilled the criteia for creating the user!!!')
		#	return redirect('register')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	return render(request, 'users/profile.html')
	