from django.db import models
from django.urls import reverse, NoReverseMatch

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название меню")

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children', on_delete=models.CASCADE
    )
    url = models.CharField(
        max_length=200, blank=True,
        help_text="Может быть абсолютным URL или именем URL"
    )
    named_url = models.CharField(
        max_length=200, blank=True,
        help_text="Имя URL из urls.py, если хотите использовать reverse()"
    )

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return "#"
        return self.url or "#"

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['menu_id', 'parent_id', 'id']
