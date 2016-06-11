from app import db, api, basic_auth
from app.resources import BasicAuthResource
from app.services.parsing import find_tags
from app.services.validation import list_channel_choices
from flask.ext.restful import reqparse, fields, marshal_with, inputs
from flask import Blueprint, request, g
from app.models import *
import re

jrnls = Blueprint('jrnl',__name__)


#TODO: Consider Implementing parser inheritance http://flask-restful-cn.readthedocs.io/en/0.3.5/reqparse.html#parser-inheritance
post_parser = reqparse.RequestParser()
post_parser.add_argument('entry',required=True,location='json')
post_parser.add_argument('channel_id',required=True,type=int,location='json',choices=list_channel_choices())
post_parser.add_argument('created_at',required=True,type=inputs.datetime_from_iso8601,location='json')

#TODO: Return custom javascript responses for the following cases: Invalid/missing channel_id, invalid/missing datetime, missing entry

@api.resource('/jrnls','/jrnls/<int:jrnl_id>')
class Jrnls(BasicAuthResource):
    """
    Jrnls endpoint
    Responsible for handling the jrnls resources
    Methods:
    """

    # Endpoint Specification
    # POST /jrnls - create new jrnl entry
    # POST /jrnls/<int> - Error: Can't create a jrnl that already exists
    tag_fields = {
    'id': fields.Integer,
    'name': fields.String
    }

    resource_fields = {
        'account_id': fields.String,
        'created_at': fields.DateTime(),
        'channel_id': fields.Integer,
        'entry': fields.String,
        'id': fields.Integer,
        'tags': fields.List(fields.Nested(tag_fields))
    }

    @marshal_with(resource_fields)
    def get(self,jrnl_id=None):
        jrnls = Jrnl.query.filter_by(account_id = g.account_id)
        if jrnl_id:
            jrnls = jrnls.filter_by(id = jrnl_id)
        return jrnls.all()

    @marshal_with(resource_fields)
    def post(self,jrnl_id=None):
        """
        Endpoint for creating new jrnl entries
        """
        if jrnl_id:
            return [], 405
        args = post_parser.parse_args()
        args['account_id'] = g.account_id
        jrnl = Jrnl(**args)
        tags = find_tags(jrnl.entry)
        for tag_name in tags:
            tag = Tag.query.filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
            jrnl.tags.append(tag)
        try:
            db.session.add(jrnl)
            db.session.commit()
        except:
            db.session.rollback()
            #TODO: Figure out appropriate SQLAlchemy error to catch and handle. No pokemon exception handling allowed
        else:
            return jrnl, 201

    def put(self,jrnl_id=None):
        """
        Update a jrnl entry
        """
        if not jrnl_id:
            return [], 405


    def delete(self,jrnl_id=None):
        """
        delete a jrnl entry
        """
        if not jrnl_id:
            return [], 405
        jrnl = Jrnl.query.filter_by(account_id = g.account_id).filter_by(id = jrnl_id).first()
        if jrnl:
            try:
                db.session.delete(jrnl)
                db.session.commit()
            except: #FIXME: Pokemon Exception handling.
                db.session.rollback()
        return [],204
