from django.db import models
# Organizer DAta
class UserData(models.Model):
	User_ID=models.CharField(max_length=20, primary_key=True)
	User_Name=models.CharField(max_length=100)
	User_Email=models.CharField(max_length=100)
	User_Password=models.CharField(max_length=20)
	Status=models.CharField(max_length=10, default='Deactive')
	class Meta:
		db_table="UserData"
