# Generated by Django 2.2.6 on 2020-01-11 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teraz', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetPies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(blank=True, max_length=20, null=True)),
                ('u_mail', models.CharField(blank=True, max_length=20, null=True)),
                ('u_reason', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
