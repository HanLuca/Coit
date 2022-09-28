# Module Import / 모듈 정의
from flask import Flask, url_for, session, render_template, request, redirect, Blueprint
from dotenv import load_dotenv
from datetime import datetime
from routes import app

import json, os, random, time


@app.route('/')
def pageStart():
    return redirect(url_for('manage.pageHome'))

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 9999, debug = True)