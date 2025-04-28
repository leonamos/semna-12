function agregar(valor) {
    const pantalla = document.getElementById('pantalla');
    pantalla.value += valor;
}

function limpiar() {
    const pantalla = document.getElementById('pantalla');
    pantalla.value = '';
}

function calcular() {
    const pantalla = document.getElementById('pantalla');
    try {
        const resultado = eval(pantalla.value);
        pantalla.value = resultado;
    } catch (error) {
        pantalla.value = 'Error';
    }
}
