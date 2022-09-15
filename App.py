from flask import Flask, url_for, session, render_template, request, redirect
from dotenv import load_dotenv
import json, os, random, time
from datetime import datetime

load_dotenv()
app = Flask(__name__)

# File Make / 기본 파일 생성
# os.mkdir("userInfo/")
# data = {
#     "host=?usersID" : []
# }

# with open('setting.json', 'w') as outfile:
#     json.dump(data, outfile, indent=4)

# Home / 홈
@app.route('/', methods=['get'])
def pageHome():
    return render_template('1Page_home.html', title = 'Home')


# Register / 회원가입
@app.route('/register', methods=['get'])
def pageRegister():
    _newUserID_ = request.args.get('registerID')
    _newUserPW_ = request.args.get('registerPW')
    _newUserEM_ = request.args.get('registerEmail')

    if _newUserID_ == None or _newUserPW_ == None:
        return render_template('2Page_register.html', title = 'Register your Account!', URL = url_for('pageHome'))

    else:
        with open('setting.json', 'r') as f: 
            programData = json.load(f)

        if _newUserID_ in programData['host=?usersID']:
            return render_template('_Page_state.html', title = 'Error', state = 'This ID already exists.', backName = 'back', back = url_for('pageRegister'))

        else:
            # User List / 유저 리스트 저장
            data = {
                "host=?usersID" : programData['host=?usersID']
            }
            programData['host=?usersID'].append(_newUserID_)

            with open('setting.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)

            # Save User Data / 유저 데이터 저장
            joinTime = str(datetime.now())

            data = {
                "id" : _newUserID_,
                "password" : _newUserPW_,
                "email" : _newUserEM_,
                "login?" : False,

                "coin" : 10,
                "exp" : 0,
                "level" : 1,
                "joinTime" : joinTime
            }

            with open(f'userInfo/{_newUserID_}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)

            # Complete Data / 데이터 조정 완료
            return render_template('_Page_state.html', title = 'Complete', state = 'Thanks For Register!', backName = 'Login Now', back = url_for('pageLogin'))


# Login / 로그인
@app.route('/login', methods=['get'])
def pageLogin():
    _userID_ = request.args.get('loginID')
    _userPW_ = request.args.get('loginPW')
    
    if _userID_ == None or _userPW_ == None:
        return render_template('3Page_login.html', title = 'Login!', URL = url_for('pageHome'))

    else:
        with open('setting.json', 'r') as f: 
            programData = json.load(f)

        if _userID_ in programData['host=?usersID']:
            with open(f'userInfo/{_userID_}.json') as f:
                userData = json.load(f)

            if userData['login?'] == False:
                if _userPW_ == userData['password']:
                    userData['login?'] = True
                    with open(f'userInfo/{_userID_}.json', 'w') as outfile:
                        json.dump(userData, outfile, indent=4)

                    return render_template('_Page_state.html', title = 'Good!', state = 'Login Complete - Delvelop...', backName = 'Okay!', back = url_for('pageProfile', userId = _userID_, userPw = _userPW_))

                else:
                    return render_template('_Page_state.html', title = 'Error', state = 'Wrong Login Info', backName = 'Login Again', back = url_for('pageLogin'))
            else:
                return render_template('_Page_state.html', title = 'Error', state = 'You Login Already.', backName = 'Profile', back = url_for('pageProfile', userId = _userID_, userPw = _userPW_))
        else:
            return render_template('_Page_state.html', title = 'Error', state = 'You entered wrong id or password.', backName = 'back', back = url_for('pageLogin'))

# Logout / 로그아웃
@app.route('/logout', methods=['get'])
def pageLogout():
    _userID_ = request.args.get('logoutID')
    _userPW_ = request.args.get('logoutPW')

    if _userID_ == None or _userPW_ == None:
        return render_template('5Page_logout.html', title = 'Logout', URL = url_for('pageHome'))

    else:
        with open('setting.json', 'r') as f: 
            programData = json.load(f)
        
        if _userID_ in programData['host=?usersID']:
            with open(f'userInfo/{_userID_}.json') as f:
                userData = json.load(f)

            if userData['login?'] == True:
                if _userPW_ == userData['password']:
                    userData['login?'] = False
                    with open(f'userInfo/{_userID_}.json', 'w') as outfile:
                        json.dump(userData, outfile, indent=4)

                    return render_template('_Page_state.html', title = 'Error', state = 'Done Logout', backName = 'Home', back = url_for('pageHome'))

                else:
                    return render_template('_Page_state.html', title = 'Error', state = 'You entered wrong id or password.', backName = 'Profile', back = url_for('pageProfile', userId = _userID_, userPw = _userPW_))
            else:
                return render_template('_Page_state.html', title = 'Error', state = 'You logout already.', backName = 'Home', back = url_for('pageHome'))
        else:
            return render_template('_Page_state.html', title = 'Error', state = 'This account is not register.', backName = 'Home', back = url_for('pageHome'))


# Profile / 프로필
@app.route('/profile/<userId>/<userPw>', methods=['get'])
def pageProfile(userId, userPw):
    with open(f'userInfo/{userId}.json') as f:
        userData = json.load(f)
        
    if userData['login?'] == True:
        return render_template(
            '4Page_profile.html', title = 'Profile - ' + userData['id'],
            userID = userId, userPW = userPw, sUserPw = '*' * int(len(userPw)),userEmail = userData['email'], 
            userCoin = userData['coin'], userExp = userData['exp'], userLevel = userData['level'],
            userJointime = userData['joinTime'], URL = url_for('pageHome')
        )

    else:
        return 'None'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)