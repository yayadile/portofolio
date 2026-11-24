from django.db import models


class SiteProfile(models.Model):
    """Satu-satunya profil situs. Diedit lewat admin, tampil di seluruh web."""
    display_name = models.CharField(max_length=80, default='WANN/YAYA')
    pronouns = models.CharField(max_length=40, blank=True, default='she/they')
    headline = models.CharField(max_length=120, default='Illustrator & Game Developer')
    headline_en = models.CharField(max_length=120, blank=True, help_text='Versi English (kosong = pakai yang Indonesia).')
    location = models.CharField(max_length=80, blank=True, default='Semarang, ID')
    about = models.TextField(blank=True)
    about_en = models.TextField(blank=True, help_text='Versi English (kosong = pakai yang Indonesia).')
    photo = models.ImageField(
        upload_to='profile/', blank=True,
        help_text='Foto kamu. Otomatis jadi duotone biru begitu di-upload.',
    )
    email = models.EmailField(blank=True)
    github_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    stack = models.TextField(
        blank=True,
        help_text='Satu grup per baris. Format: "Grup: item1, item2". Contoh: "Languages: Dart, PHP, JS"',
    )
    stack_en = models.TextField(blank=True, help_text='Versi English (kosong = pakai yang Indonesia).')
    marquee_text = models.CharField(
        max_length=200, blank=True, default='OPEN FOR PROJECTS * AR * GAMES * CREATIVE TECH * '
    )
    marquee_text_en = models.CharField(max_length=200, blank=True, help_text='Versi English (kosong = pakai yang Indonesia).')

    class Meta:
        verbose_name = 'Site Profile'
        verbose_name_plural = 'Site Profile'

    def __str__(self):
        return f'Site Profile ({self.display_name})'

    def stack_groups(self):
        return self.stack_groups_for('id')

    def stack_groups_for(self, lang='id'):
        raw = self.stack
        if lang == 'en' and (self.stack_en or '').strip():
            raw = self.stack_en
        groups = []
        for line in raw.splitlines():
            line = line.strip()
            if not line:
                continue
            if ':' in line:
                name, items = line.split(':', 1)
                groups.append((name.strip(), [i.strip() for i in items.split(',') if i.strip()]))
            else:
                groups.append(('', [line]))
        return groups


class Project(models.Model):
    """Satu project di portofolio. Urutan diatur lewat kolom 'order' di admin."""
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    tagline = models.CharField(max_length=200, blank=True)
    tagline_en = models.CharField(max_length=200, blank=True, help_text='Versi English (kosong = pakai yang Indonesia).')
    description = models.TextField(blank=True)
    description_en = models.TextField(blank=True, help_text='Versi English (kosong = pakai yang Indonesia).')
    tech = models.CharField(
        max_length=300, blank=True,
        help_text='Pisahkan dengan koma. Contoh: Flutter, MindAR, Blender',
    )
    image = models.ImageField(
        upload_to='projects/', blank=True,
        help_text='Gambar project. Otomatis jadi duotone biru begitu di-upload.',
    )
    link_url = models.URLField(blank=True, help_text='Link demo / live (opsional)')
    repo_url = models.URLField(blank=True, help_text='Link repo GitHub (opsional)')
    featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return self.title

    def tech_list(self):
        return [t.strip() for t in self.tech.split(',') if t.strip()]

    @property
    def cover(self):
        """Gambar cover buat card di halaman utama.

        Pakai `image` kalau ada; kalau belum, pakai gambar galeri pertama
        supaya project yang cuma punya foto galeri tetap punya thumbnail.
        """
        if self.image:
            return self.image
        first = self.images.first()
        return first.image if first else None


class ProjectImage(models.Model):
    """Gambar tambahan buat satu project (galeri di halaman detail)."""
    project = models.ForeignKey(
        Project, related_name='images', on_delete=models.CASCADE,
        verbose_name='Project',
    )
    image = models.ImageField(
        upload_to='projects/gallery/',
        help_text='Gambar tambahan. Otomatis jadi duotone biru seperti cover.',
    )
    caption = models.CharField(max_length=200, blank=True, help_text='Opsional.')
    order = models.PositiveIntegerField(default=0, help_text='Kecil = duluan.')

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Project image'
        verbose_name_plural = 'Project gallery images'

    def __str__(self):
        return self.caption or f'{self.project.title} — image {self.pk or "baru"}'
