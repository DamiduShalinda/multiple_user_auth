# Generated by Django 4.2.3 on 2023-07-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_staff_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='branch',
            field=models.CharField(choices=[('branch3', 'branch3'), ('branch1', 'branch1'), ('branch2', 'branch2')], default='branch1', max_length=100),
        ),
    ]