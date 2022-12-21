from django.db import models
from django.utils.translation import gettext_lazy
from costumers.models import Costumer

class Payment(models.Model):
    class Service(models.TextChoices):
        NETFLIX = 'NF', gettext_lazy('Netflix')
        AMAZON = 'AP', gettext_lazy('Amazon Prime')
        START = 'ST', gettext_lazy('Start Plus')
        PARAMOUNT = 'PM', gettext_lazy('Paramount Plus')
    
    service = models.CharField(max_length=2, choices=Service.choices, default=Service.NETFLIX)
    user = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    ammount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)