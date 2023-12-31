# Generated by Django 4.1.5 on 2023-06-26 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fact_app', '0002_alter_invoice_customer_alter_invoice_save_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fact_app.customer'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='save_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
