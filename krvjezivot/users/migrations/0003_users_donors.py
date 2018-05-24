# Generated by Django 2.0.5 on 2018-05-23 22:44

from django.db import migrations, models
import enumfields.fields
import krvjezivot.donations.enums
import krvjezivot.users.enums


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=1024, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='user',
            name='blood_group',
            field=enumfields.fields.EnumField(blank=True, enum=krvjezivot.donations.enums.BloodGroup, max_length=32, null=True, verbose_name='blood group'),
        ),
        migrations.AddField(
            model_name='user',
            name='distance',
            field=models.IntegerField(blank=True, null=True, verbose_name='distance to nearest donation venue'),
        ),
        migrations.AddField(
            model_name='user',
            name='frequency',
            field=models.FloatField(blank=True, null=True, verbose_name='average number of donations last year'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_donation_date',
            field=models.DateField(blank=True, null=True, verbose_name='date of last donation'),
        ),
        migrations.AddField(
            model_name='user',
            name='rhesus_factor',
            field=enumfields.fields.EnumField(blank=True, enum=krvjezivot.donations.enums.RhesusFactor, max_length=32, null=True, verbose_name='rhesus factor'),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=enumfields.fields.EnumField(blank=True, enum=krvjezivot.users.enums.Sex, max_length=32, null=True, verbose_name='sex'),
        ),
    ]