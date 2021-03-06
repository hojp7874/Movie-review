# Generated by Django 3.1.3 on 2021-06-01 14:10

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieCd', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('movieNm', models.CharField(max_length=50)),
                ('movieNmEn', models.CharField(blank=True, max_length=100)),
                ('prdtYear', models.CharField(blank=True, max_length=10)),
                ('openDt', models.CharField(blank=True, max_length=10)),
                ('typeNm', models.CharField(blank=True, max_length=10)),
                ('prdtStatNm', models.CharField(blank=True, max_length=10)),
                ('nationAlt', models.CharField(blank=True, max_length=30)),
                ('genreAlt', models.CharField(blank=True, max_length=30)),
                ('repNationNm', models.CharField(blank=True, max_length=10)),
                ('repGenreNm', models.CharField(blank=True, max_length=10)),
                ('posterSrc', models.TextField(null=True)),
                ('popularity', models.CharField(max_length=20, null=True)),
                ('story', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserMovieScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('like_users', models.ManyToManyField(related_name='like_reviews', to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=10)),
                ('photo', models.TextField()),
                ('like_users', models.ManyToManyField(related_name='like_peoples', to=settings.AUTH_USER_MODEL)),
                ('movies', models.ManyToManyField(related_name='peoples', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('like_users', models.ManyToManyField(related_name='like_comments', to=settings.AUTH_USER_MODEL)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movies.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
