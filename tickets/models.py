from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Choices for our dropdown menus
STATUS_CHOICES = (
    ('Open', 'Open'),
    ('In Progress', 'In Progress'),
    ('Resolved', 'Resolved'),
    ('Closed', 'Closed'),
)

PRIORITY_CHOICES = (
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
    ('Urgent', 'Urgent'),
)

CATEGORY_CHOICES = (
    ('Question', 'Question'),
    ('Request', 'Request'),
    ('Complaint', 'Complaint'),
    ('Other', 'Other'),
)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    ('Prefer not to say', 'Prefer not to say'),
)

class QueryTicket(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField()
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submitted_queries")
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_queries")
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Medium')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Question')
    
    admin_resolution = models.TextField(
        blank=True, 
        null=True, 
        help_text="The resolution/reply from the admin for the user to see."
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"[{self.get_priority_display()}] {self.subject} ({self.get_status_display()})"

    # --- THIS IS YOUR SIMPLE "AUTO-TAGGING" ---
    def save(self, *args, **kwargs):
        # On first save, try to auto-tag
        if not self.pk: # Only run on creation
            desc_lower = self.description.lower()
            if 'broken' in desc_lower or 'refund' in desc_lower or 'angry' in desc_lower:
                self.category = 'Complaint'
                self.priority = 'High'
            elif 'help' in desc_lower or 'how do i' in desc_lower:
                self.category = 'Question'
                self.priority = 'Medium'
            elif 'request' in desc_lower or 'please add' in desc_lower:
                self.category = 'Request'
                self.priority = 'Low'
                
        super().save(*args, **kwargs) # Call the real save method


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
    address = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    state = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

# This signal automatically creates/updates a Profile when a User is created/saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()