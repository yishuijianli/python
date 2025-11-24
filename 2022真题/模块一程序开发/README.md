# 员工登录系统

> **本项目使用 AI 大模型辅助开发完成**

## 功能说明
1. 员工登录功能：登录成功后进入首页，否则提示登录失败
2. 增加员工信息功能：只有root用户（学号为1）才能添加员工信息
3. 员工列表查看功能：查看所有已添加的员工信息

## 账号信息
- 用户名：admin
- 密码：123456
- 学号：1（root用户，拥有添加员工权限）

## 项目结构
```
├── app.py              # 后端Flask服务器
├── login.html          # 登录页面
├── login.js            # 登录页面逻辑
├── style.css           # 登录页面样式
├── index.html          # 首页
├── index.js            # 首页逻辑
├── index.css           # 首页样式
├── requirements.txt    # Python依赖
└── README.md          # 说明文档
```

## 安装步骤

1. 安装Python依赖：
```bash
pip install -r requirements.txt
```

## 运行步骤

1. 启动后端服务器：
```bash
python app.py
```

2. 打开浏览器访问登录页面：
```
login.html
```
（直接双击打开或使用本地服务器）

## API接口

### 1. 登录接口
- 接口地址：http://127.0.0.1:8000/login
- 请求方法：POST
- 请求参数：
```json
{
    "username": "admin",
    "password": "123456"
}
```
- 返回结果（成功）：
```json
{
    "code": 200,
    "message": "登录成功",
    "data": {
        "username": "admin",
        "student_id": 1
    }
}
```

### 2. 添加员工接口
- 接口地址：http://127.0.0.1:8000/employee/add
- 请求方法：POST
- 权限要求：只有root用户（学号为1）才能添加
- 请求参数：
```json
{
    "student_id": 1,
    "name": "张三",
    "gender": "男",
    "age": 28,
    "department": "技术部",
    "position": "工程师",
    "phone": "13800138000",
    "email": "zhangsan@example.com",
    "hire_date": "2024-01-01"
}
```
- 返回结果（成功）：
```json
{
    "code": 200,
    "message": "员工信息添加成功",
    "data": {
        "id": 1
    }
}
```

### 3. 获取员工列表接口
- 接口地址：http://127.0.0.1:8000/employees
- 请求方法：GET
- 返回结果：
```json
{
    "code": 200,
    "message": "获取成功",
    "data": [
        {
            "id": 1,
            "name": "张三",
            "gender": "男",
            "age": 28,
            "department": "技术部",
            "position": "工程师",
            "phone": "13800138000",
            "email": "zhangsan@example.com",
            "hire_date": "2024-01-01"
        }
    ]
}
```

### 4. 获取单个员工信息接口
- 接口地址：http://127.0.0.1:8000/employee/{id}
- 请求方法：GET
- 返回结果：
```json
{
    "code": 200,
    "message": "获取成功",
    "data": {
        "id": 1,
        "name": "张三",
        "gender": "男",
        "age": 28,
        "department": "技术部",
        "position": "工程师",
        "phone": "13800138000",
        "email": "zhangsan@example.com",
        "hire_date": "2024-01-01"
    }
}
```

### 5. 修改员工信息接口
- 接口地址：http://127.0.0.1:8000/update
- 请求方法：POST
- 请求参数：
```json
{
    "id": 1,
    "name": "张三",
    "gender": "男",
    "age": 29,
    "department": "技术部",
    "position": "高级工程师",
    "phone": "13800138000",
    "email": "zhangsan@example.com",
    "hire_date": "2024-01-01"
}
```
- 返回结果（成功）：
```json
{
    "code": 200,
    "message": "员工信息修改成功",
    "data": {
        "id": 1
    }
}
```

## 使用说明

### 登录流程
1. 在登录页面输入用户名和密码（admin/123456）
2. 点击"登录"按钮
3. 登录成功后自动跳转到首页

### 添加员工流程
1. 在首页点击"增加员工信息"卡片
2. 系统会验证是否为root用户（学号为1）
3. 填写员工信息表单（带*为必填项）
4. 点击"保存"按钮提交
5. 添加成功后自动跳转到员工列表页面

### 查看员工列表
1. 在首页点击"查询员工信息"按钮
2. 查看所有已添加的员工信息

### 修改员工信息
1. 在首页点击"修改员工信息"按钮
2. 从下拉列表中选择要修改的员工
3. 修改员工信息表单
4. 点击"保存"按钮提交
5. 修改成功后自动跳转到员工列表页面

## 权限说明
- 只有root用户（学号为1的admin用户）才能添加员工信息
- 其他用户尝试访问添加页面会被拒绝并返回首页
- 所有登录用户都可以查看和修改员工信息

## 数据库
系统使用SQLite数据库，数据库文件为 `employees.db`，包含两个表：
- users：用户表（存储登录账号信息）
- employees：员工表（存储员工信息）
