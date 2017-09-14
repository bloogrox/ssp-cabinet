from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=128)
    active = models.BooleanField()
    targetings = models.ManyToManyField(Field, through="CampaignFilter")
    dsp = models.ForeignKey('Dsp')

    def get_targetings(self):
        targetings = CampaignFilter.objects.filter(campaign=self)
        return targetings

    def __str__(self):
        return self.name


class CampaignFilter(models.Model):
    campaign = models.ForeignKey(Campaign)
    field = models.ForeignKey(Field)
    value = models.TextField()

    def value_as_list(self):
        return [val.strip()
                for val in self.value.split(',')]

    def get_operator(self):
        return 'IN'

    class Meta:
        unique_together = ('campaign', 'field',)


class Dsp(models.Model):
    name = models.CharField(max_length=128)
    bid_url = models.CharField(max_length=256)
    active = models.BooleanField()
    ext_fields = models.ManyToManyField(Field)

    def __str__(self):
        return self.name
