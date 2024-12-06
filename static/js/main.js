// 工具函数
function formatDate(dateStr) {
    return new Date(dateStr).toLocaleString('zh-CN', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

function handleError(error) {
    console.error('Error:', error);
    const errorMessage = error.response?.data?.error || '请求失败，请重试';
    showNotification('错误', errorMessage, 'error');
}

// 通知函数
function showNotification(title, message, type = 'info') {
    // 创建通知元素
    const notification = document.createElement('div');
    notification.className = `alert alert-${type === 'error' ? 'danger' : 'info'} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 20px; right: 20px; z-index: 1050; max-width: 300px;';
    
    notification.innerHTML = `
        <strong>${title}</strong>
        <p class="mb-0">${message}</p>
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // 添加到页面
    document.body.appendChild(notification);
    
    // 3秒后自动消失
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => notification.remove(), 150);
    }, 3000);
}

// 加载动画
function showLoading() {
    const loadingModal = new bootstrap.Modal(document.getElementById('loadingModal'));
    loadingModal.show();
    return loadingModal;
}

function hideLoading(modal) {
    if (modal) {
        modal.hide();
    }
}

// 复制到剪贴板
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showNotification('成功', '已复制到剪贴板');
    }).catch(err => {
        console.error('复制失败:', err);
        showNotification('错误', '复制失败，请手动复制', 'error');
    });
}

// 导出 PDF
function exportToPDF() {
    window.print();
}

// 初始化工具提示
document.addEventListener('DOMContentLoaded', function() {
    // 初始化所有的工具提示
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});