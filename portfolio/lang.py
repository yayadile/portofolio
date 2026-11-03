"""Kamus string UI: id = default, en = English. Tambah/edit sesukamu."""

STRINGS = {
    'nav_about': {'id': 'tentang', 'en': 'about'},
    'nav_work': {'id': 'karya', 'en': 'work'},
    'nav_stack': {'id': 'stack', 'en': 'stack'},
    'nav_contact': {'id': 'kontak', 'en': 'contact'},
    'sec_about': {'id': 'tentang', 'en': 'about'},
    'sec_work': {'id': 'karya pilihan', 'en': 'selected work'},
    'sec_contact': {'id': 'kontak', 'en': 'contact'},
    'fact_name': {'id': 'nama', 'en': 'name'},
    'fact_pronouns': {'id': 'pronomina', 'en': 'pronouns'},
    'fact_based': {'id': 'domisili', 'en': 'based'},
    'fact_focus': {'id': 'fokus', 'en': 'focus'},
    'fact_focus_val': {'id': 'creative tech, ar, game', 'en': 'creative tech, ar, games'},
    'read_more': {'id': 'selengkapnya ->', 'en': 'read more ->'},
    'back_to_work': {'id': '<- kembali', 'en': '<- back to work'},
    'more_work': {'id': 'lainnya', 'en': 'more work'},
    'contact_big_1': {'id': 'yuk bikin', 'en': "let's make"},
    'contact_big_2': {'id': 'sesuatu yang aneh_', 'en': 'something weird_'},
    'footer_built': {'id': 'dibuat dengan django * atur di admin', 'en': 'built with django * set in admin'},
    'empty_projects': {'id': 'belum ada project — tambah lewat admin -> projects.', 'en': 'no projects yet — add via admin -> projects.'},
    'empty_stack': {'id': 'isi stack di admin -> site profile.', 'en': 'fill the stack in admin -> site profile.'},
    'empty_about': {'id': 'tulis tentang kamu di admin -> site profile.', 'en': 'write about yourself in admin -> site profile.'},
    'empty_desc': {'id': 'deskripsi project diisi di admin.', 'en': 'fill in the project description in admin.'},
    'no_photo': {'id': 'BELUM ADA FOTO', 'en': 'NO PHOTO'},
    'no_image': {'id': 'BELUM ADA GAMBAR', 'en': 'NO IMAGE'},
    'upload_via_admin': {'id': 'upload via admin ->', 'en': 'upload via admin ->'},
    'project_file': {'id': '* arsip project *', 'en': '* project file *'},
    'portfolio_vol': {'id': '* portofolio — vol.01 *', 'en': '* portfolio — vol.01 *'},
}


def tr(key, lang):
    entry = STRINGS.get(key, {})
    return entry.get(lang) or entry.get('id') or key
