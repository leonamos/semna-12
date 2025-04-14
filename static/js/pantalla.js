function agregar(valor) {
    const pantalla = document.querySelector("input[name='pantalla']");
    pantalla.value += valor;
}

function limpiar(valor) {
    const pantalla = document.querySelector("input[name='pantalla']");
    if (valor == 'c' || valor == 'C') { 
        pantalla.value = '0';
    }
}

function retroceder(valor) {
if( valor == "D") {
    const pantalla = document.querySelector("input[name='pantalla']");
    pantalla.value = pantalla.value.slice(0, -1)
}

}