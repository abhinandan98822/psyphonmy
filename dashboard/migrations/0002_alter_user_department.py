# Generated by Django 3.2.12 on 2022-05-13 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(blank=True, choices=[('AD', 'AD'), ('BT', 'BT'), ('OT', 'OT'), ('ST', 'ST'), ('PT', 'PT'), ('SE', 'SE'), ('FO', 'FO')], max_length=2, null=True),
        ),
    ]
