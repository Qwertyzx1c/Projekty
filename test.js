const przycisk = document.querySelector('button')

przycisk.addEventListener('click', () => {
    const tresc = prompt('Wprowadź nową treść artykułu')
    let paragraf = document.querySelector('#xd')
    let drugi_paragraf = document.querySelector('#dx')
    if(tresc.length > 255){
    drugi_paragraf.textContent = 'Długość paragrafu powyżej jest za długa, maksymalna ilość osiągnięta!'
    }else{
    paragraf.textContent = tresc
    }
   paragraf.textContent = tresc
} )
