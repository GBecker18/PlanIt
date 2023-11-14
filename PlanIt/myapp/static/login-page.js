const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "user" && password === "pass") {
        //alert("You have successfully logged in.");
	location.open(window.location.href = (window.location.href).replace("login-page.html", "homePageEmployee.html")); //redirects to employee version of home page
        location.reload();
    } else if (username === "admin" && password === "pass") {
        //alert("You have successfully logged in.");
	location.open(window.location.href = (window.location.href).replace("login-page.html", "homePageManager.html")); //redirects to manager version of home page
        location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})