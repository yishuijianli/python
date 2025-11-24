// 检查登录状态
window.addEventListener('DOMContentLoaded', function() {
    const username = localStorage.getItem('username');
    
    if (!username) {
        // 未登录，跳转到登录页
        window.location.href = 'login.html';
        return;
    }
});
