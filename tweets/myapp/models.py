from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)  # Save the image first

    #     img_path = self.image.path
    #     img = Image.open(img_path)

    #     # Resize to fixed size (example: 300x300)
    #     output_size = (300, 300)
    #     img = img.resize(output_size, Image.ANTIALIAS)
    #     img.save(img_path)

def __str__(self):
    return f'{self.user.username} - {self.text[:10]}'
