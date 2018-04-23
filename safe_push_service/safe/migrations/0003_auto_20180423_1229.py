# Generated by Django 2.0.4 on 2018-04-23 12:29

from django.db import migrations, models
import safe_push_service.safe.validators


class Migration(migrations.Migration):

    dependencies = [
        ('safe', '0002_auto_20180416_1350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'verbose_name': 'Device', 'verbose_name_plural': 'Devices'},
        ),
        migrations.AlterModelOptions(
            name='devicepair',
            options={'verbose_name': 'Device Pair', 'verbose_name_plural': 'Device Pairs'},
        ),
        migrations.AlterField(
            model_name='device',
            name='owner',
            field=models.CharField(max_length=42, primary_key=True, serialize=False, validators=[safe_push_service.safe.validators.validate_checksumed_address]),
        ),
        migrations.AlterField(
            model_name='device',
            name='push_token',
            field=models.TextField(blank=True, null=True),
        ),
    ]
