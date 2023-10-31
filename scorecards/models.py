from django.db import models
from courses.models import Course, Tee

class Scorecard(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tee = models.ForeignKey(Tee, on_delete=models.CASCADE)
    hole1 = models.PositiveSmallIntegerField(default=0)
    hole2 = models.PositiveSmallIntegerField(default=0)
    hole3 = models.PositiveSmallIntegerField(default=0)
    hole4 = models.PositiveSmallIntegerField(default=0)
    hole5 = models.PositiveSmallIntegerField(default=0)
    hole6 = models.PositiveSmallIntegerField(default=0)
    hole7 = models.PositiveSmallIntegerField(default=0)
    hole8 = models.PositiveSmallIntegerField(default=0)
    hole9 = models.PositiveSmallIntegerField(default=0)
    hole10 = models.PositiveSmallIntegerField(default=0)
    hole11 = models.PositiveSmallIntegerField(default=0)
    hole12 = models.PositiveSmallIntegerField(default=0)
    hole13 = models.PositiveSmallIntegerField(default=0)
    hole14 = models.PositiveSmallIntegerField(default=0)
    hole15 = models.PositiveSmallIntegerField(default=0)
    hole16 = models.PositiveSmallIntegerField(default=0)
    hole17 = models.PositiveSmallIntegerField(default=0)
    hole18 = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"Scorecard for {self.course} - {self.tee}"

    class Meta:
        db_table = "scorecard"