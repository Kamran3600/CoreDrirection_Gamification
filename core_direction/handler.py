from django.db.models import Sum
from django.utils import timezone
from django_rq import job
from .models import GamificationChallenge, UserGamificationChallenge, GamificationCorePointRecord, FosUserUser
from .services_participants import update_mongo_participants


@job('gamification_challenges')
def process_relevant_challenges(challenge_ids):
    gamif_challenges = GamificationChallenge.objects.filter(
        id__in=challenge_ids, end_date__gt=timezone.now()
    )

    users_info = []
    all_core_points = GamificationCorePointRecord.objects.aggregate(step=Sum('step'))

    for challenge in gamif_challenges:
        user_gamification_entries = UserGamificationChallenge.objects.filter(
            gamification_challenge_id=challenge.id,
        )
        for entry in user_gamification_entries:
            user = entry.user

            total_core_points = GamificationCorePointRecord.objects.filter(
                user=user
            ).aggregate(total_points=Sum('day_core_point'))['total_points'] or 0
            user_info = FosUserUser.objects.values(
                'id', 'username', 'email', 'firstname', 'lastname', 'profile_picture', 'gender', 'privacy'
            ).get(id=user.id)
            users_info.append({
                'user_id': user_info['id'],
                'username': user_info['username'],
                'email': user_info['email'],
                'firstname': user_info['firstname'],
                'lastname': user_info['lastname'],
                'profile_picture': user_info['profile_picture'],
                'gender': user_info['gender'],
                'privacy': user_info['privacy'],
                'challengeID': entry.gamification_challenge_id,
                'rank': entry.rank,
                'totalCorePoints': total_core_points,
                'challengeSlug': challenge.slug_url,
                'stepCounts': all_core_points['step']
            })

    users_info = sorted(users_info, key=lambda x: x['totalCorePoints'], reverse=True)
    for i, user_info in enumerate(users_info, start=1):
        user_info['rank'] = i

    update_mongo_participants(users_info)
    return users_info
