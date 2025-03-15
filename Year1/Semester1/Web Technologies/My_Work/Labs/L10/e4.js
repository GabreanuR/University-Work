window.onload = function(){
    let input = document.getElementById("cuvant");
    let select = document.getElementById("limba");
    let form = document.getElementById("form");
    let div = document.getElementById("rezultat");
    form.onsubmit = function(event){
        event.preventDefault();
        let cuvant = input.value;
        let limba = select.value;
        let url = "http://localhost:8000/dictionar.json";
        fetch(url).then(function(response){
            if(response.status == 200){
                return response.json();
            }
            else{
                throw newError("Statusul este: " + response.status);
            }
        }).then(function(date){
            let traducere;
            for(let d of date){
                if(cuvant == d.cuvant){
                    traducere = d[limba];
                }
            }
            div.innerHTML = traducere?traducere:"Nu exista";
        });
    }
}