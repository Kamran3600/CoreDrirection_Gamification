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
    totalCorePoints = IntField()
    stepCounts = IntField()
    checkins = IntField()
    heart_rate = IntField()
    totalActivityLogToday = IntField()
    rank = IntField()
    numberOfParticipant = IntField()
    challengeID = IntField()
    challengeSlug = StringField()
    meta = {
        'collection': 'challengeparticipantschemas'
    }


