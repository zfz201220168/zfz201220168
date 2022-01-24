

# Team3项目：抢熬夜冠军

项目开始时间：2022/1/16
项目结束时间：2022/1/18
项目成员：胡纯涛、周凡钲，张淞钦

## 项目报告

* 拓展要求实现
  * 代码风格较好
  * 实现用户密码非明文存储
  * 前端对于页面进行了美化
  * 考虑到SQL注入等安全问题
  * 制作了基础的项目文档
  * 创意点
    * 在打卡时设置了留言功能
    * 登录与注册时增加了格式验证功能 
* 项目个人代码贡献
  * 项目成员：胡纯涛、周凡钲，张淞钦
    *  胡纯涛：后端基本功能实现，代码量约为50%
    *  周凡钲：前端功能实现，后端部分功能实现，代码量约为50%
    *  张淞钦：未贡献代码
* 项目中每个人扮演的角色
  * 都是打工人，先分工把自己的基本任务做完，然后再一起合作debug，debug的过程中大家互相领导，互相沟通各自所学的知识，来一起分析bug
* 建设性想法
  * 使用cookie缓存用户数据，从而可以在主页显示当前用户的用户名
  * 后端统一用一个变量flag来标识登录状态和注册状态，前端就只需从后端获取flag这一个变量从而设置弹窗提示内容

## 项目说明

项目结构如下：

```
.
├── app.py
├── config.py
├── database.py
├── form.py
├── models.py
├── static
│   ├── css
│   │   └── common.css
|   │   └── index.css
│   └── js
│   │   └── common.js
|   │   └── jquery.js
└── templates
	  └── homepage.html
	  └── register.html
	  └── login.html

```

这里是各个文件作用的简单说明：

* app.py: 在flask中，app.py是默认的程序入口，这里包含了flask应用的创建、一些依赖库的引用和路由；
* database.py: 这里用flask的数据库扩展类构建了一个实例；
* models.py: 创建数据库表模型users；
* config.py: 项目和远程数据库的配置信息；
* form.py：创建表单类，包含登录表单和注册表单两类
* static/
  * css/
    * common.css:：初始的css文件；
    * index.css：登录、注册页面美化的css文件；
  * js/
    * common.js：对前端进行表单验证，判断输入账户密码的格式是否正确；
    * jquery.js：jquery库；
* templates: 
  * homepage.html:登录成功后跳转到个人主页，也是排行榜所在页面；
  * register.html:注册页面；
  * login.html:登录页面；

数据结构设计：

```python
class Users(db.Model):  # 存储用户信息
    __tablename__ = 'users'  # the name of table

    username = db.Column(db.String(20), unique=True)
    ID = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(10))
    time = db.Column(db.DateTime)
    message = db.Column(db.String(20))
```

功能说明：

- 前段实现登录、注册以及排行榜页面的展示；
- 后端实现对数据库的增删查改，注册时加入用户，登录时判断用户名密码的正确性，以及根据打卡时间对用户进行排名；
- 前后端共同协作实现账户数据的交互以及页面跳转；

## **修改说明**

你可以自由地创建和编辑文件，但需注意：

* 不应删除已有文件或修改已有文件的名称；
* 保留程序的入口和路由。

