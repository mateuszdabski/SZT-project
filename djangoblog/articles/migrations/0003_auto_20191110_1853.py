# Generated by Django 2.2.7 on 2019-11-10 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
