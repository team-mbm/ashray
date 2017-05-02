from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
# Create your models here.


class PersonalInfo(models.Model):
    user = models.OneToOneField(User)
    father_name = models.CharField(_("Father Name"), max_length=20)
    street_name = models.CharField(_("Street Name"), max_length=20)
    city = models.CharField(_("City"), max_length=20)
    state = models.CharField(_("State"), max_length=20)

    def __str__(self):
        return str(self.user.username)


class Mobile(models.Model):
    regex = RegexValidator(regex=r'^[789]\d{9}$', message="Invalid Mobile Number")
    mobile = models.CharField(_("mobile number"), validators=[regex], blank=True, null=True, max_length=10,
                              help_text="Enter a valid 10 digit mobile number.")
    is_mobile_verified = models.BooleanField(_("is mobile verified"), default=False, blank=False, null=False)

    def __str__(self):
        return self.mobile

    class Meta:
        abstract = True


class PreviousWork(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"))
    start_date = models.DateField(_("Start Date"))
    end_date = models.DateField(_("End Date"))

    class Meta:
        abstract = True


class TypesOfPosition(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Description"))

    def __str__(self):
        return self.name
