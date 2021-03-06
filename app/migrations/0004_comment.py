# Generated by Django 2.1.2 on 2018-10-15 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181011_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='username')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('url', models.URLField(blank=True, null=True, verbose_name='url')),
                ('content', models.TextField(verbose_name='comment')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='app.Post', verbose_name='对应的文章')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'db_table': 'comment',
            },
        ),
    ]
