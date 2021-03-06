# Generated by Django 2.1 on 2019-01-13 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('post', models.CharField(choices=[('1st', 'GENERAL SECRETARY'), ('2nd', 'FINANCIAL SECRETARY'), ('3rd', 'JOINT SECRETARY')], default='3rd', max_length=50)),
                ('Image', models.ImageField(upload_to='team')),
                ('fb_link', models.URLField(blank=True, max_length=50, null=True)),
                ('git_link', models.URLField(blank=True, max_length=50, null=True)),
                ('linked_in_link', models.URLField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
