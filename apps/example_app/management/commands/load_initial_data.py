from django.core.management.base import BaseCommand
from apps.example_app.models import UserProfile, Message

class Command(BaseCommand):
    help = 'Load initial test data into the database'

    def handle(self, *args, **kwargs):
        UserProfile.objects.create(username='john_doe', email='john@example.com', bio='Software Developer')
        UserProfile.objects.create(username='jane_doe', email='jane@example.com', bio='Data Scientist')

        Message.objects.create(sender_id=1, recipient_id=2, content='Hello, Jane!')
        Message.objects.create(sender_id=2, recipient_id=1, content='Hello, John!')

        self.stdout.write(self.style.SUCCESS('Initial data loaded successfully'))
