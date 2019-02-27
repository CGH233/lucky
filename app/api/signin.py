#coding:utf-8
from . import api
from ..ccnu2 import login_once
from flask import request,jsonify,Response
import json

@api.route('/signin/', methods = ['POST'])
def signin():
    if request.method == 'POST':
        username = request.get_json().get("sno")
        password = request.get_json().get("password")
        if username is not None:
            response = login_once(username, password)
            if response is not None:
                response = eval(response)
                major = response.get('data').get('roleDepartment').get('departmentName')
                gender = response.get('data').get('userInfoVO').get('userInfo').get('sex')
                name = response.get('data').get('roleDepartment').get('realname') 
                if gender == '男':
                    gender = 0
                else:
                    gender = 1
                return jsonify({
                    "code":0,
                    "msg":"登陆成功",
                    "data":{
                        "sno":username,
                        "name":name,
                        "gender":gender,
                        "major":major,
                    },
                }),200
            else:
                return jsonify({
                    "code":"-1",
                    "msg":"密码错误"
                }),401
        else:
            return jsonify({
                "code":"1",
                "msg":"登录异常"
                }),403
