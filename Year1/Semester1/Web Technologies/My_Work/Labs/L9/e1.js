window.onload = function(){
    let select = document.getElementById("numar");
    let finalizeaza = document.getElementById("finalizeaza");
    let input = document.getElementById("rezervari");
    let span = document.getElementById("count");
    let container = document.querySelector(".container");
    finalizeaza.disabled = true;

    select.onchange=function(){
        let n = parseInt(select.value);
        let array = [];
        for(let i = 0;i < n;i++){
            let b = document.createElement("button");
            b.innerHTML = `${i+1}`;
            container.appendChild(b);
            b.style.backgroundColor = 'green';
            b.onclick = function(){
                if(b.style.backgroundColor == 'green'){
                    span.innerHTML = parseInt(span.innerHTML) + 1;
                    b.style.backgroundColor = 'red';
                    array.push(parseInt(b.innerHTML));
                    input.value = array.sort(function(a,b){
                        return a-b;
                    }).join(",");
                }
                else{
                    span.innerHTML = parseInt(span.innerHTML) - 1;
                    b.style.backgroundColor = 'green';
                    array = [];
                    let butoane = document.querySelectorAll(".container button");
                    for(let b of butoane){
                        if(b.style.backgroundColor == 'red'){
                            array.push(parseInt(b.innerHTML));
                        }
                    }
                    input.value = array.join(",");
                }
                if(input.value){
                    finalizeaza.disabled = false;
                }
                else{
                    finalizeaza.disabled = true;
                }
            }
        }
        finalizeaza.onclick = function(){
            alert("Butoanele rezervate: " + input.value);
            container.style.display = "none";
        }
    }
}