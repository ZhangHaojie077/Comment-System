# -*- coding: utf-8 -*-
from flask import render_template, request, url_for, redirect, flash,jsonify
from flask_login import login_user, login_required, logout_user, current_user
import hashlib
import os
import datetime
from sqlalchemy import and_

import faker
from comment_system.tools import generate_token
from comment_system import app, db
from comment_system.models import User, Comment ,Blog
json_meta1 = {"msg": "登录成功","status":200}
json_meta2 = {"msg": "登录失败", "status": 460}

global curent_username
curent_username=''
#用户登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    global curent_username
    token_res=hashlib.sha1(os.urandom(24)).hexdigest()

    if request.method == 'POST':
        post_data = request.get_json()
        username = post_data['username']
        password = post_data['password']
        #如果输入为空
        if not username or not password:
            flash('Invalid input.')
            return jsonify({"meta":json_meta2})

        user = User.query.filter_by(username=username).first()
        #如果用户不存在
        if user is None:
            return jsonify({"meta": json_meta2})

        #如果用户民和密码完全正确
        if username == user.username and user.validate_password(password):
            print(username)
            curent_username=username
            login_user(user)
            flash('Login success.')
            user.token=token_res
            json_token_username = {"token": token_res,'username':username}
            db.session.commit()
            return jsonify({"data":json_token_username,"meta":json_meta1})

    return jsonify({"meta":json_meta2})

#用户登录
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    global curent_username
    token_res=hashlib.sha1(os.urandom(24)).hexdigest()

    if request.method == 'POST':
        post_data = request.get_json()
        username = post_data['username']
        password = post_data['password']
        #如果输入为空
        if not username or not password:
            flash('Invalid input.')
            return jsonify({"meta":json_meta2})

        user = User.query.filter_by(username=username).first()
        #如果用户存在,则不能注册
        if user is not None:
            return jsonify({"meta": json_meta2})
        #如果用户不存在，给他注册
        else:
            curent_username=username
            user1 = User(username=username, token=token_res)
            user1.set_password(password)
            json_token_username = {"token": token_res,'username':username}
            db.session.add(user1)
            db.session.commit()
            return jsonify({"data":json_token_username,"meta":json_meta1})
    return jsonify({"meta":json_meta2})


#评论列表展示
@app.route('/comments', methods=['GET', 'POST','PUT','DELETE'])
def comment_show():
    comments_list = []
    total = 0
    #将数据库数据以json的格式全部返回
    if request.method == 'GET':
        blog_search=request.args.get("blog")
        if blog_search == '':
            comments = Comment.query.filter(Comment.blog_username==curent_username).all()
        else:
            comments = Comment.query.filter(and_(Comment.blog==blog_search,Comment.blog_username==curent_username)).all()
        for comment in comments:
            comments_list.append({'id':comment.id,'username': comment.username, 'time': comment.time,
            'blog': comment.blog,'content': comment.content, 'likes': comment.likes, 'visible': comment.visible})
        total=len(comments)
        return jsonify({
            "data":{"comments" :comments_list,"total":total
        },
            "meta":json_meta1
        })

    if request.method == 'PUT':
        put_data=request.get_json()
        id=put_data['id']
        visible=put_data['visible']
        comment=Comment.query.get(id)
        comment.visible=visible
        db.session.commit()
        return jsonify({"meta":json_meta1})

    if request.method == 'DELETE':
        delete_data=request.get_json()
        id=delete_data['params']['id']
        comment = Comment.query.get(id)
        db.session.delete(comment)
        db.session.commit()
        return jsonify({"meta":json_meta1})


#每日流量与博客流量统计
@app.route('/statistic', methods=['GET', 'POST','PUT','DELETE'])
def Traffic_Statistics():
    date_list = []
    date_flow_value = []
    blog_list=[]
    blog_flow_value=[]
    if request.method == 'GET':
        blogs=Blog.query.filter(Blog.username==curent_username).all()
        for blog in blogs:
            if blog.blog not in blog_list:
                blog_list.append(blog.blog)
                value1=0
                for t in Blog.query.filter(and_(Blog.username==curent_username,Blog.blog == blog.blog)).all():
                    value1+=t.flow
                blog_flow_value.append(value1)

        blogs = Blog.query.filter(Blog.username == curent_username).order_by(Blog.date).all()
        blog_copy=[]
        for blog in blogs:
            if blog not in blog_copy:
                date_list.append(blog.date)
                value1 = 0
                for t in Blog.query.filter(and_(Blog.username == curent_username,Blog.date == blog.date)).all():
                    value1+=t.flow
                    blog_copy.append(t)
                date_flow_value.append(value1)
        date_list.remove('1-10')
        date_list.remove('1-18')
        del date_flow_value[1]
        del date_flow_value[2]
        date_list.append('1-10')
        date_list.append('1-18')
        date_flow_value.append(1)
        date_flow_value.append(1)
    return jsonify({'data':{"xAxisData1": date_list,"xAxisData2": blog_list,
                    "seriesData1": date_flow_value,"seriesData2": blog_flow_value},"meta":json_meta1})


#前端用户注册自己的博客
@app.route('/login_front', methods=['GET', 'POST'])
def login_front():
    if request.method == 'POST':
        post_data = request.get_json()
        username = post_data['username']
        password = post_data['password']
        blog_username=post_data['blogusername']
        blog_name=post_data['blogname']
        #如果输入为空
        if not username or not password:
            flash('Invalid input.')
            return jsonify({"meta":json_meta2})

        user = User.query.filter_by(username=username).first()
        #如果用户不存在
        if user is None:
            return jsonify({"meta": json_meta2})

        #如果用户民和密码完全正确
        if username == user.username and user.validate_password(password):
            print(username)
            curent_username=username
            flash('Login success.')
            json_token_username = {"token": user.token,'username':username}
            return jsonify({"data":json_token_username,"meta":json_meta1})

    return jsonify({"meta":json_meta2})


#前端用户注册自己的博客
@app.route('/signin_front', methods=['GET', 'POST'])
def signin_front():
    if request.method == 'POST':
        post_data = request.get_json()
        username = post_data['username']
        password = post_data['password']
        blog_username=post_data['blogusername']
        blog_name=post_data['blogname']
        #如果输入为空
        if not username or not password:
            flash('Invalid input.')
            return jsonify({"meta":json_meta2})

        user = User.query.filter_by(username=username).first()
        #如果用户不存在
        if user is None:
            return jsonify({"meta": json_meta2})

        #如果用户民和密码完全正确
        if username == user.username and user.validate_password(password) and username==blog_username:
            print(username)
            curent_username=username
            a = datetime.datetime.now().strftime('%Y-%m-%d')
            new_blog=Blog(username=username,blog=blog_name,date=a[-4:],flow=1)
            db.session.add(new_blog)
            db.session.commit()
            flash('Login success.')
            json_token_username = {"token": user.token,'username':username}
            return jsonify({"data":json_token_username,"meta":json_meta1})

    return jsonify({"meta":json_meta2})

#评论列表展示
@app.route('/comments1', methods=['GET', 'POST','PUT','DELETE'])
def front_comment_show():
    comments_list = []
    total = 0
    #将数据库数据以json的格式全部返回
    if request.method == 'GET':
        user_name = request.args.get('username')
        blog_username=request.args.get("blogusername")
        blog_name = request.args.get("blogname")

        comments = Comment.query.filter(and_(Comment.blog_username==blog_username,Comment.blog==blog_name)).all()
        for comment in comments:
            comments_list.append({'id':comment.id,'username': comment.username, 'time': comment.time,
            'blog': comment.blog,'content': comment.content, 'likes': comment.likes, 'visible': comment.visible})
        total=len(comments)
        return jsonify({
            "data":{"comments" :comments_list,"total":total
        },
            "meta":json_meta1
        })

    if request.method == 'PUT':
        put_data=request.get_json()
        print(put_data)
        blog_username = put_data["blogusername"]
        blog_name = put_data["blogname"]
        user_name = put_data['username']
        context = put_data['comment']
        a = datetime.datetime.now().strftime('%Y-%m-%d')
        comment=Comment(username=user_name,time=a[-4:],blog_username=blog_username,
                        blog=blog_name,
                        content=context,likes=0,visible=True)
        db.session.add(comment)
        db.session.commit()
        return jsonify({"meta":json_meta1})



