# Generated by Django 3.0.3 on 2020-03-04 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FIAS_Object',
            fields=[
                ('aoid', models.CharField(max_length=36, primary_key=True, serialize=False, unique=True, verbose_name='Идентификатор')),
                ('parent_guid', models.CharField(blank=True, db_index=True, max_length=36, null=True, verbose_name='Идентификатор объекта родительского объекта')),
                ('aoguid', models.CharField(db_index=True, max_length=36, verbose_name='Идентификатор')),
                ('level', models.PositiveIntegerField(default=0, verbose_name='Уровень адресного объекта')),
                ('name', models.CharField(max_length=120, verbose_name='Название')),
                ('short_name', models.CharField(max_length=500, verbose_name='Короткое название')),
                ('region_code', models.CharField(blank=True, max_length=2, null=True, verbose_name='Код региона')),
                ('area_code', models.CharField(blank=True, max_length=3, null=True, verbose_name='Код района')),
                ('city_code', models.CharField(blank=True, max_length=3, null=True, verbose_name='Код города')),
                ('postal_code', models.CharField(blank=True, max_length=6, null=True, verbose_name='Почтовый индекс')),
                ('okato', models.CharField(blank=True, max_length=11, null=True, verbose_name='OKATO')),
                ('oktmo', models.CharField(blank=True, max_length=11, null=True, verbose_name='OKTMO')),
                ('kladr', models.CharField(blank=True, max_length=17, null=True, verbose_name='КЛАДР')),
                ('cent_status', models.PositiveIntegerField(blank=True, null=True, verbose_name='Статус центра')),
                ('live_status', models.BooleanField(default=True, verbose_name='Активность')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты ФИАС',
            },
        ),
        migrations.CreateModel(
            name='FIAS_FederalSubject',
            fields=[
            ],
            options={
                'verbose_name': 'Субъект',
                'verbose_name_plural': 'Субъекты Российской Федерации',
                'proxy': True,
                'default_permissions': (),
                'indexes': [],
                'constraints': [],
            },
            bases=('smpl_fias.fias_object',),
        ),
        migrations.CreateModel(
            name='FIAS_Locality',
            fields=[
            ],
            options={
                'verbose_name': 'Населенный пункт',
                'verbose_name_plural': 'Населенные пункты',
                'proxy': True,
                'default_permissions': (),
                'indexes': [],
                'constraints': [],
            },
            bases=('smpl_fias.fias_object',),
        ),
        migrations.CreateModel(
            name='FIAS_Street',
            fields=[
            ],
            options={
                'verbose_name': 'Улица',
                'verbose_name_plural': 'Улицы',
                'proxy': True,
                'default_permissions': (),
                'indexes': [],
                'constraints': [],
            },
            bases=('smpl_fias.fias_object',),
        ),
    ]