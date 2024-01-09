import logging

from core_direction.views import process_and_update_mongo

# Get an instance of the logger
logger = logging.getLogger(__name__)


def cronjob():
    process_and_update_mongo(None)

