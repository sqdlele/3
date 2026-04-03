from django.db import models


class HomeContentBlock(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='home_blocks/', blank=True, null=True)
    button_text = models.CharField(max_length=40, blank=True)
    button_link = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title


class AboutPage(models.Model):
    title = models.CharField(max_length=140, default='О нас')
    intro = models.TextField(
        default='Мы создаем универсальные проекты и сервисы под разные задачи и аудитории.',
    )
    mission_title = models.CharField(max_length=140, default='Наша миссия')
    mission_text = models.TextField(
        default='Помогаем запускать понятные и удобные цифровые продукты.',
    )
    values_title = models.CharField(max_length=140, default='Наши принципы')
    values_text = models.TextField(
        default='Качество, прозрачность процессов и внимание к людям.',
    )

    def __str__(self):
        return 'Настройки страницы "О нас"'


class TeamMember(models.Model):
    full_name = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.full_name} — {self.role}'


class AboutGalleryImage(models.Model):
    title = models.CharField(max_length=120, blank=True)
    image = models.ImageField(upload_to='about_gallery/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title or f'Фото #{self.pk}'
