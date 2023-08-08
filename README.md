# 基于DAD-3DHeads 的特征点标记、姿态评估、头部3D对齐Demo

## 写在前面

***
+ 工作中遇到，简单整理
+ 该模型 `Demo` 目前只支持单个人脸的预测
+ 理解不足小伙伴帮忙指正


**<font color="009688"> 对每个人而言，真正的职责只有一个：找到自我。然后在心中坚守其一生，全心全意，永不停息。所有其它的路都是不完整的，是人的逃避方式，是对大众理想的懦弱回归，是随波逐流，是对内心的恐惧 ——赫尔曼·黑塞《德米安》**</font>

***

## 环境安装

克隆项目

[https://github.com/PinataFarms/DAD-3DHeads.git](https://github.com/PinataFarms/DAD-3DHeads.git)


模型文件，如果没有科学上网，需要提前下载，放到家目录下: `C:\Users\liruilong\.dad_checkpoints`


`dad_3dheads.trcd`: [https://media.pinatafarm.com/public/research/dad-3dheads/dad_3dheads.trcd](https://media.pinatafarm.com/public/research/dad-3dheads/dad_3dheads.trcd
)


创建虚拟环境
```bash
(base) C:\Users\liruilong\Documents\GitHub>cd DAD-3DHeads_Demo

(base) C:\Users\liruilong\Documents\GitHub\DAD-3DHeads_Demo>conda create --name DAD-3DHeads python=3.8

(base) C:\Users\liruilong\Documents\GitHub\DAD-3DHeads_Demo>conda activate DAD-3DHeads

(DAD-3DHeads) C:\Users\liruilong\Documents\GitHub\DAD-3DHeads_Demo>pip install -r requirements.txt  -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
Looking in indexes: http://pypi.douban.com/simple/
```
## 运行 Demo 测试

68 个特征点标记

```bash
(DAD-3DHeads) C:\Users\liruilong\Documents\GitHub\DAD-3DHeads_Demo> python demo.py images\\demo_heads\\1.jpeg outputs 68_landmarks
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/4ac370c1ab3b4b7bbfd3a2236170f3b4.png)


面部曲面标记
```bash
(DAD-3DHeads) C:\Users\liruilong\Documents\GitHub\DAD-3DHeads_Demo> python demo.py images/demo_heads/1.jpeg outputs face_mesh
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/b64462fecc694a999ed891c320f18c2c.png)

头部3D曲面标记
```bash
python demo.py images/demo_heads/1.jpeg outputs head_mesh
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/0841956e76d641aeaa6cd3c8ed36839f.png)

姿态评估
```py
python demo.py images/demo_heads/1.jpeg outputs pose
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/7b8a6e66e2af424590ad8c5cf1c5142b.png)


其他的所有 Demo



```py
python demo.py <path/to/input/image.png> <path/to/output/folder> <type_of_output>

# Visualize 68 2D face landmarks
python demo.py images/demo_heads/1.jpeg outputs 68_landmarks

# Visualize 191 2D face landmarks
python demo.py images/demo_heads/1.jpeg outputs 191_landmarks

# Visualize 445 2D face landmarks
python demo.py images/demo_heads/1.jpeg outputs 445_landmarks

# Visualize face mesh
python demo.py images/demo_heads/1.jpeg outputs face_mesh

# Visualize head mesh
python demo.py images/demo_heads/1.jpeg outputs head_mesh

# Visualize head pose
python demo.py images/demo_heads/1.jpeg outputs pose

# Get 3D mesh .obj file
python demo.py images/demo_heads/1.jpeg outputs 3d_mesh

# Get flame parameters .json file
python demo.py images/demo_heads/1.jpeg outputs flame_params
```



## 博文部分内容参考

© 文中涉及参考链接内容版权归原作者所有，如有侵权请告知，这是一个开源项目，如果你认可它，不要吝啬星星哦 :)


***
https://github.com/PinataFarms/DAD-3DHeads

***

© 2018-2023 liruilonger@gmail.com, All rights reserved. 保持署名-非商用-相同方式共享(CC BY-NC-SA 4.0)
