from django.shortcuts import get_object_or_404, render

from .models import Project, SiteProfile


def home(request):
    profile = SiteProfile.objects.first()
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {
        'profile': profile,
        'projects': projects,
        'featured': projects.filter(featured=True),
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
