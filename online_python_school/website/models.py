from django.db import models

class Topic(models.Model):
    topic_seq = models.CharField(max_length=50, unique=False, null=True)
    topic_name = models.CharField(max_length=100, unique=True)
    topic_text = models.TextField(null=True)
    topic_task = models.TextField(null=True)

    def __str__(self):
        return self.topic_name