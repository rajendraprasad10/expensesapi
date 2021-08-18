from django.db import models

# Create your models here.
from django.db import models
from authentication.models import User
# Create your models here.


class Income(models.Model):

    SOUECE_OPTIONS =[
        ('SALARY', 'SALARY'),
        ('BUSINESS', 'BUSINESS'),
        ('SIDE-HUSTLES', 'SIDE-HUSTLES'),
        ('OTHERS', 'OTHERS')
    ]

    source = models.CharField(choices=SOUECE_OPTIONS, max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)

    class Meta:
        odering:['-date']

    def __str__(self):
        return str(self.owner)+'s income'