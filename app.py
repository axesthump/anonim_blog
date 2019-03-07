# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from datetime import date

import config as config
# import json

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)


db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    from models import Article
    from forms import ArticleForm

    if request.method == 'POST':
        form = ArticleForm(request.form)

        if form.validate():
            data_a = Article(**form.data)
            db.session.add(data_a)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return'Form is not valid! Post was not created.\n  ' + str(form.errors)

    if request.method == 'GET':
        articles = Article.query.all()
        return render_template('index.html', articles=articles, date_time=date.today())


@app.route('/aricle/<article_id>', methods=('GET', 'POST'))
def create(article_id):
    from models import Comment, Article
    from forms import CommentForm
    article = Article.query.filter_by(id=article_id).first()

    if request.method == 'POST':
        form = CommentForm(request.form)
        

        if form.validate():
            data = Comment(**form.data)
            db.session.add(data)
            db.session.commit()
            data.comment_id = article.id
            db.session.commit()
            return redirect(url_for('create', article_id=article_id))
        else:
            return redirect(url_for('create', article_id=article_id))


    if request.method == 'GET':
        all_comments = Comment.query.filter_by(comment_id=article_id)
        return render_template('article.html', article=article, comments=all_comments, date_today=date.today())


if __name__ == '__main__':
    from models import *

    db.create_all()
    #db.drop_all()
    app.run()
