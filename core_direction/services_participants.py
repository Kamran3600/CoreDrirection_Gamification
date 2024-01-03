from core_direction.mongo import ChallengeParticipant
from operator import itemgetter


def update_mongo_participants(users_info):
    sorted_users_info = sorted(users_info, key=itemgetter('total_core_points'), reverse=True)
    for index, user_info in enumerate(sorted_users_info, start=1):
        ChallengeParticipant.objects(id=user_info['user_id']).update_one(
            upsert=True,
            total_core_points=user_info['total_core_points'],
            rank=index,
            username=user_info['username']

        )
        print(f"Updated user {user_info['user_id']} - totalCorePoints: {user_info['total_core_points']}, rank: {index},username:{user_info['username']}")