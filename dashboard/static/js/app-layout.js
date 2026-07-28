/* dashboard/static/js/app-layout.js */
document.addEventListener("DOMContentLoaded", function () {
    const htmlEl = document.documentElement;
    const themeBtn = document.getElementById("themeToggle");
    const sidebar = document.querySelector(".sidebar-container");
    const sidebarToggle = document.getElementById("sidebarToggle");

    // 1. Dark Mode Engine
    const savedTheme = localStorage.getItem("saas-theme") || "light";
    htmlEl.setAttribute("data-bs-theme", savedTheme);
    
    if (themeBtn) {
        themeBtn.addEventListener("click", () => {
            const newTheme = htmlEl.getAttribute("data-bs-theme") === "light" ? "dark" : "light";
            htmlEl.setAttribute("data-bs-theme", newTheme);
            localStorage.setItem("saas-theme", newTheme);
            triggerToast("Mode Tampilan Berhasil Diperbarui", "success");
        });
    }

    // 2. Collapsible Sidebar Engine
    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener("click", () => {
            sidebar.classList.toggle("collapsed");
            localStorage.setItem("sidebar-state", sidebar.classList.contains("collapsed") ? "closed" : "open");
        });
    }

    // 3. Lightweight Global Toast Notification Generator
    window.triggerToast = function(message, type = "success") {
        const toastContainer = document.getElementById("saasToastContainer") || createToastContainer();
        const toast = document.createElement("div");
        toast.className = `toast-saas show animate__animated animate__fadeInUp bg-${type}`;
        toast.innerHTML = `<i class="bi bi-info-circle-fill"></i> <span>${message}</span>`;
        toastContainer.appendChild(toast);
        
        setTimeout(() => {
            toast.classList.replace("animate__fadeInUp", "animate__fadeOutDown");
            setTimeout(() => toast.remove(), 400);
        }, 3000);
    };

    function createToastContainer() {
        const container = document.createElement("div");
        container.id = "saasToastContainer";
        container.style.position = "fixed";
        container.style.bottom = "24px";
        container.style.right = "24px";
        container.style.zIndex = "9999";
        container.style.display = "flex";
        container.style.flexDirection = "column";
        container.style.gap = "8px";
        document.body.appendChild(container);
        return container;
    }
});