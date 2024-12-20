# Generated by Django 5.1.3 on 2024-12-01 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_requests', '0002_alter_servicerequest_request_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicerequest',
            old_name='date_requested',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
