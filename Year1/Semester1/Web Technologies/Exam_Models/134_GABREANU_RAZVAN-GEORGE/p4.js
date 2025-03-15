window.onload = function(){

    let submit = document.getElementById("buton");
    submit.innerHTML = "submit";
    submit.style.width = "100px";
    submit.style.height = "50px";
    submit.onclick = function(){
        let input = document.getElementById("text");
        if (input.innerHTML == input.innerHTML.toUpperCase()){
            console.log("da");
            let url = "http://localhost:8000/nume.json";
    
            fetch(url).then(function(response){
            if(response.status == 200){
                return response.json();
            }
            else{
                throw new Error("statusul: " + response.status);
            }
            }).then(function(){
        
            }).catch(function(err){
                console.log("A aparut o eroare: " + err.message);
            })
        }
        else{
            console.log("nu");
        }
        
    }
}