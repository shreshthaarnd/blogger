from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.views.decorators.csrf import csrf_exempt
import uuid
def index(request):
	return render(request,'index.html', {})
def register(request):
	return render(request,'register.html', {})
def register1(request):
	return render(request,'register1.html', {})
def archive(request):
	return render(request,'achive.html', {})
def blog(request):
	return render(request,'blog.html', {})
def	category(request):
	return render(request,'category.html', {})
def	contact(request):
	return render(request,'contact.html', {})
def	element(request):
	return render(request,'element.html', {})
def single_blog(request):
	return render(request,'single_blog.html', {})
def	login(request):
	return render(request,'login.html', {})
@csrf_exempt
def usersave(request):
	if request.method=='POST':
		name=request.POST.get("name")
		email=request.POST.get("email")
		password=request.POST.get("password")
		u="U00"
		x=1
		cid=c+str(x)
		while UserData.objects.filter(User_ID=usrid).exists():
			x=x+1
			useid=c+str(x)
		x=int(x)
		otp=uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.today())+cid+name+email+password).int
		otp=str(otp)
		otp=otp.upper()[0:6]
		request.session['OTP']=otp
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
			return render(request, 'verified.html', dic)



@csrf_exempt
def usersave_trial(request):
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
			return render(request, 'verified.html', dic)

def verified(request):
	return render(request,'verified.html', {})
def verified1(request):
	return render(request,'verified1.html', {})

@csrf_exempt
def verify_user(request):
	if request.method=='POST':
		uotp=request.POST.get('otp')
		orgid=request.POST.get('id')
		sotp=request.session['OTP']
		if uotp==sotp:
			OrganizerData.objects.filter(Org_ID=orgid).update(Status='Active')
			request.session['org_id'] = orgid
			return redirect('/index/')
		else:
			dic={'id':usrid,'msg':'Incorrect OTP'}
			return render(request, 'verified.html',dic)