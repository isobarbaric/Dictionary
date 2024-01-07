from django.db import models
from django.contrib.auth.models import User

class VocabTerm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'word'], name='unique_vocab_term')
        ]
    
    def __str__(self):
        return f"{str(self.user)} - {str(self.word)}"