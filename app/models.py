from django.db import models


class MyUser(models.Model):
    email = models.EmailField(max_length=50, )
    fam = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    otc = models.CharField(max_length=50, verbose_name='Отчество')
    phone = models.CharField(max_length=15, verbose_name='Телефон')


class Coords(models.Model):
    latitude = models.CharField(max_length=10, verbose_name='Широта', null=True)
    longitude = models.CharField(max_length=10, verbose_name='Долгота', null=True)
    height = models.CharField(max_length=10, verbose_name='Высота', null=True)


class Level(models.Model):
    LEVEL = [
        ('1А', '1А'),
        ('2А', '2А'),
        ('3А', '3А'),
        ('1B', '1Б'),
        ('2B', '2Б'),
        ('3B', '3Б'),
        ('3B*', '3Б*'),
    ]

    winter = models.CharField(max_length=3, choices=LEVEL, blank=True, verbose_name='Зима')
    summer = models.CharField(max_length=3, choices=LEVEL, blank=True, verbose_name='Лето')
    autumn = models.CharField(max_length=3, choices=LEVEL, blank=True, verbose_name='Осень')
    spring = models.CharField(max_length=3, choices=LEVEL, blank=True, verbose_name='Весна')


class Pereval(models.Model):
    STATUSES = [
        ('new', 'Новое'),
        ('pen', 'На рассмотрении'),
        ('acp', 'Принято'),
        ('rej', 'Отклонено'),
    ]
    beauty_title = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=50, blank=True)
    other_titles = models.CharField(max_length=50, blank=True)
    connect = models.CharField(max_length=50, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUSES, default='new')


class Images(models.Model):
    data = models.CharField(max_length=2000, verbose_name='Cсылка на изображение')
    title = models.CharField(max_length=50, verbose_name='Описание изображения')
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, verbose_name='Изображения', related_name='images')

    def __str__(self):
        return self.data, self.title







