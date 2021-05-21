# aliyun-wxwork
将阿里云服务器预警信息转发到企业微信群机器人

一、登录阿里云--函数计算，使用flask-web模板创建一个函数
  ![image](https://user-images.githubusercontent.com/66998320/119070771-38842600-ba1b-11eb-8963-cc3558c020c4.png)

二、将main.py文件内的代码全部替换，代码内替换成你自己的企微机器人webhook

三、设置时间环境变量，{"TZ":"Asia/Shanghai"}
  ![image](https://user-images.githubusercontent.com/66998320/119071209-f7404600-ba1b-11eb-8fd9-fc1efbcdecbc.png)

  ![image](https://user-images.githubusercontent.com/66998320/119071110-ceb84c00-ba1b-11eb-85dd-4b2ae18ec106.png)
  
效果

  
![image](https://user-images.githubusercontent.com/66998320/119071340-353d6a00-ba1c-11eb-828d-6ef03649261e.png)
