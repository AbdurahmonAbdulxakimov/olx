from django.db import models


class Days(models.TextChoices):
    SEVEN_DAY = "7 kun"
    THIRTY_DAY = "30 kun"


class PlanCode(models.TextChoices):
    VIP = "VIP"
    TOP = "TOP"


class PlanGroup(models.Model):
    pass


class PlanDetail(models.Model):
    group = models.ForeignKey(PlanGroup, on_delete=models.CASCADE, blank=True, null=True)
    code = models.CharField(max_length=255, choices=PlanCode.choices, null=True, blank=True)
    choice_text = models.CharField(max_length=16, choices=Days.choices, null=True, blank=True)
    amount = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.code


class Plan(models.Model):
    title = models.CharField(max_length=256)
    detail = models.ForeignKey(PlanDetail, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title