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
    
    // 加载员工列表
    loadEmployees();
});

// 加载员工列表
async function loadEmployees() {
    const tableBody = document.getElementById('employeeTableBody');
    
    try {
        const response = await fetch('http://127.0.0.1:8000/employees');
        const result = await response.json();
        
        if (result.code === 200 && result.data.length > 0) {
            tableBody.innerHTML = '';
            result.data.forEach(emp => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${emp.id}</td>
                    <td>${emp.name}</td>
                    <td>${emp.gender}</td>
                    <td>${emp.age}</td>
                    <td>${emp.department}</td>
                    <td>${emp.position}</td>
                    <td>${emp.phone}</td>
                    <td>${emp.email || '-'}</td>
                    <td>${emp.hire_date}</td>
                `;
                tableBody.appendChild(row);
            });
        } else {
            tableBody.innerHTML = '<tr><td colspan="9" style="text-align: center;">暂无员工数据</td></tr>';
        }
    } catch (error) {
        tableBody.innerHTML = '<tr><td colspan="9" style="text-align: center; color: red;">加载失败，请检查服务器是否启动</td></tr>';
        console.error('加载员工列表错误:', error);
    }
}
