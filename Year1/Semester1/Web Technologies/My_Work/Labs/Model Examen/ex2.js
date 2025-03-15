window.onload = function(){
    for (let i = 0; i < 6; i++) {
        let buton = document.createElement("button");
        buton.innerHTML = `Buton ${i+1}`;
        document.body.appendChild(buton);
        buton.className = "buton";
        buton.style.width = "100px";
        buton.style.height = "50px";
        buton.style.backgroundColor = (i%2==0)?"yellow":"green";
        buton.style.color = (i%2==0)?"black":"white";
        buton.culoareInitiala = buton.style.backgroundColor;
        buton.onclick = function(event){
            event.stopPropagation();
            if(buton.style.backgroundColor == "red"){
                buton.remove();
            }
            else{
                buton.style.backgroundColor = "red";
                setTimeout(function(){
                    buton.style.backgroundColor = buton.culoareInitiala;
                },5000);
            }
        }

    }
    document.body.onclick = function(){
        let butoane = document.getElementsByTagName("button");
        alert("Sunt " + butoane.length + " butoane");
    }
};