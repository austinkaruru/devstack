const nav1 = document.getElementById("nav1");
const nav2 = document.getElementById("nav2");
const nav3 = document.getElementById("nav3");

nav2.style.display = "none";
nav3.style.display = "none";

nav1.addEventListener("click", function(){
    if (nav2.style.display === "none"){
        nav2.style.display = "block";
        nav3.style.display = "none";
    } else {
        nav2.style.display = "none";    
    }
});