window.onload = function(){
    let inputNume = document.getElementById("nume");
    let inputEmail = document.getElementById("email");
    let inputVarsta = document.getElementById("varsta");
    let buton = document.getElementById("salveaza");
    let div = document.getElementById("informatii");
    buton.onclick = function(){
        let ob = {
            nume: inputNume.value,
            email: inputEmail.value,
            varsta: inputVarsta.value
        };
        localStorage.setItem("date",JSON.stringify(ob));
        div.innerHTML = `<p>${ob.nume}, ${ob.email}, ${ob.varsta}`;
    }
    if(localStorage.getItem("date")){
        let ob = JSON.parse(localStorage.getItem("date"));
        div.innerHTML = `<p>${ob.nume}, ${ob.email}, ${ob.varsta}`;
    }
}