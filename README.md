# aliyun-wxwork
将阿里云服务器预警信息转发到企业微信群机器人

一、登录阿里云--函数计算，使用flask-web模板创建一个函数
  ![image](https://user-images.githubusercontent.com/66998320/119070771-38842600-ba1b-11eb-8963-cc3558c020c4.png)

二、将main.py文件内的代码全部替换，代码内替换成你自己的企微机器人webhook

三、设置时间环境变量，{"TZ":"Asia/Shanghai"}
  ![image](https://user-images.githubusercontent.com/66998320/119071209-f7404600-ba1b-11eb-8fd9-fc1efbcdecbc.png)

  ![image](https://user-images.githubusercontent.com/66998320/119071110-ceb84c00-ba1b-11eb-85dd-4b2ae18ec106.png)
  
四、触发器的地址就是你需要回调的地址
  ![image](https://user-images.githubusercontent.com/66998320/119071535-92d1b680-ba1c-11eb-84fe-f8fed42d846a.png)

五、阿里云报警规则填写填写函数回调地址即可
  ![image](https://user-images.githubusercontent.com/66998320/119071704-e217e700-ba1c-11eb-9b28-6372672d48e7.png)

  
效果

  
![image](https://user-images.githubusercontent.com/66998320/119071340-353d6a00-ba1c-11eb-828d-6ef03649261e.png)
