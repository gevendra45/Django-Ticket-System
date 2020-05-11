from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import req

def thome(request):
	context={
		'ticket': req.objects.all()
	}
	return render(request, 'ticketapp/thome.html', context, {'title' : 'Ticket Home'})

def tabout(request):
	return render(request, 'ticketapp/about.html', {'title' : 'Ticket Raise About'})

class TicketListView(ListView):
	model = req
	template_name = 'ticketapp/thome.html'
	context_object_name = 'ticket'#context_object_name = 'posts'
	ordering=['id']

class TicketDetailView(DetailView):
	model = req
	#fields = ['id', 'req', 'reqdesc', 'date_posted', 'status']

class TicketCreateView(LoginRequiredMixin, CreateView):
	model = req
	fields = ['RequestType', 'RequestDescription', 'city', 'state', 'pincode', 'CoutryCode', 'SecodaryNumber']

	def form_valid(self, form):
		form.instance.updatedby = self.request.user
		return super().form_valid(form)

class TicketUpdateView(LoginRequiredMixin, UpdateView):
	model = req
	fields = ['RequestType', 'RequestDescription', 'city', 'state', 'pincode', 'CoutryCode', 'SecodaryNumber', 'remarks']

	def form_valid(self, form):
		form.instance.updatedby = self.request.user
		return super().form_valid(form)

	def test_func(self):
		req = self.get_object()
		if self.request.user == req.updatedby:
			return True
		return False

def newpost(request):
	return render(request, 'ticketapp/newticket.html', {'title' : 'Ticket Raise About'})