import uuid
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class Room(models.Model):
    id           = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) 
    name         = models.CharField(max_length=50, unique=True)
    private_room = models.BooleanField(default=False)
    passcode     = models.CharField(max_length=128, blank=True, null=True, default=None)
    created_by   = models.ForeignKey(User, related_name='created_rooms', on_delete=models.CASCADE)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("room", kwargs={"pk": self.pk})
    
    def check_passcode(self, passcode):
        return check_password(passcode, self.passcode)

    def save(self, *args, **kwargs):
        if self.private_room:
            self.passcode = make_password(self.passcode)
        super(Room, self).save(*args, **kwargs)
