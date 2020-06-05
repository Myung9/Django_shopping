from django.db import models

# Create your models here.

class User(models.Model):
    #objects = models.Manager()
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    #admin페이지에서 객체를 문자열로 확인하기 위한 __str__
    def __str__(self):
        return self.email

    class Meta:
        db_table = 'm9_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
