from django.db import models



class Node(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Dsp(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name




class Router(models.Model):
    node = models.ForeignKey(Node)
    safe_uid = models.CharField(max_length=256, blank=True, null=True)
    active = models.BooleanField()
    dsp = models.ForeignKey(Dsp)

    def __str__(self):
        return "%s %s" % (self.node, self.dsp)

    class Meta:
        unique_together = ('node', 'dsp','safe_uid')
