# Module Import / 모듈 정의
from flask import Flask, url_for, session, render_template, request, redirect, Blueprint
from dotenv import load_dotenv
from datetime import datetime

import json, os, random, time

Account_Register = Blueprint("accountRegister", __name__, url_prefix="/account")

# Register / 회원가입
@Account_Register.route('/register', methods=['get'])
def pageRegister():
    _newUserID_ = request.args.get('registerID')
    _newUserPW_ = request.args.get('registerPW')
    _newUserEM_ = request.args.get('registerEmail')

    if _newUserID_ == None or _newUserPW_ == None: 
        return render_template('2Page_register.html', title = 'Register your Account!', URL = url_for('manage.pageHome'))
        
    else:
        with open('setting.json', 'r') as f: 
            programData = json.load(f)

        if _newUserID_ in programData['host=?usersID']:
            return render_template('_Page_state.html', title = 'Error', state = 'This ID already exists.', backName = 'back', back = url_for('accountRegister.pageRegister'))

        else:
            # User List / 유저 리스트 저장
            data = {
                "host=?usersID" : programData['host=?usersID']
            }
            programData['host=?usersID'].append(_newUserID_)

            with open('setting.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)

            # Save User Data / 유저 데이터 저장
            joinTime = str(datetime.now().date())

            data = {
                "id" : _newUserID_,
                "password" : _newUserPW_,
                "email" : _newUserEM_,
                "login?" : False,
                "code" : False,

                "coin" : 10,
                "exp" : 0,
                "level" : 1,    
                "joinTime" : joinTime,
            }

            with open(f'userInfo/{_newUserID_}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)

            # Complete Data / 데이터 조정 완료
            return render_template('_Page_state.html', title = 'Complete', state = 'Thanks For Register!', backName = 'Login Now', back = url_for('accountLogin.pageLogin'))
