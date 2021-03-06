# Generated by Django 3.2.4 on 2021-12-14 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='team')),
                ('social_facebook', models.CharField(blank=True, max_length=200, null=True)),
                ('social_twitter', models.CharField(blank=True, max_length=200, null=True)),
                ('social_instagram', models.CharField(blank=True, max_length=200, null=True)),
                ('social_linkedin', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
