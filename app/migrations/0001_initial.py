# Generated by Django 3.1.4 on 2020-12-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('policy_type', models.CharField(choices=[('AUTO', 'Auto'), ('HEALTH', 'Health'), ('TERM', 'TERM')], default='AUTO', max_length=30)),
                ('sum_insured', models.FloatField()),
                ('premium', models.FloatField()),
            ],
        ),
    ]
