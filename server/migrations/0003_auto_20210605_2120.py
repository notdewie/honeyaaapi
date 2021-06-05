# Generated by Django 3.2.4 on 2021-06-05 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20210605_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interestName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Oriented',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientedType', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='swipeperson',
            name='fromPerson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_person', to='server.person'),
        ),
        migrations.AlterField(
            model_name='swipeperson',
            name='toPerson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_person', to='server.person'),
        ),
        migrations.AddField(
            model_name='person',
            name='interested',
            field=models.ManyToManyField(to='server.Interest'),
        ),
        migrations.AddField(
            model_name='person',
            name='oriented',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.oriented'),
        ),
    ]