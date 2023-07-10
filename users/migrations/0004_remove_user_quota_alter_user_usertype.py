# Generated by Django 4.2.3 on 2023-07-10 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='quota',
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('manager', 'manager'), ('staff', 'staff'), ('customer', 'customer')], default='customer', max_length=10),
        ),
    ]