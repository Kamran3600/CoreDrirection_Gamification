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


