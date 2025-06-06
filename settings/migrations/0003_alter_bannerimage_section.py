# Generated by Django 5.2.1 on 2025-05-09 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_alter_bannerimage_image_alter_sitesettings_site_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerimage',
            name='section',
            field=models.CharField(choices=[('home_hero', 'Home Hero'), ('about_hero', 'About Hero'), ('education_hero', 'Education Hero'), ('development_hero', 'Development Hero'), ('portfolio_hero', 'Portfolio Hero'), ('contact_hero', 'Contact Hero'), ('cta_image', 'Call to Action Image')], max_length=50, unique=True),
        ),
    ]
