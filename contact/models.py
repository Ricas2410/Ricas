from django.db import models

class ContactSubmission(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('education', 'ICT Education'),
        ('development', 'Software Development'),
        ('cybersecurity', 'Cybersecurity'),
        ('computer', 'Computer Sales'),
        ('network', 'Network Services'),
        ('general', 'General Inquiry'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.service_type} - {self.created_at.strftime('%Y-%m-%d')}"

    class Meta:
        ordering = ['-created_at']
