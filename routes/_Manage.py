# Module Import / 모듈 정의
from flask import Flask, url_for, session, render_template, request, redirect, Blueprint
from dotenv import load_dotenv
from datetime import datetime

import json, os, random, time

Manage = Blueprint("manage", __name__, url_prefix="/manage")


# Home / 홈
@Manage.route('/', methods=['get'])
def pageHome():
    return render_template('1Page_home.html', title = 'Home')

# Notce / 공지 페이지
@Manage.route('/notice', methods=['get'])
def pageManger():
    return render_template('6Page_manger.html', title = 'M', back = url_for('manage.pageHome')) 
