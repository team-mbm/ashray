from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Location(models.Model):
    street_number = models.CharField(_("Street Number"), max_length=20, blank=True)
    city = models.CharField(_("City"), max_length=20, blank=True)
    state = models.CharField(_("State"), max_length=20, blank=True)
    pin_code = models.CharField(_("Pin Code"), max_length=20, blank=True)

    def __str__(self):
        return str(self.street_number) + " " + str(self.city)


class Contact(models.Model):
    contact_number = models.CharField(_("Contact Number"), max_length=20, blank=True)
    email = models.CharField(_("Email"), max_length=20, blank=True)

    def __str__(self):
        return str(self.contact_number)


class TypeOfCase(models.Model):
    name = models.CharField(_("Name"), max_length=20, blank=True)
    desc = models.TextField(_("Description"), blank=True)
    max_age = models.IntegerField(_("Age"))

    def __str__(self):
        return str(self.name)


class Case(models.Model):

    case_filer_name = models.CharField(_("Complaintee Name"), max_length=20, blank=True)
    contact = models.ForeignKey("Contact", blank=True, null=True)
    name_child = models.CharField(_("Name of Child"), max_length=20)
    desc = models.TextField(_("Description"), blank=True)
    location = models.ForeignKey("Location", blank=True, null=True)
    type = models.ForeignKey("TypeOfCase", blank=True, null=True)
    age_of_child = models.IntegerField(_("Age"))

    '''
    Functions to be made
    '''

    def __str__(self):
        return str(self.case_filer_name)

class name2(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class name3(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
