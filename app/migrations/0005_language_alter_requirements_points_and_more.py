# Generated by Django 5.0.2 on 2024-03-30 02:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_level_alter_author_author_profile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='requirements',
            name='points',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='what_you_will_learn',
            name='points',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.language'),
        ),
    ]
