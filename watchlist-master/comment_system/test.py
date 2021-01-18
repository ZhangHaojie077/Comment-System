from comment_system.models import Comment ,User ,Blog
from flask_login import login_user, login_required, logout_user, current_user
date_list=[]
from sqlalchemy import and_
import datetime
a=datetime.datetime.now().strftime('%Y-%m-%d')

print(a[-4:])
