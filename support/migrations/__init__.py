
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('user_name', models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci')),
                ('support_message', models.TextField(max_length=1000, db_collation='utf8mb4_unicode_ci')),
                ('date', models.DateField()),
                ('status', models.IntegerField()),
            ],
        ),
    ]
