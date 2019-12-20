from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
	
	age = forms.CharField(required=False)
	comment = forms.CharField(required=False , widget=forms.Textarea)

	class Meta:
		model = Member
		fields = '__all__'

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['name'].widget.attrs.update({'class':'form-control'})
		self.fields['email'].widget.attrs.update({'class':'form-control'})
		self.fields['phone'].widget.attrs.update({'class':'form-control'})
		self.fields['age'].widget.attrs.update({'class':'form-control'})
		self.fields['gender'].widget.attrs.update({'class':'custom-select'})
		self.fields['comment'].widget.attrs.update({'class':'form-control'})