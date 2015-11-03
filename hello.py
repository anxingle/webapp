# -*- coding: utf-8 -*-

import os
import mimetypes
from tempfile import mktemp
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, redirect, url_for
import ctypes
from ctypes import *

app = Flask(__name__)

UPLOAD_FOLDER = 'static/Uploads'
SOURCE_FOLDER = 'static/compute'
ALLOWED_MIMETYPES = {'image/jpeg', 'image/png', 'image/gif'}
func = cdll.LoadLibrary('Hello.dll')
Index_pic = ['login.jpg','abc1.jpg','abc2.gif','abc3.jpg','abc4.jpg','abc5.jpg','abc6.jpg','abc7.jpg', \
'abc8.jpg','abc9.jpg','abc10.jpg','abc11.jpg','abc12.jpg','abc13.jpg']

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
            return render_template('upload.html',img='%s/%s'%(UPLOAD_FOLDER,Index_pic[0]),img1='%s/%s'%(UPLOAD_FOLDER,Index_pic[1]), \
                img2='%s/%s'%(UPLOAD_FOLDER,Index_pic[2]),img3='%s/%s'%(UPLOAD_FOLDER,Index_pic[3]),\
                img4='%s/%s'%(UPLOAD_FOLDER,Index_pic[4]),img5='%s/%s'%(UPLOAD_FOLDER,Index_pic[13]),\
                img6='%s/%s'%(UPLOAD_FOLDER,Index_pic[6]),img7='%s/%s'%(UPLOAD_FOLDER,Index_pic[7]), \
                img8='%s/%s'%(UPLOAD_FOLDER,Index_pic[8]),img9='%s/%s'%(UPLOAD_FOLDER,Index_pic[9]),\
                img10='%s/%s'%(UPLOAD_FOLDER,Index_pic[10]),img11='%s/%s'%(UPLOAD_FOLDER,Index_pic[11]), \
                img12='%s/%s'%(UPLOAD_FOLDER,Index_pic[12]) \
                )
    elif request.method == 'POST':
        str0 = func.show()
        size = -1
        str0 = ctypes.string_at(str0,size)
        str1 = str0.decode('utf-8')
        result_pic = str1.split(',')
        #print(str1)
        f = request.files['file']
        fname = mktemp(suffix='_', prefix='u', dir=UPLOAD_FOLDER) + \
            secure_filename(f.filename)
        f.save(fname)
        if mimetypes.guess_type(fname)[0] in ALLOWED_MIMETYPES:
            return render_template('upload.html',img=fname,img1='%s/%s'%(SOURCE_FOLDER,result_pic[7]), \
                img2='%s/%s'%(SOURCE_FOLDER,result_pic[1]),img3='%s/%s'%(SOURCE_FOLDER,result_pic[8]),\
                img4='%s/%s'%(SOURCE_FOLDER,result_pic[3]),img5='%s/%s'%(SOURCE_FOLDER,result_pic[4]),\
                img6='%s/%s'%(SOURCE_FOLDER,result_pic[5]),img7='%s/%s'%(SOURCE_FOLDER,result_pic[6]), \
                img8='%s/%s'%(SOURCE_FOLDER,result_pic[1]),img9='%s/%s'%(SOURCE_FOLDER,result_pic[0]),\
                img10='%s/%s'%(SOURCE_FOLDER,result_pic[9]),img11='%s/%s'%(SOURCE_FOLDER,result_pic[10]), \
                img12='%s/%s'%(SOURCE_FOLDER,result_pic[11]) \
                )
        else:
            os.remove(fname)
            return redirect(url_for('upload'), 302)


@app.route('/')
def index():
    return redirect(url_for('upload'), 302)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
