window.addEventListener("load",function(){
    let i = 0;
    let t = setInterval(function(){
        let x = Math.floor(Math.random()*window.innerWidth - 50);
        let y = Math.floor(Math.random()*window.innerHeight - 50);
        let b = document.createElement("button");
        b.style.width = "50px";
        b.style.height = "50px";
        b.style.borderRadius = "10px";
        b.style.backgroundColor = `rgb(${Math.floor(Math.random()*256)},${Math.floor(Math.random()*256)},${Math.floor(Math.random()*256)})`;
        document.body.appendChild(b);

        b.indice = i;

        b.style.position = "absolute";
        b.style.left = x + "px";
        b.style.top = y + "px";

        i++;
        if(i == 4){
            clearInterval(t);
        }

        document.body.addEventListener("keydown", function(event){
            let butoane = document.getElementsByTagName("button");
            if((butoane.length == 4) && (event.key == 's')){
                let nr = 0;
                for(let b of butoane){
                    b.addEventListener("click",function(){
                        if (b.indice == nr){
                            b.style.backgroundColor = "red";
                            b.innerHTML = b.indice;
                            if(nr == 3){
                                alert("Ai cartigat!");
                            }
                        }
                        else{
                            alert("Ai pierdut jocul!");
                            for(let b of butoane){
                                b.remove();
                            }
                        }
                        nr++;
                    });
                }
            }
        });
    },2000);
});