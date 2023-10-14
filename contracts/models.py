# CycleTime/contracts/models.py

from django.db import models
from django.contrib.auth.models import User

# Attorney Model
class Attorney(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Each attorney has one user associated with them.
    
    # If you want to add additional fields for an attorney later on, you can add them here.

    def __str__(self):
        return self.user.username

# Contract Model
class Contract(models.Model):
    attorney = models.ForeignKey(Attorney, on_delete=models.CASCADE)  # Each contract is associated with an attorney.
    title = models.CharField(max_length=200)  # Contract title.
    start_date = models.DateTimeField()       # Start date for the contract.
    end_date = models.DateTimeField()         # End date for the contract.

    def __str__(self):
        return self.title

    # Property to calculate the duration/lifecycle of the contract.
    @property
    def lifecycle_duration(self):
        return self.end_date - self.start_date
