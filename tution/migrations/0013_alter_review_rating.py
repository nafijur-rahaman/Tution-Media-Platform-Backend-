# Generated by Django 5.0.6 on 2024-08-15 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0012_remove_review_tuition_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('⭐', 1), ('⭐⭐', 2), ('⭐⭐⭐', 3), ('⭐⭐⭐⭐', 4), ('⭐⭐⭐⭐⭐', 5)], max_length=5),
        ),
    ]
