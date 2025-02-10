/*
    Universidad Simon Bolivar
    Departamento de Computación y Tecnología de la Información
    CI3641 – Lenguajes de Programación 1
    Trimestre: Septiembre - Diciembre 2023
    Profesor: Ricardo Monascal
    Estudiante: Junior Miguel Lara Torres
    Carnet: 17-10303

    Parcial 1 - Pregunta 1, Parte B, seccion 2.

    "Dada una matriz cuadrada A(cuya dimension es NxN)m calcular
    el producto A x A^t (Donde A^t es la transpuesta de A)."

    IMPORTANTE: Caracteristica del input, se pide primeramente el
    valor N, que simula la dimension de la matriz, luego se pide
    al usuario que ingrese fila por fila donde cada valor de la fila
    debe estar separado por espacio, Ej.
    N      -> 3
    Fila 0 -> 1 2 3
    Fila 1 -> 4 5 6
    Fila 2 -> 7 8 9

    PD: Todo archivo .js puede ser cargado en un navegador
    y interpretarse directamente, sin embargo particularmente este
    archivo fue creado y ejecutado en una terminal de 
    Debian 11(WSL) con Node.js.
*/

process.stdout.write('Multiplicacion de matrices.\n');

// Inicializacion de preguntas y arreglo de datos de entrada.
// Como tambien variables generales para el programa.
let questions = [
    'Ingrese dimension N >= 0: ', 
    'indique elementos de la fila '
];
let inputs = [];
let rows = [];
let k = 0;
let N;

// Funcion que permite escribir por pantalla strings permitiendo
// interactuar con el usuario.
function writeConsole(index){
    if(index == 0){
        process.stdout.write(questions[index]);
    } else {
        process.stdout.write(questions[1] + (index-1) + ': ');
    }
}

// Proceso de JS que permite realizar preguntas, verificar si la
// data entrante es correcta, para luego realizar la multiplicacion
// matricial y mostrar por consola.
process.stdin.on('data', function(data){
    // Leemos por consola la data.-
    inputs.push(data.toString().trim());
    
    // Verificando que el numero de columnas sea correcto.
    // En caso contrario, mensaje de error y finalizar programar.
    if(k > 0){
        rows[k-1] = inputs[k].split(' ');
        if(rows[k-1].length != N){
            process.stdout.write(`Error: Numero de columnas distinto a ${N}.\n`);
            process.exit();
        }
    } else {
        N = Number(inputs[0]);
    }
    
    // Seguimos leyendo filas de la matriz.
    if( k < N ){
        k++; writeConsole(k);

    // Realizamso la multiplicacion por transpuesta de la misma.
    } else {
        let result = [];
        for(let r in rows){
            result[r] = [];
            for(let c in rows[r]){
                result[r][c] = 0;
                for(let z = 0; z < N; z++){
                    result[r][c] += Number(rows[r][z])*Number(rows[c][z]);
                }
            }
        }
        console.log("Resultado de A x A^t:");
        for(let i = 0; i < N; i++){
            console.log(result[i]);
        }
        process.exit();
    }
});

writeConsole(0);