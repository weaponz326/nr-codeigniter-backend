from django.db import models

from accounts.models import Profile


# Create your models here.

class Cashflow(models.Model):
    account = models.ForeignKey(Profile, on_delete=models.CASCADE)
    sheet_code = models.CharField(max_length=20, blank=True)
    sheet_name = models.CharField(max_length=100, blank=True)
    sheet_type = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return str(self.id)

class DailyInflow(models.Model):
    cashflow = models.ForeignKey(Cashflow, on_delete=models.CASCADE)
    inflow = models.CharField(max_length=150, blank=True)
    monday = models.CharField(max_length=18, blank=True)
    tuesday = models.CharField(max_length=18, blank=True)
    wednesday = models.CharField(max_length=18, blank=True)
    thursday = models.CharField(max_length=18, blank=True)
    friday = models.CharField(max_length=18, blank=True)
    thursday = models.CharField(max_length=18, blank=True)
    wednesday = models.CharField(max_length=18, blank=True)

    def __str__(self):
        return str(self.id)
    
class DailyOutflow(models.Model):
    cashflow = models.ForeignKey(Cashflow, on_delete=models.CASCADE)
    outflow = models.CharField(max_length=150, blank=True)
    monday = models.CharField(max_length=18, blank=True)
    tuesday = models.CharField(max_length=18, blank=True)
    wednesday = models.CharField(max_length=18, blank=True)
    thursday = models.CharField(max_length=18, blank=True)
    friday = models.CharField(max_length=18, blank=True)
    thursday = models.CharField(max_length=18, blank=True)
    wednesday = models.CharField(max_length=18, blank=True)

    def __str__(self):
        return str(self.id)

class WeeklyInflow(models.Model):
    cashflow = models.ForeignKey(Cashflow, on_delete=models.CASCADE)
    inflow = models.CharField(max_length=150, blank=True)
    week_one = models.CharField(max_length=18, blank=True)
    week_two = models.CharField(max_length=18, blank=True)
    week_three = models.CharField(max_length=18, blank=True)
    week_four = models.CharField(max_length=18, blank=True)
    week_five = models.CharField(max_length=18, blank=True)
    
    def __str__(self):
        return str(self.id)

class WeeklyOutflow(models.Model):
    cashflow = models.ForeignKey(Cashflow, on_delete=models.CASCADE)
    outflow = models.CharField(max_length=150, blank=True)
    week_one = models.CharField(max_length=18, blank=True)
    week_two = models.CharField(max_length=18, blank=True)
    week_three = models.CharField(max_length=18, blank=True)
    week_four = models.CharField(max_length=18, blank=True)
    week_five = models.CharField(max_length=18, blank=True)
    
    def __str__(self):
        return str(self.id)

class MonthlyInflow(models.Model):
    cashflow = models.ForeignKey(Cashflow, on_delete=models.CASCADE)
    inflow = models.CharField(max_length=150, blank=True)
    january = models.CharField(max_length=18, blank=True)
    february = models.CharField(max_length=18, blank=True)
    march = models.CharField(max_length=18, blank=True)
    april = models.CharField(max_length=18, blank=True)
    may = models.CharField(max_length=18, blank=True)
    june = models.CharField(max_length=18, blank=True)
    july = models.CharField(max_length=18, blank=True)
    august = models.CharField(max_length=18, blank=True)
    september = models.CharField(max_length=18, blank=True)
    october = models.CharField(max_length=18, blank=True)
    november = models.CharField(max_length=18, blank=True)
    december = models.CharField(max_length=18, blank=True)
    
    def __str__(self):
        return str(self.id)

class MonthlyOutflow(models.Model):
    cashflow = models.ForeignKey(Cashflow, on_delete=models.CASCADE)
    outflow = models.CharField(max_length=150, blank=True)
    january = models.CharField(max_length=18, blank=True)
    february = models.CharField(max_length=18, blank=True)
    march = models.CharField(max_length=18, blank=True)
    april = models.CharField(max_length=18, blank=True)
    may = models.CharField(max_length=18, blank=True)
    june = models.CharField(max_length=18, blank=True)
    july = models.CharField(max_length=18, blank=True)
    august = models.CharField(max_length=18, blank=True)
    september = models.CharField(max_length=18, blank=True)
    october = models.CharField(max_length=18, blank=True)
    november = models.CharField(max_length=18, blank=True)
    december = models.CharField(max_length=18, blank=True)
    
    def __str__(self):
        return str(self.id)

class QuarterlyInflow(models.Model):
    cashflow = models.ForeignKey(Cashflow, on_delete=models.CASCADE)
    inflow = models.CharField(max_length=150, blank=True)
    first_quarter = models.CharField(max_length=18, blank=True)
    second_quarter = models.CharField(max_length=18, blank=True)
    third_quarter = models.CharField(max_length=18, blank=True)
    fourth_quarter = models.CharField(max_length=18, blank=True)
    
    def __str__(self):
        return str(self.id)

class QuarterlyOutflow(models.Model):
    cashflow = models.ForeignKey(Cashflow, on_delete=models.CASCADE)
    outflow = models.CharField(max_length=150, blank=True)
    first_quarter = models.CharField(max_length=18, blank=True)
    second_quarter = models.CharField(max_length=18, blank=True)
    third_quarter = models.CharField(max_length=18, blank=True)
    fourth_quarter = models.CharField(max_length=18, blank=True)
    
    def __str__(self):
        return str(self.id)
