from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.views.decorators.csrf import csrf_exempt
def index(request):
	return render(request,'index.html', {})
def register(request):
	return render(request,'register.html', {})



@csrf_exempt

def OrgSave(request):
	if request.method=='POST':
		f=request.POST.get("Fullname")
		e=request.POST.get("Email")
		p=request.POST.get("Password")
		#OrganizerData.objects.all().delete()
		#to generate the ID
		c="ORG00"
		x=1
		cid=c+str(x)
		while OrganizerData.objects.filter(Org_ID=cid).exists():
			x=x+1 #2
			cid=c+str(x)
		x=int(x)
		#Generate OTP
		otp=uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.today())+cid+f+e+p).int
		otp=str(otp)
		otp=otp.upper()[0:6]
		request.session['OTP']=otp#Make Session
		if OrganizerData.objects.filter(Org_Email=e).exists():
			dic={'msg':'Already Exists'}
			return render(request, 'register.html',dic)
		else:
			OrganizerData(
				Org_ID=cid,
				Org_Name=f,
				Org_Email=e,
				Org_Password=p,
				).save()
			sub='QuizAPP OTP'
			msg='''Your OTP is '''+otp+''',

Thanks!'''
			email=EmailMessage(sub,msg,to=[e])
			email.send()
			msg="Registered Success! Now Verify Your Email"
			dic={'msg':msg,'id':cid}#JSON
			return render(request, 'verified.html',dic)

def verified(request):
	return render(request,'verified.html', {})
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
			dic={'id':orgid,'msg':'Incorrect OTP'}
			return render(request, 'verified.html',dic)