window.onload = function(){
    let p = document.getElementById("info");
    let nr = 0;
    let font;
    let c;
    let f = localStorage.getItem("font",font);
    if(f){
        p.style.border = f + "px solid red";
    }
    window.onkeydown = function (event) {
        if(event.key == "a"){
            if(nr == 0){
                nr++
                let data = new Date();
                p.innerHTML += ` Data: ${data.getDate()}/ ora:${data.getHours()}`;
                c = setInterval(function(){
                    font = Math.floor(Math.random()*21) + 10;
                    console.log(font);
                    p.style.border = font + "px solid red";
                },3000);
            }
            else{
                clearInterval(c);
                localStorage.setItem("font",font);
            }
        }
    };
}