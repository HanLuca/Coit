# Module Import / 모듈 정의
from flask import Flask, url_for, session, render_template, request, redirect, Blueprint
from dotenv import load_dotenv
from datetime import datetime

import json, os, random, time

Account_Login = Blueprint("accountLogin", __name__, url_prefix="/account")

# Login / 로그인
@Account_Login.route('/login', methods=['get'])
def pageLogin():
    _userID_ = request.args.get('loginID')
    _userPW_ = request.args.get('loginPW')
    
    if _userID_ == None or _userPW_ == None:
        return render_template('3Page_login.html', title = 'Login!', URL = url_for('manage.pageHome'))

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

                    return render_template('_Page_state.html', title = 'Good!', state = 'Login Complete - Delvelop...', backName = 'Okay!', back = url_for('accountProfile.pageProfile', userId = _userID_, userPw = _userPW_))

                else:
                    return render_template('_Page_state.html', title = 'Error', state = 'Wrong Login Info', backName = 'Login Again', back = url_for('accountLogin.pageLogin'))
            else:
                return render_template('_Page_state.html', title = 'Error', state = 'You Login Already.', backName = 'Profile', back = url_for('accountProfile.pageProfile', userId = _userID_, userPw = _userPW_))
        else:
            return render_template('_Page_state.html', title = 'Error', state = 'You entered wrong id or password.', backName = 'back', back = url_for('accountLogin.pageLogin'))

# Logout / 로그아웃
@Account_Login.route('/logout', methods=['get'])
def pageLogout():
    _userID_ = request.args.get('logoutID')
    _userPW_ = request.args.get('logoutPW')

    if _userID_ == None or _userPW_ == None:
        return render_template('5Page_logout.html', title = 'Logout', URL = url_for('manage.pageHome'))

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

                    return render_template('_Page_state.html', title = 'Error', state = 'Done Logout', backName = 'Home', back = url_for('manage.pageHome'))

                else:
                    return render_template('_Page_state.html', title = 'Error', state = 'You entered wrong id or password.', backName = 'Profile', back = url_for('accountProfile.pageProfile', userId = _userID_, userPw = _userPW_))
            else:
                return render_template('_Page_state.html', title = 'Error', state = 'You logout already.', backName = 'Home', back = url_for('manage.pageHome'))
        else:
            return render_template('_Page_state.html', title = 'Error', state = 'This account is not register.', backName = 'Home', back = url_for('manage.pageHome'))
