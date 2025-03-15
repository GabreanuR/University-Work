window.onload = function(){
    let N = Math.floor(Math.random() * 6) + 5;
    for(let i = 0 ; i < N; i++){
        let array = [];
        let div = document.createElement("div");
        document.body.appendChild(div);
        div.className = "patrat";
        div.innerHTML="Div"+(i+1);
        div.style.position="relative";
        div.style.marginBottom="3px";
        div.style.left="0px";
        array.push(parseInt(div.innerHTML));
        div.onclick = function(event){
            div.style.left= parseInt(div.style.left) + 10 + "px";
            event.stopPropagation();
        }
        document.body.onclick = function(event){
            let j = Math.floor(Math.random() * N);
            let divuri = document.getElementsByClassName("patrat");
            divuri[j].style.position = "absolute";
            divuri[j].style.left = event.clientX + "px";
            divuri[j].style.top = event.clientY + "px";
        }
    }
}