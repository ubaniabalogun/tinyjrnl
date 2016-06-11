"""
validation.py
Custom validators
"""
from app.models import *

def list_channel_choices():
    """
    Returns a list of all the valid channels that exist in the database
    """
    channels = Channel.query.all()
    channel_ids = [channel.id for channel in channels]
    return channel_ids
