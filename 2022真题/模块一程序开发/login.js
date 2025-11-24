// 登录表单提交处理
document.getElementById('loginForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMsg = document.getElementById('errorMsg');
    
    // 清空错误信息
    errorMsg.textContent = '';
    
    try {
        // 发送登录请求
        const response = await fetch('http://127.0.0.1:8000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });
        
        const result = await response.json();
        
        if (result.code === 200) {
            // 登录成功，保存用户信息
            localStorage.setItem('username', result.data.username);
            localStorage.setItem('student_id', result.data.student_id);
            // 跳转到首页
            window.location.href = 'index.html';
        } else {
            // 登录失败，显示错误信息
            errorMsg.textContent = result.message || '登录失败，请重试';
        }
    } catch (error) {
        errorMsg.textContent = '网络错误，请检查服务器是否启动';
        console.error('登录错误:', error);
    }
});
