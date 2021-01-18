# -*- coding: utf-8 -*-
import click
import datetime
from comment_system import app, db
from comment_system.models import User, Comment ,Blog


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

status_flag=True

@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    username1 = 'admin'
    password1 = '123456'
    token1='12334455'
    username2 = 'wangba'
    password2 = '456789'
    token2 = '1233445533'

    blogs=['博客1','博客12','博客1','博客4','博客1','博客4','博客1','博客7','博客1','博客2','博客1','博客1']
    dates=['1-1','1-2','1-3','1-4','1-5','1-6','1-7','1-8','1-9','1-9','1-10','1-18']
    flow=[1,1,1,1,1,1,1,1,1,1,1,1]

    comments = [
        {'username': 'ZhangHaojie', 'time': '1-1', 'blog': '博客1','blog_username':'admin',
         'content': '这篇文章太棒了', 'likes': 7, 'visible': status_flag},
        {'username': 'ZhangYuancheng', 'time': '1-2', 'blog': '博客12', 'blog_username': 'admin',
         'content': '就那样吧', 'likes': 4, 'visible': status_flag},
        {'username': 'MengHaoran', 'time': '1-3', 'blog': '博客1', 'blog_username': 'admin',
         'content': '一般一般', 'likes': 28, 'visible': status_flag},
        {'username': 'ZhongYunke', 'time': '1-4', 'blog': '博客4', 'blog_username': 'admin',
         'content': '技术很实用', 'likes': 44, 'visible': status_flag},
        {'username': 'LiHua', 'time': '1-5', 'blog': '博客1', 'blog_username': 'admin',
         'content': '踩踩踩踩', 'likes': 2, 'visible': status_flag},
        {'username': "XiaoZhang", 'time': '1-6', 'blog': '博客4', 'blog_username': 'admin',
         'content': '太赞赞赞赞赞', 'likes': 122, 'visible': status_flag},
        {'username': "XiaoWang", 'time': '1-7', 'blog': '博客1', 'blog_username': 'admin',
         'content': '一般，也就那样吧', 'likes': 24, 'visible': status_flag},
        {'username': "XiaoLi", 'time': '1-8', 'blog': '博客7', 'blog_username': 'admin',
         'content': '技术从哪里学的呢', 'likes': 110, 'visible': status_flag},
        {'username': "XiaoZhao", 'time': '1-9', 'blog': '博客1', 'blog_username': 'admin',
         'content': '真不错真不错', 'likes':112, 'visible': status_flag},
        {'username': "XiaoMeng", 'time': '1-9', 'blog': '博客2', 'blog_username': 'admin',
         'content': '这篇真的太好了', 'likes': 33, 'visible': status_flag},
        {'username': 'XiaoZhong', 'time': '1-10', 'blog': '博客1', 'blog_username': 'admin',
         'content': '我也觉得这篇真好', 'likes': 55, 'visible': status_flag},
    ]

    user = User(username=username1,token=token1)
    user.set_password(password1)
    db.session.add(user)
    user1 = User(username=username2, token=token2)
    user1.set_password(password2)
    db.session.add(user1)

    for m in comments:
        comment = Comment(username=m['username'], time=m['time'], blog=m['blog'],blog_username=m['blog_username'],
                          content=m['content'], likes=m['likes'], visible=m['visible'])
        db.session.add(comment)

    for j in range(len(dates)):
        blog=Blog(blog=blogs[j],username=username1,date=dates[j],flow=flow[j])
        db.session.add(blog)

    db.session.commit()
    click.echo('Done.')


@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create user."""
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.set_password(password)
    else:
        click.echo('Creating user...')
        user = User(username=username, name='Admin')
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('Done.')
