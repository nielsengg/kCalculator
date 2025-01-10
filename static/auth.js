function checkAuth() {
    const userName = localStorage.getItem('userName');
    if (!userName) {
        window.location.href = "/intro";
    } else {
        window.location.href = "/home";
    }
}

checkAuth();