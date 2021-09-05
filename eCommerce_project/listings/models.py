from django.db import models

class Seller(models.Model):
  name = models.CharField(max_length=200)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  description = models.TextField(blank=True)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Listing(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
  def __str__(self):
    return self.title