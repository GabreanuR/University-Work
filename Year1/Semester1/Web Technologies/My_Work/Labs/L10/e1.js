window.onload = function(){
    let input = document.getElementById("mesaj");
    let buton = document.getElementById("salveaza");
    let paragraf = document.querySelector(".afiseaza");
    let sterge = document.getElementById("sterge");
    buton.onclick = function(){
        let mesajInput = input.value;
        localStorage.setItem("mesaj", mesajInput);
        alert("Mesajul a fost salvat");
        paragraf.innerHTML = mesajInput;
    }
    let mesajSalvat = localStorage.getItem("mesaj");
        if(mesajSalvat){
            paragraf.innerHTML = mesajSalvat;
        }
    sterge.onclick = function(){
        localStorage.removeItem("mesaj");
        paragraf.innerHTML = "Niciun mesaj salvat";
    }
}