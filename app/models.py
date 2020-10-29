from django.db import models
# Organizer DAta
class UserData(models.Model):
	Usr_ID=models.CharField(max_length=20, primary_key=True)
	Usr_Name=models.CharField(max_length=100)
	Usr_Ins=models.CharField(max_length=200, default='None')
	Usr_Email=models.CharField(max_length=80,blank=True)
	Usr_Email=models.CharField(max_length=80, blank=True)
	Usr_Password=models.CharField(max_length=20)
	Status=models.CharField(max_length=10, default='Deactive')
	class Meta:
		db_table="UserData"
