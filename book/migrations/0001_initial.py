# Generated by Django 3.2.5 on 2021-07-08 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='نام')),
                ('last_name', models.CharField(max_length=40, verbose_name='نام خانوادگی')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='تاریخ وفات')),
                ('nick_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='تخلص')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='ژانر کتاب را وارد کنید', max_length=200, verbose_name='ژانر')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='نام انشارات')),
                ('phone', models.PositiveIntegerField(blank=True)),
                ('addres', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('summary', models.TextField(max_length=500, verbose_name='خلاصه ')),
                ('pages', models.IntegerField()),
                ('Year', models.DateField()),
                ('isbn', models.CharField(blank=True, help_text='مراجعه شود به اینجا http://www.isbn.ir/Forms/faq.aspx', max_length=13, null=True, verbose_name='شابک')),
                ('img', models.ImageField(blank=True, null=True, upload_to='home/%Y/%m/%d/')),
                ('author', models.ManyToManyField(to='book.Author', verbose_name='نویسنده')),
                ('genre', models.ManyToManyField(to='book.Genre', verbose_name='ژانر')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.publisher', verbose_name='ناشر')),
            ],
        ),
    ]
