# Generated by Django 3.1.2 on 2020-10-31 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('User_ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('User_Name', models.CharField(max_length=100)),
                ('User_Email', models.CharField(max_length=100)),
                ('User_Password', models.CharField(max_length=20)),
                ('Status', models.CharField(default='Deactive', max_length=10)),
            ],
            options={
                'db_table': 'UserData',
            },
        ),
    ]
