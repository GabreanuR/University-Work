window.onload = function(){
    let info = document.getElementById("info");
    let intervalId;
    let nr = 0;
    function randomFontSize() {
        let fontSize = Math.floor(Math.random() * 21) + 10;
        info.style.fontSize = `${fontSize}px`;
    }

    document.addEventListener("keypress", (event) => {
        if (event.key === "a" && nr == 0) {
            
            if (!intervalId) {
                info.textContent += ` ${new Date().toLocaleString()}`;
                intervalId = setInterval(randomFontSize, 3000);
            } else {
                nr = 1
                clearInterval(intervalId);
                intervalId = null;
                const finalFontSize = info.style.fontSize;
                localStorage.setItem("fontSize", finalFontSize);
            }
        }
    });

    const savedFontSize = localStorage.getItem("fontSize");
    if (savedFontSize) {
        info.style.fontSize = savedFontSize;
    }
};