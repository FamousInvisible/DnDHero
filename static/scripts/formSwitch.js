let elemsToClean = document.getElementById("cleaner").children
let radios = document.getElementsByClassName("radio")
function radio(className){
    for (let e = 0; e < elemsToClean.length; e++){
        elemsToClean[e].style.display = "none"; //чистим форму от всех полей
    }
    for (let e = 0; e < radios.length; e++){
        radios[e].style.disabled = true; //деактивируем все радиокнопки
    }

    elemsToShow = document.getElementsByClassName(className)
    for (let e = 0; e < elemsToShow.length; e++){
        elemsToShow[e].style.display = "block"; //показываем элементы которые нам нужно
    }
}
