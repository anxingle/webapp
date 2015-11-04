##代码结构
#### /static
&nbsp;&nbsp;&nbsp;- - ->compute(静态文件)
&nbsp;&nbsp;&nbsp;- - ->Uploads(静态文件)
#### /templates
&nbsp;&nbsp;&nbsp;- - ->upload.html(HTML模板)
#### hello.py (Flask 框架主文件)
#### hello.dll (要调用的DLL文件)
##使用方法：
#### $->:python hello.py (确保已经安装Flask)
#### $->:Running on http://0.0.0.0:5000/ (press CTRL+C to quit...)
打开浏览器，在本机输入localhost:5000/就可以访问了。如果是局域网内其他PC，需要输入充当服务器的PC的IP:5000/ 。
