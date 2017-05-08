from django.db import models
from django.utils.translation import ugettext_lazy as _


class PostalCode(models.Model):
    """
    model to store postalcodes,city and state,
    will be used in dropdown list on Frontend part to fill city and state in Location part
    """
    pin_code = models.CharField(_("Pin Code"), primary_key=True, max_length=20, blank=False, null=False)
    post_office = models.CharField(_("Post Office"), max_length=40, blank=True)
    city = models.CharField(_("City"), max_length=20, blank=True)
    state = models.CharField(_("State"), max_length=20, blank=True)


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
    contact = models.ForeignKey("Contact", blank=True, null=True)
    location = models.ForeignKey("Location", blank=True, null=True)
    type = models.ForeignKey("TypeOfCase", blank=True, null=True)
    case_filer_name = models.CharField(_("Complaintee Name"), max_length=20, blank=True)
    name_child = models.CharField(_("Name of Child"), max_length=20)
    desc = models.TextField(_("Description"), blank=True)

    age_of_child = models.IntegerField(_("Age"))

    '''
    Functions to be made
    '''

    def __str__(self):
        return str(self.case_filer_name)
