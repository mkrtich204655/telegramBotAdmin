
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('user_name', models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci')),
                ('bad_rating', models.IntegerField()),
                ('blocked_until', models.DateField()),
            ],
        ),
    ]
