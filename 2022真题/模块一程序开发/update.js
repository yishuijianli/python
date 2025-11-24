// 检查登录状态
window.addEventListener('DOMContentLoaded', function() {
    const username = localStorage.getItem('username');
    
    if (!username) {
        // 未登录，跳转到登录页
        alert('请先登录');
        window.location.href = 'login.html';
        return;
    }
    
    // 显示用户名
    document.getElementById('username').textContent = username;
    
    // 加载员工列表到下拉框
    loadEmployeeList();
});

// 加载员工列表
async function loadEmployeeList() {
    const selectElement = document.getElementById('employeeSelect');
    
    try {
        const response = await fetch('http://127.0.0.1:8000/employees');
        const result = await response.json();
        
        if (result.code === 200 && result.data.length > 0) {
            result.data.forEach(emp => {
                const option = document.createElement('option');
                option.value = emp.id;
                option.textContent = `${emp.name} - ${emp.department} - ${emp.position}`;
                selectElement.appendChild(option);
            });
        } else {
            selectElement.innerHTML = '<option value="">暂无员工数据</option>';
        }
    } catch (error) {
        console.error('加载员工列表错误:', error);
        alert('加载员工列表失败，请检查服务器是否启动');
    }
}

// 员工选择变化事件
document.getElementById('employeeSelect').addEventListener('change', async function() {
    const empId = this.value;
    const form = document.getElementById('updateEmployeeForm');
    
    if (!empId) {
        form.style.display = 'none';
        return;
    }
    
    // 加载员工详细信息
    try {
        const response = await fetch(`http://127.0.0.1:8000/employee/${empId}`);
        const result = await response.json();
        
        if (result.code === 200) {
            const emp = result.data;
            
            // 填充表单
            document.getElementById('employeeId').value = emp.id;
            document.getElementById('name').value = emp.name;
            document.getElementById('gender').value = emp.gender;
            document.getElementById('age').value = emp.age;
            document.getElementById('department').value = emp.department;
            document.getElementById('position').value = emp.position;
            document.getElementById('phone').value = emp.phone;
            document.getElementById('email').value = emp.email || '';
            document.getElementById('hire_date').value = emp.hire_date;
            
            // 显示表单
            form.style.display = 'block';
            
            // 清空消息
            document.getElementById('message').textContent = '';
            document.getElementById('message').className = 'message';
        } else {
            alert('获取员工信息失败');
        }
    } catch (error) {
        console.error('获取员工信息错误:', error);
        alert('获取员工信息失败，请检查服务器是否启动');
    }
});

// 表单提交处理
document.getElementById('updateEmployeeForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = '';
    messageDiv.className = 'message';
    
    // 获取表单数据
    const formData = {
        id: parseInt(document.getElementById('employeeId').value),
        name: document.getElementById('name').value,
        gender: document.getElementById('gender').value,
        age: parseInt(document.getElementById('age').value),
        department: document.getElementById('department').value,
        position: document.getElementById('position').value,
        phone: document.getElementById('phone').value,
        email: document.getElementById('email').value,
        hire_date: document.getElementById('hire_date').value
    };
    
    try {
        // 发送修改请求
        const response = await fetch('http://127.0.0.1:8000/update', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        const result = await response.json();
        
        if (result.code === 200) {
            // 修改成功
            messageDiv.textContent = result.message;
            messageDiv.className = 'message success';
            
            // 重新加载员工列表
            document.getElementById('employeeSelect').innerHTML = '<option value="">请选择员工</option>';
            loadEmployeeList();
            
            // 3秒后跳转到员工列表
            setTimeout(() => {
                window.location.href = 'list.html';
            }, 2000);
        } else {
            // 修改失败
            messageDiv.textContent = result.message;
            messageDiv.className = 'message error';
        }
    } catch (error) {
        messageDiv.textContent = '网络错误，请检查服务器是否启动';
        messageDiv.className = 'message error';
        console.error('修改员工错误:', error);
    }
});
