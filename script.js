document.addEventListener("DOMContentLoaded", function () {

    const registerSection = document.getElementById("registerSection");
    const loginSection = document.getElementById("loginSection");
    const bookingSection = document.getElementById("bookingSection");

    const registerBtn = document.getElementById("registerBtn");
    const loginBtn = document.getElementById("loginBtn");

    const goLogin = document.getElementById("goLogin");

    const registerMessage = document.getElementById("registerMessage");
    const loginMessage = document.getElementById("loginMessage");

    const bookingForm = document.getElementById("bookingForm");
    const bookingMessage = document.getElementById("bookingMessage");


    // Switch to login
    goLogin.addEventListener("click", function(){
        registerSection.style.display = "none";
        loginSection.style.display = "block";
    });


    // REGISTER
    registerBtn.addEventListener("click", function(){

        const name = document.getElementById("regName").value;
        const email = document.getElementById("regEmail").value;
        const password = document.getElementById("regPassword").value;

        if(!name || !email || !password){
            registerMessage.innerText = "Fill all fields";
            registerMessage.style.color = "red";
            return;
        }

        const user = { name, email, password };
        localStorage.setItem("user", JSON.stringify(user));

        registerMessage.innerText = "Account Created Successfully!";
        registerMessage.style.color = "lightgreen";

        setTimeout(() => {
            registerSection.style.display = "none";
            loginSection.style.display = "block";
                                                                                     
