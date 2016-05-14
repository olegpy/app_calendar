from django.db import models
from django.contrib.auth.models import User
from django import forms


from django_countries.fields import CountryField


class Country(models.Model):
    country = models.CharField(max_length=200)
    iso = models.CharField(max_length=5)

    def __unicode__(self):
        return self.country


class Company(models.Model):
    company = models.CharField(max_length=200)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.company


class Agreement(models.Model):
    negotiator = models.ForeignKey(User)
    company = models.ForeignKey(Company)
    credit = models.IntegerField()
    debet = models.IntegerField()
    start_agreement = models.DateField()
    end_agreement = models.DateField()

    def __unicode__(self):
        return self.negotiator.username


class Period(models.Model):
    choice = models.ForeignKey(Agreement)
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return self.choice.negotiator.username

    def clean(self):
        start_date = self.start_date
        end_date = self.end_date
        if start_date > end_date:
            raise forms.ValidationError(
                'End Date must be greater than Start Date')
