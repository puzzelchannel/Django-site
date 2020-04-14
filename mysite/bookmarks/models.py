# from django.db import models
# from django.contrib.auth.models import User
#
#
# # Create your models here.
#
#
# # imports from custom apps
#
#
# class bookmarks(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     url = models.URLField()
#
#     class Meta:
#         unique_together = (("user", "name"), ("url", "user"))
#
#     def __unicode__(self):
#         return self.url
