# Generated by Django 3.1.5 on 2021-03-10 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccountHolder', models.CharField(max_length=25)),
                ('AccountNumber', models.BigIntegerField()),
                ('MobileNumber', models.BigIntegerField()),
                ('Address', models.TextField()),
                ('IssueType', models.CharField(max_length=8)),
                ('Issue', models.TextField()),
                ('PostalZip', models.CharField(max_length=6)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'ContactUs',
            },
        ),
    ]