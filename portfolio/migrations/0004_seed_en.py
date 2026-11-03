"""Isi versi English buat seed awal. Kolom _en boleh dikosongkan — fallback ke Indonesia."""
from django.db import migrations


def seed_en(apps, schema_editor):
    SiteProfile = apps.get_model('portfolio', 'SiteProfile')
    Project = apps.get_model('portfolio', 'Project')

    profile = SiteProfile.objects.first()
    if profile:
        profile.headline_en = 'Illustrator & Game Developer'
        profile.about_en = (
            'Informatics Engineering student (D3) at Politeknik Negeri Semarang. '
            'Into creative tech — AR, games, and weird-but-fun visual stuff. '
            'Currently building ASTORYA (an AR Ramayana storybook for my final project) '
            'and INVESTIGATE IT! (a 2D mystery game). Sometimes I draw, sometimes I code, '
            'often both.'
        )
        profile.marquee_text_en = "OPEN FOR PROJECTS * AR * GAMES * CREATIVE TECH * LET'S COLLAB * "
        profile.save()

    en = {
        'astorya': (
            'Marker-based AR Ramayana storybook',
            'My final project: a Ramayana coloring storybook brought to life with AR. '
            'Scan a page, get a 3D pop-up, live coloring, and bilingual ID/EN narration.\n\n'
            'Built with Flutter + MindAR/Three.js for the AR, and an After Effects → Blender '
            'pipeline for the pop-up assets.',
        ),
        'investigate-it': (
            '2D mystery / detective investigation game',
            'A 2D investigation game: explore the crime scene, collect clues, examine evidence, '
            'interrogate witnesses and suspects, connect everything on the investigation board, '
            'solve the puzzles, then accuse the culprit.',
        ),
        'ricecheck': (
            'Rice authenticity detector',
            'An Android app that detects adulterated vs authentic rice via image analysis. '
            'Snap the rice, get a verdict + confidence score — fully on-device, offline.',
        ),
        'sitama': (
            'Web + mobile app',
            'An app with a Laravel backend and a Flutter mobile client.',
        ),
        'kompas': (
            'Web app',
            'A Next.js web app backed by MariaDB.',
        ),
    }
    for slug, (tagline_en, description_en) in en.items():
        Project.objects.filter(slug=slug).update(tagline_en=tagline_en, description_en=description_en)


def unseed_en(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_project_description_en_project_tagline_en_and_more'),
    ]

    operations = [
        migrations.RunPython(seed_en, unseed_en),
    ]
