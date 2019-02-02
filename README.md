## 介绍
专门记录python书写的web页面

### 系统环境

- running inside Linux
- pyhton (>=2.7) OR (>=3.6)

### 列表
1. 程序部署 --- 可以自动化部署zabbix、redis、logstash等基础组件
2. 加班管理 --- 记录加班时常，领导可查
3. 周报管理 --- 周报管理，记录周报信息，领导可查
4. 资产管理 --- 资产管理，记录xen虚拟机和物理机资产信息

### 环境准备
- running inside Linux
- python ( >= 2.7 )
- pip install Django==1.10.1
- pip install django-extensions
- pip install psycopg2
- yum install -y ansible 2.7.1
- pip install ansible==2.3.1
- yum install gcc
- yum install python-devel
- pip install pymssql
- pip install psycopg2-binary

### 启动方法
  ```
>\# cd python-web/deploy_manager
>\# python manage.py makemigrations  --empty blog
>\# python manage.py makemigrations
>\# python manage.py migrate
>\# python manage.py createsuperuser
>\# python manage.py runserver 0.0.0.0:8000

  ```

#### 界面预览
1. 浏览器打开http://IP:8000/admin  输入刚才创建的账号密码

![](https://raw.githubusercontent.com/goywzl/sre-system/master/screenshots/admin-login.png)

2. 创建普通账号，最好多创建一个admin管理账号，admin用户有特效
![](https://raw.githubusercontent.com/goywzl/sre-system/master/screenshots/create-user.png)

3. 由于后面需要用到first用户名称来识别员工，所以配置first名，别忘了点右下角的保存
![](https://raw.githubusercontent.com/goywzl/sre-system/master/screenshots/user-first-name.png)

4.浏览器打开http://IP:8000 并输入创建的test用户登陆

![](https://raw.githubusercontent.com/goywzl/sre-system/master/screenshots/user-lgoin.png)

5.部署应用程序，需要连动ansible-playbook，我这里把我的playbook删掉了，所以你需要自己看代码在配置

![](https://raw.githubusercontent.com/goywzl/sre-system/master/screenshots/deploy-1.png)

6.查看部署记录

![](https://raw.githubusercontent.com/goywzl/sre-system/master/screenshots/deploy-2.png)

7.加班管理，可以选择时间进行加班调休，当然必须领导同意才能有这个东西

![](https://raw.githubusercontent.com/goywzl/sre-system/master/screenshots/worker-1.png)

8.加班查询，可以查看自己的提交的历史，以及还剩下多少加班时长，admin用户有特效哦

![](https://raw.githubusercontent.com/goywzl/sre-system/master/screenshots/worker-2.png)

9.填写周报信息，可以记录一周的工作

![](https://raw.githubusercontent.com/goywzl/sre-system/master/screenshots/weekly-1.png)

10.查看周报信息，查询自己每周的工作，admin用户有特效哦

![](https://raw.githubusercontent.com/goywzl/sre-system/master/screenshots/weekly-2.png)

11.资产管理，手动更新物理机资产，也可以跑脚本，有隐藏接口，需要自己去挖掘了

![](https://raw.githubusercontent.com/goywzl/sre-system/master/screenshots/property-1.png)

12.查看资产信息，可以进行搜索功能，用着还不错

![](https://raw.githubusercontent.com/goywzl/sre-system/master/screenshots/property-2.png)

13.查看操作历史，防止谁删除或者误操作，记录一切你的行为

![](https://raw.githubusercontent.com/goywzl/sre-system/master/screenshots/property-3.png)

14.由于公司使用xen，并且可以无秘钥登陆，所以使用ansible进行抓取信息，只需要输入一个xen池中的一台ip即可，隐藏功能，如果你有十个池，你可以一行一个xen池的IP

![](https://raw.githubusercontent.com/goywzl/sre-system/master/screenshots/property-4.png)

### 联系方式
mail: xiaohui920@sina.cn
