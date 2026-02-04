from django.db import models

# Create your models here.

from django.db import models
import os

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # 1. Save the new file first
        super().save(*args, **kwargs)
        
        # 2. Check how many files we have
        files = UploadedFile.objects.all().order_by('-uploaded_at')
        
        # 3. If more than 5, delete the oldest ones
        if files.count() > 5:
            files_to_delete = files[5:] # Keep first 5, delete the rest
            for old_file in files_to_delete:
                # Delete from computer storage
                if old_file.file and os.path.isfile(old_file.file.path):
                    os.remove(old_file.file.path)
                # Delete from database
                old_file.delete()