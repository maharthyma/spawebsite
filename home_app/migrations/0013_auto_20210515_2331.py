# Generated by Django 3.2.2 on 2021-05-15 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0012_about_2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SocialMedia',
        ),
        migrations.AddField(
            model_name='contactus',
            name='Facebook',
            field=models.URLField(default='https://www.facebook.com/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='Instagram',
            field=models.URLField(default='https://www.facebook.com/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='Twitter',
            field=models.URLField(default='https://www.facebook.com/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='Youtube',
            field=models.URLField(default='https://www.facebook.com/'),
            preserve_default=False,
        ),
    ]
