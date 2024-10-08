# Generated by Django 4.2.4 on 2023-09-04 12:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0003_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="rating",
            field=models.DecimalField(
                decimal_places=1,
                max_digits=2,
                validators=[django.core.validators.MaxValueValidator(5)],
            ),
        ),
    ]
