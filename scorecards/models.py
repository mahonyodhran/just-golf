from django.db import models

class Scorecard(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = "scorecard"
    
    def __str__(self):
        return self.name