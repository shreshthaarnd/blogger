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

class BlogData(models.Model):
	Blog_ID=models.CharField(max_length=20, primary_key=True)
	User_ID=models.CharField(max_length=20)
	Blog_Title=models.CharField(max_length=100)
	Blog_Category=models.CharField(max_length=100)
	Blog_Body=models.CharField(max_length=2000)
	Blog_Image=models.FileField(upload_to='blogimages/')
	class Meta:
		db_table="BlogData"