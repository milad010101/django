# Generated by Django 4.1.2 on 2022-10-09 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Daste_Bandi_Ketab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Nevisandeh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Family', models.CharField(max_length=150)),
                ('Age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Family', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('daste_Bandi_Ketab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.daste_bandi_ketab')),
                ('nevisandeh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.nevisandeh')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.user')),
            ],
        ),
    ]
