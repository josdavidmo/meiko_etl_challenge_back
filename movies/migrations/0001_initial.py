# Generated by Django 2.2.1 on 2019-05-19 21:31
import os

from django.contrib.auth.models import User
import django.contrib.postgres.fields
from django.db import migrations, models


def create_superuser(_, schema_editor):
  superuser = User()
  superuser.is_active = True
  superuser.is_superuser = True
  superuser.is_staff = True
  superuser.username = os.environ['DJANGO_USERNAME']
  superuser.email = os.environ['DJANGO_EMAIL']
  superuser.set_password(os.environ['DJANGO_PASSWORD'])
  superuser.save(using=schema_editor.connection.alias)


class Migration(migrations.Migration):
  initial = True

  dependencies = [
  ]

  operations = [
    migrations.RunPython(create_superuser),
    migrations.CreateModel(
      name='Movie',
      fields=[
        ('id',
         models.AutoField(auto_created=True, primary_key=True, serialize=False,
                          verbose_name='ID')),
        ('movie_title', models.CharField(max_length=100)),
        ('color', models.CharField(max_length=20)),
        ('director_name', models.CharField(max_length=50)),
        ('actor_1_name', models.CharField(max_length=50)),
        ('actor_2_name', models.CharField(max_length=50)),
        ('actor_3_name', models.CharField(max_length=50)),
        ('director_facebook_likes', models.PositiveIntegerField(null=True)),
        ('actor_3_facebook_likes', models.PositiveIntegerField(null=True)),
        ('actor_2_facebook_likes', models.PositiveIntegerField(null=True)),
        ('actor_1_facebook_likes', models.PositiveIntegerField(null=True)),
        ('num_critic_for_reviews', models.PositiveIntegerField(null=True)),
        ('duration', models.IntegerField(null=True)),
        ('gross', models.BigIntegerField(null=True)),
        ('genres', django.contrib.postgres.fields.ArrayField(
          base_field=models.CharField(max_length=20), size=None)),
        ('num_voted_users', models.PositiveIntegerField()),
        ('cast_total_facebook_likes', models.PositiveIntegerField()),
        ('facenumber_in_poster', models.PositiveIntegerField(null=True)),
        ('plot_keywords', django.contrib.postgres.fields.ArrayField(
          base_field=models.CharField(max_length=20), null=True, size=None)),
        ('movie_imdb_link', models.URLField()),
        ('language', models.CharField(max_length=20)),
        ('country', models.CharField(max_length=20)),
        ('content_rating', models.CharField(max_length=20)),
        ('budget', models.BigIntegerField(null=True)),
        ('title_year', models.PositiveIntegerField(null=True)),
        ('imdb_score',
         models.DecimalField(decimal_places=2, max_digits=3, null=True)),
        ('aspect_ratio',
         models.DecimalField(decimal_places=2, max_digits=4, null=True)),
        ('movie_facebook_likes', models.PositiveIntegerField()),
        ('num_user_for_reviews', models.PositiveIntegerField(null=True)),
      ],
    ),
  ]