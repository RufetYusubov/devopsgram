# Generated by Django 4.2.3 on 2023-08-14 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialApp', '0002_alter_savemodel_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savemodel',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_saves', to='socialApp.postmodel'),
        ),
    ]