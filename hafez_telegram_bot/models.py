from django.db import models
from future.utils import python_2_unicode_compatible


@python_2_unicode_compatible
class Hafez_Fall(models.Model):
    class Meta:
        verbose_name = "فال حافظ"
        verbose_name_plural = "فال حافظ"

    text = models.TextField(blank=False, verbose_name="شعر")
    description = models.TextField(blank=False, verbose_name="تفسیر")

    def __str__(self):
        return "{0}_{1}".format(self.text, self.description)


@python_2_unicode_compatible
class UserInformation(models.Model):
    class Meta:
        verbose_name = "کاربران تلگرام بات"
        verbose_name_plural = "کاربران تلگرام بات"

    user_id = models.CharField(max_length=100, verbose_name="کد کاربری تلگرام", unique=True)
    username = models.CharField(max_length=100, verbose_name="نام انتخابی کاربر")
    first_name = models.CharField(max_length=100, verbose_name="نام کاربر")
    last_name = models.CharField(max_length=100, verbose_name="فامیل کاربر")
    state = models.CharField(default="صفحه اول", max_length=200, verbose_name="موقعیت در ربات")

    def __str__(self):
        return "{0}_{1}_{2}_{3}".format(self.user_id, self.username, self.first_name, self.last_name)
