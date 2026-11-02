"""Seed awal: profil + project dari data yang sudah ada. Bisa diubah semua via admin."""
from django.db import migrations


def seed(apps, schema_editor):
    SiteProfile = apps.get_model('portfolio', 'SiteProfile')
    Project = apps.get_model('portfolio', 'Project')

    if not SiteProfile.objects.exists():
        SiteProfile.objects.create(
            display_name='WANN/YAYA',
            pronouns='she/they',
            headline='Illustrator & Game Developer',
            location='Semarang, ID',
            about=(
                'Mahasiswa D3 Teknik Informatika di Politeknik Negeri Semarang. '
                'Suka creative tech — AR, game, dan hal-hal visual yang aneh tapi fun. '
                'Lagi bangun ASTORYA (AR storybook Ramayana buat Tugas Akhir) dan '
                'INVESTIGATE IT! (game misteri 2D). Kadang gambar, kadang ngoding, '
                'sering dua-duanya.'
            ),
            github_url='https://github.com/yayadile',
            stack=(
                'Languages: Dart, PHP, JavaScript, TypeScript, C#, Kotlin, Python\n'
                'Frameworks: Flutter, Laravel, Next.js, Unity, Django\n'
                'Databases: MariaDB, SQLite, Room, Redis\n'
                'Design: Figma, Adobe Illustrator, Blender\n'
                'Creative Tech: MindAR, Three.js, ARCore, LiteRT'
            ),
            marquee_text='OPEN FOR PROJECTS * AR * GAMES * CREATIVE TECH * LET\'S COLLAB * ',
        )

    if not Project.objects.exists():
        Project.objects.bulk_create([
            Project(
                title='ASTORYA',
                slug='astorya',
                tagline='Marker-based AR Ramayana storybook',
                description=(
                    'Tugas Akhir: buku cerita mewarnai Ramayana yang hidup lewat AR. '
                    'Scan halaman bukunya, muncul pop-up 3D, bisa live coloring, '
                    'ada narasi bilingual Indonesia-Inggris.\n\n'
                    'Dibangun dengan Flutter + MindAR/Three.js untuk AR-nya, dan pipeline '
                    'After Effects -> Blender buat aset pop-up 3D-nya.'
                ),
                tech='Flutter, MindAR, Three.js, Blender, After Effects',
                order=1,
            ),
            Project(
                title='INVESTIGATE IT!',
                slug='investigate-it',
                tagline='2D mystery / detective investigation game',
                description=(
                    'Game investigasi 2D: jelajahi TKP, kumpulkan clue, periksa bukti, '
                    'interogasi saksi dan tersangka, hubungkan semuanya di investigation board, '
                    'pecahkan puzzle-nya, lalu tuduh pelakunya.'
                ),
                tech='Unity, C#',
                order=2,
            ),
            Project(
                title='RiceCheck',
                slug='ricecheck',
                tagline='Rice authenticity detector',
                description=(
                    'Aplikasi Android pendeteksi beras oplosan vs beras asli lewat analisis citra. '
                    'Foto berasnya, dapat verdict + confidence score — jalan fully on-device, offline.'
                ),
                tech='Kotlin, Jetpack Compose, CameraX, LiteRT, Room',
                order=3,
            ),
            Project(
                title='SITAMA',
                slug='sitama',
                tagline='Web + mobile app',
                description='Aplikasi dengan backend Laravel dan client mobile Flutter.',
                tech='Laravel, Flutter, MariaDB',
                order=4,
            ),
            Project(
                title='KOMPAS',
                slug='kompas',
                tagline='Web app',
                description='Aplikasi web berbasis Next.js dengan database MariaDB.',
                tech='Next.js, MariaDB',
                order=5,
            ),
        ])


def unseed(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
