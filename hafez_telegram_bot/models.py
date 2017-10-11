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
        return str(self.text)


@python_2_unicode_compatible
class UserInformation(models.Model):
    class Meta:
        verbose_name = "کاربران تلگرام بات"
        verbose_name_plural = "کاربران تلگرام بات"

    user_id = models.CharField(max_length=20, verbose_name="کد کاربری تلگرام", unique=True)
    username = models.CharField(max_length=100, verbose_name="نام انتخابی کاربر", default="ندارد")
    first_name = models.CharField(max_length=100, verbose_name="نام کاربر", default="ندارد")
    last_name = models.CharField(max_length=100, verbose_name="فامیل کاربر", default="ندارد")
    createdUserTime = models.DateTimeField(auto_now_add=True, verbose_name="زمان ساخت اکانت")
    changedUserTime = models.DateTimeField(auto_now=True, verbose_name="آخرین استفاده از ربات")


def __str__(self):
    return str(self.user_id)