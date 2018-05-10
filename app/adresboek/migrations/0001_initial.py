# Generated by Django 2.0.3 on 2018-05-10 13:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('slug', models.CharField(default=uuid.uuid4, max_length=36, unique=True)),
                ('vernomen_adres', models.CharField(blank=True, default='', max_length=100)),
                ('straatnaam', models.CharField(blank=True, max_length=100)),
                ('huisnummer', models.PositiveSmallIntegerField(default=0)),
                ('toevoeging', models.CharField(blank=True, default='', max_length=6)),
                ('postcode', models.CharField(blank=True, help_text='Formaat: 0000AA', max_length=6)),
                ('plaatsnaam', models.CharField(blank=True, max_length=100)),
                ('deelgemeente', models.CharField(blank=True, max_length=100)),
                ('provincie', models.CharField(blank=True, choices=[('DR', 'Drenthe'), ('FL', 'Flevoland'), ('FR', 'Friesland'), ('GE', 'Gelderland'), ('GR', 'Groningen'), ('LI', 'Limburg'), ('NB', 'Noord-Brabant'), ('NH', 'Noord-Holland'), ('OV', 'Overijssel'), ('UT', 'Utrecht'), ('ZE', 'Zeeland'), ('ZH', 'Zuid-Holland')], max_length=2)),
                ('vernomen_bewoners', models.CharField(blank=True, default='', max_length=100)),
                ('in_de_wijk', models.NullBooleanField()),
                ('compleet', models.BooleanField(default=0)),
                ('wijzigings_datum', models.DateField(auto_now=True, verbose_name='Laatst gewijzigd')),
            ],
            options={
                'verbose_name_plural': 'Adressen',
                'ordering': ['-compleet', 'postcode', 'huisnummer'],
            },
        ),
    ]
