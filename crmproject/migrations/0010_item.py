# Generated by Django 4.2.1 on 2023-06-20 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crmproject', '0009_remove_category_product_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmproject.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmproject.product')),
            ],
        ),
    ]
