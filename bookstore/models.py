from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категорія')

    def __str__(self) -> str:
        return self.title


class SubCategory(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категорія')
    title = models.CharField(max_length=100, verbose_name='Підкатегорія')
    image = models.ImageField(upload_to='images/subcategory', blank=True, verbose_name='Зображення')

    def __str__(self) -> str:
        return f'{self.category} : {self.title}'


class PaperBook(models.Model):
    LANGUAGES_CHOICES = [
        ('Російська', 'Російська'),
        ('Українська', 'Українська'),
        ('Англійська', 'Англійська'),
    ]

    PAPER_CHOICES = [
        ('Офсетний', 'Офсетний'),
        ('Книжкова', 'Книжкова'),
        ('Крейдований', 'Крейдований'),
    ]

    BOOK_COVER_CHOICES = [
        ('Тверда', 'Тверда'),
        ('М\'яка', 'М\'яка'),
    ]

    ILLUSTRATIONS_CHOICES = [
        ('Немає ілюстрацій', 'Немає ілюстрацій'),
        ('Чорно-білі', 'Чорно-білі'),
        ('Кольорові', 'Кольорові'),
    ]

    PERIOD_LITERATURE_CHOICES = [
        ('Література XX ст.', 'Література ХХ ст.'),
        ('Сучасна література', 'Сучасна література'),
    ]

    # mandatory characteristics
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name='*Категорія')
    subcategory = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True, verbose_name='*Суб-категорія')
    code = models.CharField(max_length=100, null=True, verbose_name='*Код книги')
    title = models.CharField(max_length=100, verbose_name='*Назва книги')
    format = models.CharField(max_length=100, verbose_name='*Формат')
    language = models.CharField(max_length=100, choices=LANGUAGES_CHOICES, verbose_name='*Мова')
    book_cover = models.CharField(max_length=100, choices=BOOK_COVER_CHOICES, verbose_name='*Палітурка')
    price = models.IntegerField(verbose_name='*Ціна (грн)')
    image = models.CharField(max_length=255, verbose_name='*Зображення')
    about_the_book = models.TextField(verbose_name='*Усе про книжку')
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True, verbose_name='*Видавництво')

    # optional characteristics
    isbn = models.CharField(max_length=100, blank=True, null=True, verbose_name='ISBN')
    Illustrations = models.CharField(max_length=100, choices=ILLUSTRATIONS_CHOICES, blank=True, null=True,
                                     verbose_name='*Ілюстрації')
    number_of_pages = models.CharField(max_length=100, blank=True, null=True, verbose_name='Кількість сторінок')
    author = models.ManyToManyField('Author', blank=True, verbose_name='Автор')
    interpreter = models.ManyToManyField('Interpreter', blank=True, verbose_name='Перекладач')
    illustrator = models.ManyToManyField('Illustrations', blank=True, verbose_name='Ілюстратор')
    book_series = models.ForeignKey('BookSeries', on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name='Серія')
    year_first_publishing = models.IntegerField(blank=True, null=True, verbose_name='Рік першого видавництва')
    year_publication = models.IntegerField(blank=True, null=True, verbose_name='Рік видання')
    weight = models.CharField(max_length=100, blank=True, null=True, verbose_name='Вага')
    edition = models.IntegerField(blank=True, null=True, verbose_name='Тираж')
    paper = models.CharField(max_length=100, choices=PAPER_CHOICES, blank=True, null=True, verbose_name='Папір')
    period_literature = models.CharField(
        max_length=100, choices=PERIOD_LITERATURE_CHOICES, blank=True, null=True,
        verbose_name='Література за періодами')

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return self.title


class Author(models.Model):
    title = models.CharField(max_length=100, verbose_name='Повне ім\'я')
    image = models.CharField(max_length=255, blank=True, verbose_name='*Зображення')
    biography = models.TextField(blank=True, verbose_name='Біографія')

    def __str__(self) -> str:
        return self.title


class Publisher(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва видавництва')
    image = models.CharField(max_length=255, blank=True, verbose_name='*Зображення')
    information = models.TextField(blank=True, verbose_name='Інформація про видавництво')

    def __str__(self) -> str:
        return self.title


class Interpreter(models.Model):
    title = models.CharField(max_length=100, verbose_name='Повне ім\'я')

    def __str__(self) -> str:
        return self.title


class Illustrations(models.Model):
    title = models.CharField(max_length=100, verbose_name='Повне ім\'я')

    def __str__(self) -> str:
        return self.title


class BookSeries(models.Model):
    title = models.CharField(max_length=100, verbose_name='Серія книг')

    def __str__(self) -> str:
        return self.title
