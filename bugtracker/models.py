__author__ = "mwilliamson with help from Joseph H.,Alec and Patterson"
"""
Ticket

Title
Time/Date
Description
Name of user who filed ticket
Status of ticket (New / In Progress / Done / Invalid)
Name of user assigned to ticket
Name of user who completed the ticket
"""

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Ticket(models.Model):
    NEW = 'New'
    IN_PROGRESS = 'In Progress'
    DONE = 'Done'
    INVALID = 'Invalid'
    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In_Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid')
    ]
    title = models.CharField(max_length=300)
    post_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default=NEW
    )
    filed_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='filed_by',
        null=True,
        blank=True,
    )
    assigned_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='assigned_to'
    )
    completed_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='completed_by'
    )

    def __str__(self):
        return f"{self.title} - {self.status}"
