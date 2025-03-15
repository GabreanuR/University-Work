window.onload = function(){
    let par = document.getElementById("raspuns");
    let select = document.getElementById("animal");
    let input = document.getElementById("varsta");
    form.onsubmit = function(event){
        event.preventDefault();
        let animal = select.value;
        let varstainit = input.value;
        let url = "http://localhost:8000/animale.json";
        fetch(url).then(function(response){
            if(response.status == 200){
                return response.json();
            }
            else{
                throw newError("Statusul este: " + response.status);
            }
        }).then(function(date){
            for(let d of date){
                let nume = d.nume;
                let tip = d.tip;
                let varsta = d.varsta;
                if (tip == animal && varstainit <= varsta){
                    par.innerHTML += nume;
                    par.innerHTML += " ";
                }
            }
            if (par.innerHTML == ""){
                par.innerHTML = "Nu exista animale";
            }
        });
    };
}