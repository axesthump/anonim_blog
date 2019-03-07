# -*- coding: utf-8 -*-

from datetime import date

from app import db

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.Date, default=date.today)
    # is_visible = db.Column(db.Boolean, default=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text
        }


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    #article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False, index=True)
    #article = db.relationship(Article, foreign_keys=[article_id])
    content = db.Column(db.String(500), nullable=False)
    comment_id = db.Column(db.Integer, nullable=True, index=True)
    date_created = db.Column(db.Date, default=date.today)

    def to_dict(self):
        return {
            'com': self.com
        }
