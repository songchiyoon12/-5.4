import os
from models import db
from flask import Flask, render_template ,request,redirect
from flask_sqlalchemy import SQLAlchemy
from models import User
from flask import session #세션
from flask_wtf.csrf import CSRFProtect #csrf
from form import RegisterForm
import crawling
import webbrowser

app = Flask(__name__)



@app.route('/')
def about():
    return render_template("main.html" )

@app.route('/index.html')
def hello():

    list_zum, list_zum_href = crawling.zum()
    list_today, list_today_href = crawling.today()
    list_clien, list_clien_href = crawling.clien()


    return render_template("index.html",
                           zum =list_zum,
                           today =list_today,
                           clien =list_clien,
                           zum_href = list_zum_href,
                           zum_len = len(list_zum),
                           today_href=list_today_href,
                           today_len = len(list_today),
                           clien_href=list_clien_href,
                           clien_len = len(list_clien))

       

@app.route('/albamon.html', endpoint='albamon.html')
def terms(): 
    return render_template('albamon.html')

@app.route('/register.html', endpoint='register.html',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit(): #내용 채우지 않은 항목이 있는지까지 체크
        usertable = User() 
        usertable.userid = form.data.get('userid')
        usertable.email = form.data.get('email')
        usertable.password = form.data.get('password')

        db.session.add(usertable) #DB저장
        db.session.commit() #변동사항 반영
        
        return "/" 
    return render_template('register.html', form=form)



@app.route('/albahaven.html', endpoint='albahaven.html')
def terms(): 
    return render_template('albahaven.html')

@app.route('/editor1.html', endpoint='editor1.html')
def terms(): 
    return render_template('editor1.html')

@app.route('/editor2.html', endpoint='editor2.html')
def terms(): 
    return render_template('editor2.html')

@app.route('/editor3.html', endpoint='editor3.html')
def terms(): 
    return render_template('editor3.html')

@app.route('/editor4.html', endpoint='editor4.html')
def terms(): 
    return render_template('editor4.html')

@app.route('/editor5.html', endpoint='editor5.html')
def terms(): 
    return render_template('editor5.html')


if __name__ == '__main__':

     basedir = os.path.abspath(os.path.dirname(__file__)) #현재 파일이 있는 디렉토리 절대 경로
     dbfile = os.path.join(basedir, 'db.sqlite') #데이터베이스 파일을 만든다

     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
     app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True #사용자에게 정보 전달완료하면 teadown. 그 때마다 커밋=DB반영
     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #추가 메모리를 사용하므로 꺼둔다
     app.config['SECRET_KEY']='asdfasdfasdfqwerty'

     csrf = CSRFProtect()
     csrf.init_app(app)

     db = SQLAlchemy() #SQLAlchemy를 사용해 데이터베이스 저장
     db.init_app(app) #app설정값 초기화
     db.app = app #Models.py에서 db를 가져와서 db.app에 app을 명시적으로 넣는다
     db.create_all() #DB생성

   

    
     app.run('127.0.0.1' ,port =8080)

