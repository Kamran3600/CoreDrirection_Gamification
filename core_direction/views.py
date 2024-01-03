from django.shortcuts import render
from .models import FosUserUser, GamificationChallenge
from django.core.paginator import Paginator
from django.utils import timezone
from .handler import process_relevant_challenges


def fos_user_user(request):
    user_list = FosUserUser.objects.order_by('id')
    paginator = Paginator(user_list, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'fos_user_user.html', {'fos_user_users': page_obj})


def gamification_challenge_view(request):
    challenges_list = GamificationChallenge.objects.all().order_by('id')
    paginator = Paginator(challenges_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gamification_challenge.html', {'paginated_challenges': page_obj})


def process_and_update_mongo(request):
    gamif_challenges = GamificationChallenge.objects.filter(end_date__gt=timezone.now())
    user_challenge_ids = list(gamif_challenges.values_list('id', flat=True))
    job = process_relevant_challenges.delay(user_challenge_ids)
    return render(request, 'challenge_queue.html', {'job_id': job.id})
