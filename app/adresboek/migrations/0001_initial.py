# Generated by Django 2.0.3 on 2018-03-26 22:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('UUid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('slug', models.CharField(default=uuid.uuid4, max_length=36, unique=True)),
                ('vernomen_bewoners', models.CharField(blank=True, default='', max_length=100)),
                ('vernomen_adres', models.CharField(blank=True, default='', max_length=100)),
                ('huisnummer', models.PositiveSmallIntegerField(default=0)),
                ('toevoeging', models.CharField(blank=True, default='', max_length=6)),
                ('in_de_wijk', models.NullBooleanField()),
                ('compleet', models.BooleanField(default=0)),
                ('google_maps_image', models.ImageField(blank=True, default='', upload_to='resources/assets/images/external_api_cache/google_maps/')),
                ('google_streetview_image', models.ImageField(blank=True, default='', upload_to='resources/assets/images/external_api_cache/google_streetview/')),
                ('wijzigings_datum', models.DateField(auto_now=True, verbose_name='Laatst gewijzigd')),
            ],
            options={
                'verbose_name_plural': 'Adressen',
                'ordering': ['-compleet', 'vernomen_adres', 'huisnummer', 'vernomen_bewoners'],
            },
        ),
        migrations.CreateModel(
            name='Postcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.CharField(blank=True, help_text='Formaat: 0000AA', max_length=6)),
                ('straatnaam', models.CharField(blank=True, max_length=100)),
                ('plaatsnaam', models.CharField(blank=True, max_length=100)),
                ('deelgemeente', models.CharField(blank=True, max_length=100)),
                ('provincie', models.CharField(blank=True, choices=[('DR', 'Drenthe'), ('FL', 'Flevoland'), ('FR', 'Friesland'), ('GE', 'Gelderland'), ('GR', 'Groningen'), ('LI', 'Limburg'), ('NB', 'Noord-Brabant'), ('NH', 'Noord-Holland'), ('OV', 'Overijssel'), ('UT', 'Utrecht'), ('ZE', 'Zeeland'), ('ZH', 'Zuid-Holland')], max_length=2)),
                ('breedtegraad', models.DecimalField(decimal_places=13, max_digits=15, null=True)),
                ('lengtegraad', models.DecimalField(decimal_places=13, max_digits=16, null=True)),
                ('wijzigings_datum', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['postcode'],
            },
        ),
        migrations.AddField(
            model_name='adres',
            name='postcode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adresboek.Postcode'),
        ),
    ]
