from django.db import models
from ckeditor.fields import RichTextField


class MainMenu(models.Model):
    title = models.CharField(verbose_name = 'Заголовок страницы', max_length=200, null = True)
    title_kaz = models.CharField(verbose_name = 'Заголовок страницы каз', max_length=200, null = True)
    name = models.CharField(verbose_name = 'Название меню', max_length=200)
    name_kz = models.CharField(verbose_name = 'Название меню каз', max_length=200, null = True, blank=True)
    name_description = models.CharField(verbose_name = 'Подтекст', max_length=200, null = True, blank=True)
    name_description_kz = models.CharField(verbose_name = 'Подтекст каз', max_length=200, null = True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = 'Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name = 'Время изменения')
    is_published = models.BooleanField(default=True, verbose_name = 'Опубликованный')
    slug = models.SlugField(max_length=255, unique=True, db_index = True, verbose_name="URL")
    page_html = models.TextField(verbose_name = 'Изменения страницы', blank=True)
    page_html_kz =models.TextField(verbose_name = 'Изменения страницы каз', blank=True)
    text = models.TextField(verbose_name = 'Описание', null = True, blank=True)
    text_kz = models.TextField(verbose_name = 'Описание каз', null = True, blank=True)
    meta_description = models.TextField(verbose_name = 'Meta Description SEO', null = True, blank=True)
    meta_description_kaz = models.TextField(verbose_name = 'Meta Description SEO kaz', null = True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("главное меню")
        verbose_name_plural = ("Главное меню")

    def get_absolute_url(self):
        pass

    
class SubMenu(models.Model):
    title = models.CharField(verbose_name = 'Заголовок страницы', max_length=200, null = True)
    title_kaz = models.CharField(verbose_name = 'Заголовок страницы каз', max_length=200, null = True)
    name = models.CharField(verbose_name = 'Название меню', max_length=200)
    name_kz = models.CharField(verbose_name = 'Название меню каз', max_length=200, blank=True)
    name_description = models.CharField(verbose_name = 'Подтекст', max_length=200, null = True, blank=True)
    name_description_kz = models.CharField(verbose_name = 'Подтекст каз', max_length=200, null = True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = 'Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name = 'Время изменения')
    is_published = models.BooleanField(default=True, verbose_name = 'Опубликованный')
    slug = models.SlugField(max_length=255, unique=True, db_index = True, verbose_name="URL")
    image = models.ImageField(upload_to = 'static/%Y/%m/%d/', verbose_name = 'Изображение категории', null = True, blank=True)
    main_menu = models.ForeignKey(MainMenu, on_delete = models.CASCADE)
    page_html = models.TextField(verbose_name = 'Изменения страницы', blank=True)
    page_html_kz = models.TextField(verbose_name = 'Изменения страницы каз', blank=True)
    text = models.TextField(verbose_name = 'Описание', null = True, blank=True)
    text_kz = models.TextField(verbose_name = 'Описание каз', null = True, blank=True)
    meta_description = models.TextField(verbose_name = 'Meta Description SEO', null = True, blank=True)
    meta_description_kaz = models.TextField(verbose_name = 'Meta Description SEO kaz', null = True, blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("меню категорий")
        verbose_name_plural = ("Меню категорий")
    
class SubCategoryMenu(models.Model):
    title = models.CharField(verbose_name = 'Заголовок страницы', max_length=200, null = True)
    title_kaz = models.CharField(verbose_name = 'Заголовок страницы каз', max_length=200, null = True)
    name = models.CharField(verbose_name = 'Название меню', max_length=200)
    name_kz = models.CharField(verbose_name = 'Название меню каз', max_length=200, blank=True)
    name_description = models.CharField(verbose_name = 'Подтекст', max_length=200, null = True, blank=True)
    name_description_kz = models.CharField(verbose_name = 'Подтекст каз', max_length=200, null = True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = 'Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name = 'Время изменения')
    is_published = models.BooleanField(default=True, verbose_name = 'Опубликованный')
    image = models.ImageField(upload_to = 'static/%Y/%m/%d/', verbose_name = 'Изображение категории', null = True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index = True, verbose_name="URL")
    main_menu = models.ForeignKey(SubMenu, on_delete = models.CASCADE)
    page_html = models.TextField(verbose_name = 'Изменения страницы', blank=True)
    page_html_kz = models.TextField(verbose_name = 'Изменения страницы каз', blank=True)
    text = models.TextField(verbose_name = 'Описание', null = True, blank=True)
    text_kz = models.TextField(verbose_name = 'Описание каз', null = True, blank=True)
    meta_description = models.TextField(verbose_name = 'Meta Description SEO', null = True, blank=True)
    meta_description_kaz = models.TextField(verbose_name = 'Meta Description SEO kaz', null = True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("меню подкатегорий")
        verbose_name_plural = ("Меню подкатегорий")

class Products(models.Model):
    title = models.CharField(verbose_name = 'Заголовок страницы', max_length=200, null = True)
    title_kaz = models.CharField(verbose_name = 'Заголовок страницы каз', max_length=200, null = True)
    name = models.CharField(verbose_name = 'Наименование товара', max_length=200)
    name_kz = models.CharField(verbose_name = 'Наименование товара каз', max_length=200, null = True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = 'Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name = 'Время изменения')
    is_published = models.BooleanField(default=True, verbose_name = 'Опубликованный')
    slug = models.SlugField(max_length=255, unique=True, db_index = True, verbose_name="URL")
    # sub_menu_id = models.CharField(max_length=10, choices=menues, default=None)
    page_html = models.TextField(verbose_name = 'Изменения страницы', blank=True)
    page_html_kz = models.TextField(verbose_name = 'Изменения страницы каз', blank=True)
    text = models.TextField(verbose_name = 'Описание', blank=True)
    text_kz = models.TextField(verbose_name = 'Описание каз', blank=True)
    image = models.ImageField(upload_to = 'static/%Y/%m/%d/', verbose_name = 'Изображение товара', null = True, blank=True)
    price = models.IntegerField(verbose_name = 'Цена')
    promotion_price = models.IntegerField(verbose_name = 'Цена со скидкой', default=0)
    meta_description = models.TextField(verbose_name = 'Meta Description SEO', null = True, blank=True)
    meta_description_kaz = models.TextField(verbose_name = 'Meta Description SEO kaz', null = True, blank=True)
    main_menu = models.ForeignKey(SubCategoryMenu, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("товар")
        verbose_name_plural = ("Товары")

# main_menu = MainMenu.objects.all()
# for i in main_menu:
#     print(i['id'], i['name'], i['name_kz'])
class Settings(models.Model):
    company_name = models.CharField(verbose_name = 'Название компании', max_length=200)
    company_title = models.CharField(verbose_name = 'Краткое описание компании', max_length=200, null=True, blank=True)
    company_title_kz = models.CharField(verbose_name = 'Краткое описание компании каз', max_length=200, null=True, blank=True)
    company_logo = models.ImageField(upload_to = 'static/', verbose_name = 'Logo компании', null = True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = 'Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name = 'Время изменения')
    is_published = models.BooleanField(default=True, verbose_name = 'Опубликованный')
    phone = models.CharField(verbose_name = 'Номер телефона', max_length=200, null=True)
    phone_1 = models.CharField(verbose_name = 'Номер телефона', max_length=200, null=True, blank=True)
    phone_2 = models.CharField(verbose_name = 'Номер телефона', max_length=200, null=True, blank=True)
    phone_3 = models.CharField(verbose_name = 'Номер телефона', max_length=200, null=True, blank=True)
    address = models.CharField(verbose_name = 'Адрес компании', max_length=2000)
    e_address = models.EmailField(verbose_name = 'Email адрес компании', max_length=500)
    work_time = models.CharField(verbose_name = 'График работы', max_length=200)
    instagram = models.CharField(verbose_name = 'Ссылка на Instagram', max_length=200, null=True, blank=True)
    telegram = models.CharField(verbose_name = 'Ссылка на Telegram', max_length=200, null=True, blank=True)
    

    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name = ("настройку")
        verbose_name_plural = ("Настройки")

class Gallery(models.Model):
    name = models.CharField(verbose_name = 'Название картинки', max_length=200, null=True, blank=True)
    picture = models.ImageField(upload_to = 'static/', verbose_name = 'Загрузить изображение', null = True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = 'Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name = 'Время изменения')
    is_published = models.BooleanField(default=True, verbose_name = 'Опубликованный')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("картинка")
        verbose_name_plural = ("Галерея")

