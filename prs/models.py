from django.db import models
from model_utils.models import TimeStampedModel

class PullRequest(TimeStampedModel):
	branchSource 				= models.CharField(max_length=50, null=False, blank=True)
	branchDestiny 				= models.CharField(max_length=50, null=False, blank=True)
	author 				= models.CharField(max_length=50, null=False, blank=True)
	title 				= models.CharField(max_length=50, null=False, blank=True)
	description 				= models.TextField(max_length=5000, null=False, blank=True)
	status 				= models.CharField(max_length=50, null=False, blank=True)
	date_create 		= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_merge 		= models.DateTimeField(auto_now=True, verbose_name="date updated")

	def __str__(self):
		return self.title