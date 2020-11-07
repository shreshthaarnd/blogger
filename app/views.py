from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import *
from django.views.decorators.csrf import csrf_exempt
import uuid
import datetime
from django.core.mail import EmailMessage

def checksession(request):
	try:
		uid=request.session['user_id']
		return True
	except:
		return False

def index(request):
	dic={'checksession':checksession(request)}
	return render(request,'index.html', dic)
def archive(request):
	return render(request,'achive.html', {})
def blog(request):
	dic={'checksession':checksession(request),
		'data':BlogData.objects.all(),
		'users':UserData.objects.all()}
	return render(request,'blog.html', dic)
def logout(request):
	del request.session['user_id']
	return redirect('/index/')
def	category(request):
	return render(request,'category.html', {})
def	contact(request):
	return render(request,'contact.html', {})
def	element(request):
	return render(request,'element.html', {})
def single_blog(request):
	return render(request,'single-blog.html', {})

@csrf_exempt
def usersave(request):
	if request.method=='POST':
		name=request.POST.get("name")
		email=request.POST.get("email")
		password=request.POST.get("password")
		c="U00"
		x=1
		cid=c+str(x)
		while UserData.objects.filter(User_ID=cid).exists():
			x=x+1 #2
			cid=c+str(x)
		x=int(x)

		#Generate OTP
		otp=uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.today())+cid+name+email+password).int
		otp=str(otp)
		otp=otp.upper()[0:6]
		request.session['OTP']=otp#Make Session

		if UserData.objects.filter(User_Email=email).exists():
			dic={'msg':'User Already Exists'}
			return render(request, 'register.html',dic)
		else:
			UserData(User_ID=cid, User_Name=name, User_Email=email, User_Password=password).save()
			sub='Blogger OTP'
			msg='''Your OTP is '''+otp+''',

Thanks!'''
			email=EmailMessage(sub,msg,to=[email])
			email.send()

			msg="Registered Success! Now Verify Your Email"
			dic={'msg':msg,'id':cid}#JSON
			return render(request, 'verify.html', dic)

@csrf_exempt
def verify_user(request):
	if request.method=='POST':
		uotp=request.POST.get('otp')
		userid=request.POST.get('id')
		sotp=request.session['OTP']
		if uotp==sotp:
			UserData.objects.filter(User_ID=userid).update(Status='Active')
			request.session['user_id'] = userid
			return redirect('/index/')
		else:
			dic={'id':usrid,'msg':'Incorrect OTP'}
			return render(request, 'verify.html',dic)
def register(request):
	return render(request,'register.html',{})
def login(request):
	return render(request,'login.html',{})
@csrf_exempt
def checklogin(request):
	if request.method=='POST':
		email=request.POST.get('email')
		password=request.POST.get('password')
		if UserData.objects.filter(User_Email=email,User_Password=password).exists():
			request.session['user_id']=UserData.objects.filter(User_Email=email)[0].User_ID
			return redirect('/index/')
		else:
			dic={'msg':'Incorrect Email or Password'}
			return render(request,'login.html',dic)
def verify(request):
	return render(request,'verify.html',{})
def postblog(request):
	return render(request,'postblog.html',{})

@csrf_exempt
def blogsave(request):
	if request.method=='POST':
		title=request.POST.get("title")
		category=request.POST.get("category")
		body=request.POST.get("body")
		image=request.FILES['image']
		c="B00"
		x=1
		cid=c+str(x)
		while BlogData.objects.filter(Blog_ID=cid).exists():
			x=x+1 #2
			cid=c+str(x)
		x=int(x)
		BlogData(
			Blog_ID=cid,
			User_ID=request.session['user_id'],
			Blog_Title=title,
			Blog_Body=body,
			Blog_Image=image
			).save()
		dic={'msg':'Blog Posted Successfully'}
		return render(request, 'postblog.html', dic)