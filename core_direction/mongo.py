from operator import itemgetter

from mongoengine import Document, StringField, IntField, connect

connect("Core_direction")


class ChallengeParticipant(Document):
    id = IntField()
    username = StringField()
    firstname = StringField()
    lastname = StringField()
    profile_picture = StringField()
    email = StringField()
    gender = StringField()
    privacy = StringField()
    total_core_points = IntField()
    stepCounts = IntField()
    checkins = IntField()
    heartRate = IntField()
    totalActivityLogToday = IntField()
    rank = IntField()
    numberOfParticipant = IntField()
    challengeId = IntField()
    meta = {
        'collection': 'challengeparticipantschemas'
    }


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
