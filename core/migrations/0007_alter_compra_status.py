# Generated by Django 4.1.3 on 2022-11-15 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='status',
            field=models.IntegerField(choices=[(1, 'Carrinho'), (2, 'Realizado'), (3, 'Pago'), (4, 'Entregue')], default=1),
        ),
    ]
