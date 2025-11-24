// 检查登录状态
window.addEventListener('DOMContentLoaded', function() {
    const username = localStorage.getItem('username');
    const student_id = localStorage.getItem('student_id');
    
    if (!username) {
        // 未登录，跳转到登录页
        alert('请先登录');
        window.location.href = 'login.html';
        return;
    }
    
    // 检查是否为root用户
    if (parseInt(student_id) !== 1) {
        alert('权限不足，只有root用户（学号为1）才能添加员工信息');
        window.location.href = 'index.html';
        return;
    }
    
    // 显示用户名
    document.getElementById('username').textContent = username;
});

// 表单提交处理
document.getElementById('addEmployeeForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = '';
    messageDiv.className = 'message';
    
    // 获取表单数据
    const formData = {
        student_id: parseInt(localStorage.getItem('student_id')),
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
        // 发送添加请求
        const response = await fetch('http://127.0.0.1:8000/employee/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        const result = await response.json();
        
        if (result.code === 200) {
            // 添加成功
            messageDiv.textContent = result.message;
            messageDiv.className = 'message success';
            // 重置表单
            document.getElementById('addEmployeeForm').reset();
            // 3秒后跳转到员工列表
            setTimeout(() => {
                window.location.href = 'list.html';
            }, 2000);
        } else {
            // 添加失败
            messageDiv.textContent = result.message;
            messageDiv.className = 'message error';
        }
    } catch (error) {
        messageDiv.textContent = '网络错误，请检查服务器是否启动';
        messageDiv.className = 'message error';
        console.error('添加员工错误:', error);
    }
});
