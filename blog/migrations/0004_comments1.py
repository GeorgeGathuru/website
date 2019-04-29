# Generated by Django 2.2 on 2019-04-26 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_comments_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=200)),
                ('Comments1', models.TextField()),
                ('comment_time1', models.DateTimeField(default=django.utils.timezone.now)),
                ('email1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
