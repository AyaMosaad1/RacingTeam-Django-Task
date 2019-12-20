from django.shortcuts import render

from .forms import MemberForm

def index(request):
	if request.method == 'POST':
		form = MemberForm(request.POST)
		if form.is_valid():
			form.save()
	
	form = MemberForm()
	return render(request,'index.html', {'form' : form})