# Generated by Django 4.0.3 on 2022-03-06 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='professor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='professor.professor'),
            preserve_default=False,
        ),
    ]
