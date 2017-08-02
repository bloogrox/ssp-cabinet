from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=128)
    active = models.BooleanField()
    targetings = models.ManyToManyField(Field, through="CampaignFilter")

    def __str__(self):
        return self.name


class CampaignFilter(models.Model):
    campaign = models.ForeignKey(Campaign)
    field = models.ForeignKey(Field)
    value = models.CharField(max_length=1024)

    class Meta:
        unique_together = ('campaign', 'field',)
