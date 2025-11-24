from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
CORS(app)

# 数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 用户模型
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    student_id = db.Column(db.Integer, unique=True, nullable=False)  # 学号
    
# 员工模型
class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100))
    hire_date = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

# 初始化数据库
with app.app_context():
    db.create_all()
    # 创建root用户（学号为1）
    if not User.query.filter_by(username='admin').first():
        root_user = User(username='admin', password='123456', student_id=1)
        db.session.add(root_user)
        db.session.commit()

@app.route('/login', methods=['POST'])
def login():
    """
    员工登录API
    接收用户名和密码，验证后返回登录结果
    """
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    
    # 从数据库验证用户
    user = User.query.filter_by(username=username, password=password).first()
    
    if user:
        return jsonify({
            'code': 200,
            'message': '登录成功',
            'data': {
                'username': username,
                'student_id': user.student_id
            }
        })
    else:
        return jsonify({
            'code': 401,
            'message': '用户名或密码错误'
        }), 401

@app.route('/employee/add', methods=['POST'])
def add_employee():
    """
    添加员工信息API
    只有root用户（学号为1）才能添加员工
    """
    data = request.get_json()
    
    # 验证是否为root用户
    student_id = data.get('student_id')
    if student_id != 1:
        return jsonify({
            'code': 403,
            'message': '权限不足，只有root用户才能添加员工'
        }), 403
    
    # 获取员工信息
    try:
        employee = Employee(
            name=data.get('name'),
            gender=data.get('gender'),
            age=data.get('age'),
            department=data.get('department'),
            position=data.get('position'),
            phone=data.get('phone'),
            email=data.get('email', ''),
            hire_date=data.get('hire_date')
        )
        
        db.session.add(employee)
        db.session.commit()
        
        return jsonify({
            'code': 200,
            'message': '员工信息添加成功',
            'data': {
                'id': employee.id
            }
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'code': 500,
            'message': f'添加失败：{str(e)}'
        }), 500

@app.route('/employees', methods=['GET'])
def get_employees():
    """
    获取所有员工信息
    """
    employees = Employee.query.all()
    employee_list = []
    
    for emp in employees:
        employee_list.append({
            'id': emp.id,
            'name': emp.name,
            'gender': emp.gender,
            'age': emp.age,
            'department': emp.department,
            'position': emp.position,
            'phone': emp.phone,
            'email': emp.email,
            'hire_date': emp.hire_date
        })
    
    return jsonify({
        'code': 200,
        'message': '获取成功',
        'data': employee_list
    })

@app.route('/employee/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    """
    获取单个员工信息
    """
    employee = Employee.query.get(emp_id)
    
    if not employee:
        return jsonify({
            'code': 404,
            'message': '员工不存在'
        }), 404
    
    return jsonify({
        'code': 200,
        'message': '获取成功',
        'data': {
            'id': employee.id,
            'name': employee.name,
            'gender': employee.gender,
            'age': employee.age,
            'department': employee.department,
            'position': employee.position,
            'phone': employee.phone,
            'email': employee.email,
            'hire_date': employee.hire_date
        }
    })

@app.route('/update', methods=['POST'])
def update_employee():
    """
    修改员工信息API
    """
    data = request.get_json()
    emp_id = data.get('id')
    
    # 查找员工
    employee = Employee.query.get(emp_id)
    if not employee:
        return jsonify({
            'code': 404,
            'message': '员工不存在'
        }), 404
    
    # 更新员工信息
    try:
        employee.name = data.get('name', employee.name)
        employee.gender = data.get('gender', employee.gender)
        employee.age = data.get('age', employee.age)
        employee.department = data.get('department', employee.department)
        employee.position = data.get('position', employee.position)
        employee.phone = data.get('phone', employee.phone)
        employee.email = data.get('email', employee.email)
        employee.hire_date = data.get('hire_date', employee.hire_date)
        
        db.session.commit()
        
        return jsonify({
            'code': 200,
            'message': '员工信息修改成功',
            'data': {
                'id': employee.id
            }
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'code': 500,
            'message': f'修改失败：{str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
