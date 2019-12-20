from django.db import models

class Member(models.Model):
	name = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 200)
	phone = models.CharField(max_length = 200)
	age = models.CharField(max_length = 200 , blank=True)
	gender = models.CharField(max_length=1 , choices = (( 'M', 'Male') , ('F', 'Female')), default='M')
	comment = models.TextField(default='' , blank=True)

	def __str__(self):
		return self.name

	
		
