from django.db import models


class SiteProfile(models.Model):
    """Satu-satunya profil situs. Diedit lewat admin, tampil di seluruh web."""
    display_name = models.CharField(max_length=80, default='WANN/YAYA')
    pronouns = models.CharField(max_length=40, blank=True, default='she/they')
    headline = models.CharField(max_length=120, default='Illustrator & Game Developer')
    location = models.CharField(max_length=80, blank=True, default='Semarang, ID')
    about = models.TextField(blank=True)
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
    marquee_text = models.CharField(
        max_length=200, blank=True, default='OPEN FOR PROJECTS * AR * GAMES * CREATIVE TECH * '
    )

    class Meta:
        verbose_name = 'Site Profile'
        verbose_name_plural = 'Site Profile'

    def __str__(self):
        return f'Site Profile ({self.display_name})'

    def stack_groups(self):
        groups = []
        for line in self.stack.splitlines():
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
    description = models.TextField(blank=True)
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
