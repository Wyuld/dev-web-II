# Generated by Django 3.2.9 on 2021-11-29 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_inscricao_vagadeemprego'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='vagaDeEmprego',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='inscricoes', to='core.vagadeemprego'),
        ),
    ]