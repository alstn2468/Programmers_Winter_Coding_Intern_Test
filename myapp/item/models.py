from django.db import models


class Item(models.Model):
    lecture_code = models.CharField(max_length=10)
    lecture = models.CharField(max_length=100)
    professor = models.CharField(max_length=20)
    location = models.CharField(max_length=10)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    day_of_week = models.CharField(max_length=5)
    is_register = models.BooleanField(default=False)

    def __str__(self):
        return self.lecture


class Memo(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             related_name="memos")
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title
