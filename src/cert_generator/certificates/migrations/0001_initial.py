# Generated by Django 5.1.1 on 2024-09-14 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('html_template', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneratedCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_name', models.CharField(max_length=200)),
                ('generated_at', models.DateTimeField(auto_now_add=True)),
                ('pdf_file', models.FileField(upload_to='generated_certificates/')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificates.certificatetemplate')),
            ],
        ),
    ]
