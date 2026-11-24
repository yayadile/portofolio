"""Kamus string UI: id = default, en = English. Tambah/edit sesukamu."""

STRINGS = {
    'flip_hint': {'id': 'seret / klik kartunya buat muter', 'en': 'drag / click the card to spin it'},
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
    'empty_projects': {'id': 'belum ada project.', 'en': 'no projects yet.'},
    'empty_stack': {'id': 'belum ada stack.', 'en': 'no stack yet.'},
    'empty_about': {'id': 'belum ada deskripsi.', 'en': 'no description yet.'},
    'empty_desc': {'id': 'belum ada deskripsi.', 'en': 'no description yet.'},
    'no_image': {'id': 'BELUM ADA GAMBAR', 'en': 'NO IMAGE'},
    'project_file': {'id': '* arsip project *', 'en': '* project file *'},
    'cover': {'id': 'cover', 'en': 'cover'},
    'portfolio_vol': {'id': '* portofolio — vol.01 *', 'en': '* portfolio — vol.01 *'},
}


def tr(key, lang):
    entry = STRINGS.get(key, {})
    return entry.get(lang) or entry.get('id') or key
