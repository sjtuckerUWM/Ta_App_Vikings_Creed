# Generated by Django 4.0.3 on 2022-05-15 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj_app', '0003_alter_coursemodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='assigned_tas',
            field=models.ManyToManyField(related_name='tas', to='proj_app.myusermodel'),
        ),
    ]
