from django_rq import job
from .models import GamificationChallenge, UserGamificationChallenge, GamificationCorePointRecord
from django.utils import timezone
from django.db.models import Sum
from .mongo import update_mongo_participants


@job('gamification_challenges')
def process_relevant_challenges(challenge_ids):
    gamif_challenges = GamificationChallenge.objects.filter(
        id__in=challenge_ids, end_date__gt=timezone.now()
    )

    users_info = []
    for challenge in gamif_challenges:
        user_gamification_entries = UserGamificationChallenge.objects.filter(
            gamification_challenge_id=challenge.id,
        )
        for entry in user_gamification_entries:
            user = entry.user

            total_core_points = GamificationCorePointRecord.objects.filter(
                user=user,
                assign_date__gte=challenge.start_date,
                assign_date__lte=challenge.end_date,
            ).aggregate(total_points=Sum('day_core_point'))['total_points'] or 0

            users_info.append({
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'rank': entry.rank,
                'total_core_points': total_core_points,
            })

    users_info = sorted(users_info, key=lambda x: x['total_core_points'], reverse=True)
    for i, user_info in enumerate(users_info, start=1):
        user_info['rank'] = i

    update_mongo_participants(users_info)

    return users_info
