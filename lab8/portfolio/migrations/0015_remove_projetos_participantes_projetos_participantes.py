# Generated by Django 4.0.4 on 2022-05-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_formacao_link_cadeira'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projetos',
            name='participantes',
        ),
        migrations.AddField(
            model_name='projetos',
            name='participantes',
            field=models.ManyToManyField(to='portfolio.pessoa'),
        ),
    ]
