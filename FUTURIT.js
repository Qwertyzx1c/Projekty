const oblicz = document.querySelector("button")
const kursy = document.querySelectorAll("input[type='checkbox']")

function funkcja_obliczeniowa(event){
    event.preventDefault()
    
    const tabela = document.querySelector("table")
    const ilosc_rat = document.querySelector("#raty").value
    let suma = 0
    
    tabela.innerHTML = `<tr>
        <td>Kurs:</td>
        <td>Kwota:</td>
    </tr>`

    for(let kurs of kursy){
        if(kurs.checked){
            tabela.innerHTML += `<tr>
            <td>${kurs.name}</td>
            <td>${kurs.value}</td>
            </tr>`

            suma += Number(kurs.value)
        }
    }

    const raty_span = document.querySelector('#raty_span')
    const suma_span = document.querySelector('#suma_span')

    raty_span.textContent = ilosc_rat
    suma_span.textContent = Number(suma / ilosc_rat).toFixed(2)
}
oblicz.addEventListener("click", funkcja_obliczeniowa)
