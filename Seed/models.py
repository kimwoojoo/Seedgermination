from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from mysite.settings import MEDIA_ROOT


import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(os.path.join(BASE_DIR, "static"))
#print("여기는 models")
class ImageUpload(models.Model):
    image = ProcessedImageField(
        upload_to= "image",
        processors=[ResizeToFill(250,250)],
        format= "JPEG",
        options={'quality' : 80}
    )
# Create your models here.
