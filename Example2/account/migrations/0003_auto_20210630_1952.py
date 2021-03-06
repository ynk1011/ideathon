# Generated by Django 3.1.7 on 2021-06-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210630_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', '남성'), ('F', '여성')], default='', max_length=1, verbose_name='성별'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='job',
            field=models.CharField(choices=[('S', '학생'), ('O', '직장인'), ('F', '프리랜서'), ('E', '기타')], default='', max_length=1, verbose_name='직업'),
        ),
    ]
