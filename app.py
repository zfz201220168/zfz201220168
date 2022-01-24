from flask import Flask, render_template, request, Response, redirect, url_for, make_response, flash
import config
from database import db
import models
from datetime import datetime
from form import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
user = models.Users


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])  # 登录界面
def login():
    if request.method == 'POST':  # 登录
        form = LoginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            u = user.query.filter_by(username=username).first()
            if u:
                if check_password_hash(u.password, password):
                    temp = show_list(username, 2)
                    response = make_response(temp)
                    response.delete_cookie('username')
                    response.set_cookie('username', username)
                    return response  # 验证通过，重定向至排行榜界面
                else:
                    return render_template('login.html', flag=1)  # 密码错误
            else:
                return render_template('login.html', flag=0)  # 用户名不存在
    return render_template('login.html', flag=-1)  # 无操作，不弹窗


@app.route('/register', methods=['GET', 'POST'])  # 注册界面
def register():
    if request.method == 'POST':  # 注册行为
        form = RegisterForm(request.form)
        if form.validate():
            if user.query.filter_by(username=form.username.data).first():
                return render_template('register.html', flag=4)  # 用户名已存在
            else:
                username = form.username.data
                password = form.password.data
                hash_password = generate_password_hash(password)
                add_new_user(username, hash_password, len(user.query.all()))
                return render_template('login.html', flag=3)  # 注册成功
        else:
            return render_template('register.html')  # 注册失败
    return render_template('register.html', flag=-1)  # 无操作，不弹窗


@app.route('/rank', methods=['GET', 'POST'])  # rank
def ranklist():  # put application's code here
    if request.method == 'GET':
        return show_list('', -1)
    else:
        message = request.form.get('message')
        click_to_clock(get_username(), message)
        return show_list(get_username(), 5)


def show_list(username, flag):
    result = user.query.order_by(user.time.desc()).all()
    for i in range(len(result)):
        result[i].rank = i + 1
    return render_template('homepage.html', list=result, name=username, flag=flag)  # 登录成功，弹窗


def add_new_user(username, number, id):  # 注册
    new_p = user(username=username, password=number, ID=id)
    db.session.add(new_p)
    db.session.commit()
    db.session.close


def click_to_clock(name, message):
    db.session.query(user).filter_by(username=name).update({'time': get_time()})
    if message:
        db.session.query(user).filter_by(username=name).update({'message': message})
    else:
        db.session.query(user).filter_by(username=name).update({'message': '熬夜冠军非我莫属'})
    db.session.commit()
    db.session.close()


def get_username():
    username = request.cookies.get('username')
    return username


def get_time():
    return datetime.now()


if __name__ == '__main__':
    app.run()
