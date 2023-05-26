# Generated by Django 4.2.1 on 2023-05-25 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fashion',
            field=models.CharField(choices=[('CASUAL', '캐쥬얼'), ('STREET', '스트릿'), ('FORMAL', '포멀'), ('RETRO', '레트로'), ('ATHLEISURE', '애슬레저'), ('FUNK', '펑크')], max_length=50, null=True, verbose_name='패션'),
        ),
    ]
