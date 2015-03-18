#cby_py_pt
#该程序在苹果系统OS X 10.9开发，使用PyCharm作为IDE.
/doc/design：程序概要设计说明。

assignment_pingtai.sql包含数据定义语句。程序运行前，请将数据库定义导入mysql数据库。

/conf/mysql.conf 包含了数据库连接信息，请配置为合适参数。

deploy.sh：在执行该文件前，请将CGIDIR变量指向正确目录。使用合适的权限执行该文件。

程序的入口界面类似如下：
http://localhost/cgi-bin/index.py

第三方程序访问接口如下：
http://localhost/cgi-bin/getimage.py?u=用户名
