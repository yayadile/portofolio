from django.shortcuts import get_object_or_404, redirect, render

from .models import Project, SiteProfile


def _lang(request):
    return getattr(request, 'LANG', 'id')


def set_lang(request, code):
    request.session['lang'] = 'en' if code == 'en' else 'id'
    return redirect(request.META.get('HTTP_REFERER', '/'))


def home(request):
    profile = SiteProfile.objects.first()
    lang = _lang(request)
    projects = Project.objects.filter(featured=True)
    if not projects.exists():
        # Kalau semua di-uncheck, jangan tampilkan halaman kosong.
        projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {
        'profile': profile,
        'projects': projects,
        'stack_groups': profile.stack_groups_for(lang) if profile else [],
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    profile = SiteProfile.objects.first()
    others = Project.objects.exclude(pk=project.pk)[:3]
    return render(request, 'portfolio/project_detail.html', {
        'profile': profile,
        'project': project,
        'others': others,
    })
