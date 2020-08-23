from django.shortcuts import render, get_object_or_404
from .models import WeeklyAccountabilityMeeting


def all_wams(request):
    wams = WeeklyAccountabilityMeeting.objects.order_by('theme')
    return render(request, 'wam/all_wams.html', {'wams': wams})


def detail(request, wam_id):
    wam = get_object_or_404(WeeklyAccountabilityMeeting, pk=wam_id)
    return render(request, 'wam/detail.html', {'wam': wam})
