# Generated by Django 3.0.2 on 2020-02-24 11:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('baserooter', '0002_auto_20200221_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='chatModel',
            fields=[
                ('request_id', models.IntegerField(auto_created=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=5000)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_by', to='baserooter.User')),
            ],
            options={
                'db_table': 'chat_logs',
            },
        ),
        migrations.AddIndex(
            model_name='chatmodel',
            index=models.Index(fields=['id', 'request_id', 'requested_by', 'message', 'created_at'], name='chat_logs_id_a88483_idx'),
        ),
    ]