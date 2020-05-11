from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class req(models.Model):
	ReqType = models.TextChoices('ReqType', 'Plumbing Electrical Painting Cleaning')
	RequestType = models.CharField(blank=True, choices=ReqType.choices, max_length=15)
	RequestDescription = models.TextField()
	city = models.CharField(max_length=20)
	State = models.TextChoices('State', 'Andhra-Pradesh Arunachal-Pradesh Assam Bihar Chandigarh Chhattisgarh Daman-and-Diu Delhi Goa Gujarat Haryana Himachal-Pradesh Jammu-and-Kashmir Jharkhand Karnataka Kerala Madhya-Pradesh Maharashtra Manipur Meghalaya Mizoram Nagaland Odisha Punjab Rajasthan Sikkim Tamil-Nadu Telangana Tripura Uttar-Pradesh Uttarakhand West-Bengal')
	state = models.CharField(blank=True, choices=State.choices, max_length=20)
	pincode = models.CharField(max_length=6, blank= True)
	CoutryCode = models.CharField(max_length=4)
	SecodaryNumber = models.CharField(max_length=10)
	Status = models.TextChoices('Status', 'Pending In-Progress Completed')
	status = models.CharField(blank=True, choices=Status.choices, max_length=15, default=Status.Pending)
	date_posted=models.DateTimeField(default=timezone.now)
	remarks = models.TextField()
	updatedby = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.reqdesc

	def get_absolute_url(self):
		return reverse('ticket-detail', kwargs = {'pk': self.pk})