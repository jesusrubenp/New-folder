from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    original_video = models.FileField(upload_to='original_videos/')
    transcoded_video = models.FileField(upload_to='transcoded_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title