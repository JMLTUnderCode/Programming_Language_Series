/*
    Universidad Simon Bolivar
    Departamento de Computación y Tecnología de la Información
    CI3641 – Lenguajes de Programación 1
    Trimestre: Septiembre - Diciembre 2023
    Profesor: Ricardo Monascal
    Estudiante: Junior Miguel Lara Torres
    Carnet: 17-10303

    Parcial 1 - Pregunta 1, Parte B, seccion 1.

    "Dada una cadena de caracteres w y un entero no-negativo
    k, calcular la rotacion de k posicion de la cadena w."

    PD: Todo archivo .js puede ser cargado en un navegador
    y interpretarse directamente, sin embargo particularmente este
    archivo fue creado y ejecutado en una terminal de 
    Debian 11(WSL) con Node.js.
*/ 
process.stdout.write('Determinar k rotaciones de un string w.\n');

// Inicializacion de preguntas y arreglo de datos de entrada.
let questions = ['Ingrese cadena w: ', 'Ingrese entero k >= 0: '];
let inputs = [];

// Funcion que permite escribir por pantalla strings permitiendo
// interactuar con el usuario.
function writeConsole(index){
    process.stdout.write(questions[index]);
}

// Proceso de JS para leer por consola datos, mediante un
// condicional de si el arreglo de respuestas a menor al de
// preguntas seguiremos preguntando hasta obtener una cantidad
// igualada de respuestas - preguntas.
process.stdin.on('data', function(data){
    inputs.push(data.toString().trim());

    if(inputs.length < questions.length){
        writeConsole(inputs.length);
    } else {
        // Ejecutamos procedimiento para rotar string.
        // Inicializando con el string dado mediante el uso de las
        // funciones substring y charAt, una que permite extraer el
        // resto del string a partir de un indice dado y el otro 
        // permitiendo extrar un caracter dado el indice de su posicion.
        let w = inputs[0];
        for(let i = 0; i < inputs[1]; i++){
            w = w.substring(1) + w.charAt(0);
        }
        console.log("Rotacion:\n" + w);
        process.exit();
    }
});

writeConsole(0);