from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

role = (
    ('student', 'Student'),
    ('teacher', 'Teacher')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(choices=role, default=role[0][0], max_length=30, blank=False, null=False)

    def __str__(self):
        return f"{self.user.username} User Role is {self.role}"

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
