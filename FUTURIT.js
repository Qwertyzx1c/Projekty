const oblicz = document.querySelector("button")

function funkcja_obliczeniowa(event){
    event.preventDefault()
    
    const checkboxy = document.querySelectorAll("input[type='checkbox']:checked")
    const miasto = document.querySelector("#miasta").value
    
    const raty = document.querySelector("#ratatuj").value

    const tabela = document.querySelector("table")
    
    tabela.innerHTML = `<tr>
        <td>Kurs</td>
        <td>Kwota</td>
    </tr`
    for(let kurs of checkboxy){
        tabela.innerHTML += `<tr>
            <td>${kurs.name}</td>
            <td>${kurs.value}</td>
        </tr>`
    }
}
oblicz.addEventListener("click", funkcja_obliczeniowa)
