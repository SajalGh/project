# Generated by Django 2.2 on 2020-02-11 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('M1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('Gender', models.CharField(default='', max_length=20)),
                ('email_address', models.CharField(default='', max_length=500)),
                ('Age', models.CharField(default='', max_length=100)),
                ('Address', models.CharField(default='', max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]