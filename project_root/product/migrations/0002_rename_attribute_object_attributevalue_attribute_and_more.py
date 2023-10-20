# Generated by Django 4.1 on 2023-10-15 06:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attributevalue',
            old_name='attribute_object',
            new_name='attribute',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category_object',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='attribute',
            name='basemodel_ptr',
        ),
        migrations.RemoveField(
            model_name='attributevalue',
            name='basemodel_ptr',
        ),
        migrations.RemoveField(
            model_name='category',
            name='basemodel_ptr',
        ),
        migrations.RemoveField(
            model_name='product',
            name='basemodel_ptr',
        ),
        migrations.AddField(
            model_name='attribute',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attribute',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, 
                                    verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attribute',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, 
                                    verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, 
                                    verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, 
                                    verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

print('product migration 2')
