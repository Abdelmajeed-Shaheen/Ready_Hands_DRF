# Generated by Django 3.0.5 on 2020-04-27 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ready_Hands_API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Ready_Hands_API.Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Ready_Hands_API.Address'),
            preserve_default=False,
        ),
    ]