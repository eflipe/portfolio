# Generated by Django 3.1.4 on 2020-12-22 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categorías'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Comentarios'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Posts'},
        ),
    ]
