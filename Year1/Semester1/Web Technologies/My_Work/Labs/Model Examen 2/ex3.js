window.onload = function(){
    let input = document.getElementById("numar");
    let paragrafe = document.getElementsByTagName("p");
    let nr = paragrafe.length;
    if(localStorage.getItem("nr")){
        input.value = localStorage.getItem("nr");
    }
    console.log(input.value);
    window.onkeydown = function (event) {
        if(event.key == "s"){
            window.onkeydown = null;
            let numar = input.value;
            console.log(numar);
            var c = setInterval(function(){
                var x;
                for(let p of paragrafe){
                  if (p.innerHTML.split(" ").length > parseInt(input.value)){
                    x=p;
                    break;
                  }
                }
                if(x){
                  document.body.removeChild(x);   //parinte.removeChild(copil)
                }
                else {
                  clearInterval(c);
                  localStorage.setItem("nr",nr-paragrafe.length);
                }
            },2000);
        }
    };
}