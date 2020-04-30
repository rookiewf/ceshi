from django.db import models


# Create your models here.
class User(models.Model):
    SEX = (
        ('male', '女生'),
        ('fmale', '男生')
    )
    name = models.CharField(max_length=12, verbose_name='姓名')
    age = models.IntegerField(null=True, verbose_name='年龄')
    sex = models.CharField(null=True, max_length=12, choices=SEX, verbose_name='性别')

    class Meta:
        db_table = 'user'

    def to_dict(self):
        return {
            'name':self.name,
            'age':self.age,
            'sex':self.sex
        }
