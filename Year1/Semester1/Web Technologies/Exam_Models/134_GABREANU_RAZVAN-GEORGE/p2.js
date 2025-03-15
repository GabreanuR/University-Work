window.onload = function(){
    let array = ["color1","color2","color3","color4","color5"];
    window.onkeydown = function (event) {
        if(event.key == "s"){
            let j = Math.floor(Math.random() * 5);
            let buton = document.createElement("button");
            buton.className = array[j];
            buton.style.height = "50px";
            buton.style.width = "100px";
            document.body.appendChild(buton);
            let color = getComputedStyle(buton, null);
            let color2 = color.getPropertyValue("background-color");
            buton.innerHTML = color2;
            buton.onclick = function(event){
                event.stopPropagation();
                let butoaneClasa = buton.className;
                console.log(butoaneClasa);
                let butoane = document.getElementsByClassName(butoaneClasa);
                for(let i = 0; i < butoane.length; i++){
                    butoane[i].disabled = true;
                }
            }
        }
        if(event.key == "Backspace"){
            var butoaneDis = document.getElementsByTagName("button");
            for(let i = 0; i < butoaneDis.length; i++){
                if(butoaneDis[i].disabled == true){
                    butoaneDis[i].remove();
                }
            } 
        }
    };
    document.body.onclick = function(event){
        event.stopPropagation();
        let butoane = document.getElementsByTagName("button");
        alert("Sunt " + butoane.length + " butoane");
    }
    
}