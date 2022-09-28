# Module Import / 모듈 정의
from flask import Flask, url_for, session, render_template, request, redirect, Blueprint
from dotenv import load_dotenv
from datetime import datetime

import json, os, random, time

Account_Profile = Blueprint("accountProfile", __name__, url_prefix="/account")

# Profile / 프로필
@Account_Profile.route('/profile/<userId>/<userPw>', methods=['get'])
def pageProfile(userId, userPw):
    with open('setting.json', 'r') as f: 
        programData = json.load(f)

    if userId in programData['host=?usersID']:
        with open(f'userInfo/{userId}.json') as f:
            userData = json.load(f)
            
        if userData['login?'] == True:
            return render_template(
                '4Page_profile.html', title = 'Profile - ' + userData['id'],
                userID = userId, userPW = userPw, sUserPw = '*' * int(len(userPw)),userEmail = userData['email'], 
                userCoin = userData['coin'], userExp = userData['exp'], userLevel = userData['level'],
                userJointime = userData['joinTime'], URL = url_for('manage.pageHome'), userProfileUrl = None
            )

        else:
            return render_template('_Page_state.html', title = 'Error', state = 'Not Login', backName = 'Home', back = url_for('manage.pageHome'))

    else:
        return render_template('_Page_state.html', title = 'Error', state = 'No user.', backName = 'Home', back = url_for('manage.pageHome'))
