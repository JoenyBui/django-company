from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from rest_framework.authtoken.models import Token


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     """
#     Create new authentication token new user is created.
#
#     :param sender:
#     :param instance:
#     :param created:
#     :param kwargs:
#     :return:
#     """
#     if created:
#         tk = Token.objects.create(user=instance)
#         tk.save()
