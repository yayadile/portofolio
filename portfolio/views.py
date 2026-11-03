from django.shortcuts import get_object_or_404, redirect, render

from .models import Project, SiteProfile


def _lang(request):
    return getattr(request, 'LANG', 'id')


def set_lang(request, code):
    request.session['lang'] = 'en' if code == 'en' else 'id'
    return redirect(request.META.get('HTTP_REFERER', '/'))


def home(request):
    profile = SiteProfile.objects.first()
    projects = Project.objects.all()
    lang = _lang(request)
    return render(request, 'portfolio/home.html', {
        'profile': profile,
        'projects': projects,
        'featured': projects.filter(featured=True),
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
