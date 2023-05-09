from django.db import models
import uuid

class AppScore(models.Model):
    app_score_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=255)
    as_date = models.DateField()
    as_q1 = models.IntegerField()
    as_q2 = models.IntegerField()
    as_q3 = models.IntegerField()
    as_q4 = models.IntegerField()
    as_q5 = models.IntegerField()

    class Meta:
        db_table = 'app_score'
