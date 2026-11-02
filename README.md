# Portfolio — Django

Web portofolio zine-style: biru `#0033FF` + putih, font Intel One Mono + VT323 (pixel).
Semua konten (nama, bio, project, foto, stack, sosmed) diatur lewat **Django admin** — nggak perlu ngoding buat update.

## Cara jalanin (di laptop kamu)

```bash
cd portfolio-django

# 1. bikin virtual env & install (sekali aja)
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
pip install -r requirements.txt

# 2. database (sekali aja, udah ada seed isi awal)
python manage.py migrate

# 3. bikin akun admin (sekali aja)
python manage.py createsuperuser

# 4. jalanin
python manage.py runserver
```

Buka:
- Web: http://127.0.0.1:8000
- Admin: http://127.0.0.1:8000/admin (login pake akun tadi)

## Yang bisa di-setting di admin

| Menu | Buat apa |
|---|---|
| **Site profiles** | Nama tampil, pronouns, headline, lokasi, foto profil, bio, email, link GitHub/IG/LinkedIn, tech stack, teks marquee |
| **Projects** | Tambah/edit/hapus project: judul, tagline, deskripsi, tech, gambar, link demo, link repo, urutan tampil (`order`), tampil/nggak (`featured`) |

Catatan:
- **Foto apapun yang di-upload otomatis jadi duotone biru-putih** (efek posterize via CSS). Jadi tinggal upload foto biasa aja.
- Profil cuma bisa satu — tombol "add" disembunyikan kalau udah ada.
- Urutan project diatur dari kolom `order` (kecil = duluan).

## Struktur

```
portfolio-django/
├── config/            # settings & url utama
├── portfolio/         # app: models (SiteProfile, Project), admin, views
│   └── migrations/    # 0002_seed.py = isi awal (boleh dihapus isinya)
├── templates/         # base.html, portfolio/home.html, project_detail.html
├── static/css/        # style.css — semua styling di sini
├── media/             # hasil upload dari admin (dibuat otomatis)
└── manage.py
```

## Mau deploy beneran?

Nanti aja pas udah siap — yang perlu: `DEBUG=False`, ganti `SECRET_KEY`, set `ALLOWED_HOSTS` ke domain kamu,
`python manage.py collectstatic`, dan pake database beneran (Postgres) kalau traffic-nya rame. SQLite cukup buat portofolio pribadi.

## Ganti warna / font?

Semua token ada di `static/css/style.css` bagian `:root`:
`--blue`, font `--mono` (Intel One Mono) dan `--pixel` (VT323, dari Google Fonts).
