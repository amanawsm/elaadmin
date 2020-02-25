from django.db import models
from django.utils import timezone
from baserooter.models import requestNormal,deploymentRequest
from django.contrib.auth import get_user_model
User = get_user_model()


class chatModel(models.Model):
    id = models.AutoField(primary_key=True)
    normal = models.ForeignKey(requestNormal, related_name='normal', blank=True, null=True, on_delete=models.CASCADE)
    deployment = models.ForeignKey(deploymentRequest, related_name='deployment',blank=True, null=True,on_delete=models.CASCADE)
    message = models.CharField(max_length=5000)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        output = str(self.id)
        return output
    class Meta:
        db_table = 'chat_logs'
        indexes = [
            models.Index(fields=['id', 'normal','deployment','message','created_at'])
        ]