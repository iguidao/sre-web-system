## 介绍
专门记录python书写的web页面

### 系统环境

- running inside Linux
- pyhton (>=2.7) OR (>=3.6)

### 列表
1. 程序部署
    部署管理，可以自动化部署zabbix、redis、logstash等基础组件
2. 加班管理
    加班管理，记录加班时常，领导可查
3. 周报管理
    周报管理，记录周报信息，领导可查
4. 资产管理
    资产管理，记录xen虚拟机和物理机资产信息

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
1. 浏览器打开http://IP:8000
2. 输入刚才创建的账号密码

![](https://raw.githubusercontent.com/goywzl/python-web/master/screenshots/pytyhon-web-login.png)

3. 部署界面如下图，需要自行配置ansible-playbook，并且需要自己查看查看代码如何实现python链接ansible
![](https://raw.githubusercontent.com/goywzl/python-web/master/screenshots/deploy-1.png)

4. 部署历史记录界面如下图，目前是空
![](https://raw.githubusercontent.com/goywzl/python-web/master/screenshots/deploy-2.png)




### 联系方式
mail: xiaohui920@sina.cn
