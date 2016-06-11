"""
authentication.py

This module provides authentication services
"""
from app import basic_auth, db
from flask import g
from app.models import *

@basic_auth.verify_password
def verify_api_creds(account_id,api_key):
    """
    Verify the API credentials supplied via HTTP Basic Auth
    """
    user = User.query.filter_by(account_id = account_id).first()
    if not user:
        return False

    g.account_id = account_id
    return user.auth_key == api_key
