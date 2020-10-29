from django.shortcuts import render


def index(request):
	return render(request,'index.html', {})
def archive(request):
	return render(request,'archive.html',{})
def blog(request):
	return render(request,'blog.html',{})
def category(request):
	return render(request,'category.html',{})
def contact(request):
	return render(request,'contact.html',{})
def element(request):
	return render(request,'element.html',{})
def single_blog(request):
	return render(request,'single-blog.html',{})
