window.onload = function(){
    if(JSON.parse(localStorage.getItem("date")) != 0){
        let lista = JSON.parse(localStorage.getItem("date"));
        let cont = document.getElementsByTagName("ul");
        
    }
    let zile = document.getElementsByTagName("li");
    let array = []
    for(let i = 0; i < zile.length; i++){
            array.push(zile[i].innerHTML)
                
        }
    console.log(array);
        var c = setInterval(function(){
            let input = document.getElementsByTagName("input");
            let aux = array.pop();
            array.unshift(aux);  
            if(input[0].checked == true){
                clearInterval(c);
                localStorage.setItem("date",JSON.stringify(array));
            }
            else{
                
            }  
        },3000);
    
}

