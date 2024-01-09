from core_direction.mongo import ChallengeParticipant
from operator import itemgetter


def update_mongo_participants(users_info):
    sorted_users_info = sorted(users_info, key=itemgetter('totalCorePoints'), reverse=True)
    for index, user_info in enumerate(sorted_users_info, start=1):
        ChallengeParticipant.objects(id=user_info['user_id']).update_one(
            upsert=True,
            totalCorePoints=user_info['totalCorePoints'],
            rank=index,
            username=user_info['username'],
            email=user_info['email'],
            firstname=user_info['firstname'],
            lastname=user_info['lastname'],
            profile_picture=user_info['profile_picture'],
            gender=user_info['gender'],
            privacy=user_info['privacy'],
            challengeID=user_info['challengeID'],
            challengeSlug=user_info['challengeSlug'],
            stepCounts=user_info['stepCounts']

        )
        print(
            f"Updated user {user_info['user_id']} - totalCorePoints: {user_info['totalCorePoints']}, rank: {user_info['rank']}, username: {user_info['username']}, email: {user_info['email']}, firstname: {user_info['firstname']}, lastname: {user_info['lastname']}, profile_picture: {user_info['profile_picture']}, gender: {user_info['gender']}, privacy: {user_info['privacy']}, challengeID: {user_info['challengeID']}, challengeSlug: {user_info['challengeSlug']}, stepCounts: {user_info['stepCounts']}")
