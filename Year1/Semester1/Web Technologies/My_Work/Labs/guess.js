window.onload = guess;
function guess(){
    let mesaj = document.querySelector(".message");
    let nume = prompt("Numele jucatorului: ")
    mesaj.innerHTML +=` ${nume}`;
    let nrSecret = Math.floor(Math.random()*20)+1;
    console.log(nrSecret);
    let input = document.getElementById('guess');
    let buton = document.getElementById('check');
    let s = 20;
    let i = 0;
    buton.onclick = verifica;
    function verifica(){
        i++;
        if(i < 20){
            if(nrSecret == parseInt(input.value)){
                document.body.style.backgroundColor = "red";
                mesaj.innerHTML =  `Ai castigat jocul!`;
                document.querySelector(".number").innerHTML = nrSecret;
                buton.disabled = true;

                let p = document.createElement("p");
                p.innerHTML = `Jucatorul ${nume} a castigat jocul cu scorul ${s}`;
                document.getElementById('jucatori').appendChild(p);
            }
            else{
                s--;
                if(nrSecret < parseInt(input.value)){
                    mesaj.innerHTML = `Numarul e prea mare!`;
                }
                else{
                    mesaj.innerHTML = `Numarul e prea mic!`;
                }
            }
            document.querySelector(".score").innerHTML = s;
            document.querySelector(".hightscore").innerHTML = i;
        }
        else{
            mesaj.innerHTML = `Ai pierdut jocul!`;
            buton.disabled = true;
        }
    }
}
