window.addEventListener("load",function(){
    document.body.addEventListener("click",function(event){
        let notificare = document.createElement("div");
        notificare.innerHTML = `<p>Aceasta este o notificare!</p>`;
        notificare.classList.add("popup");
        document.body.appendChild(notificare);
        //console.log(event.clientX + " " + event.clientY);

        notificare.style.position = "absolute";
        notificare.style.left = event.clientX + "px";
        notificare.style.top = event.clientY + "px"; 
        //console.log(getComputedStyle(notificare).width);
        //console.log(getComputedStyle(notificare).border);

        let buton = document.createElement("button");
        buton.innerHTML = `Sterge`;
        buton.classList.add("buton");
        notificare.appendChild(buton);

        buton.addEventListener("click",function(event){
            event.stopPropagation();
            notificare.remove();
        });

        setTimeout(function(){
            notificare.style.animation = "disparitie 3s";
            setTimeout(function(){
                notificare.remove();
            },3000);
        },5000);
    });
});