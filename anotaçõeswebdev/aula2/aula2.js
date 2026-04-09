let a = 5, b = "5";

console.log(a == b);   // true (igualdade)
console.log(a === b);  // false (igualdade estrita)
console.log(a != b);   // false (diferente)
console.log(a !== b);  // true (diferente estrito)
console.log(a < b);    // false (menor que)
console.log(a > b);    // false (maior que)
console.log(a <= b);   // true (menor ou igual)
console.log(a >= b);   // true (maior ou igual)


let idade = 25;
let temCarteira = true;

// AND (&&) - ambas condições devem ser verdadeiras
if (idade >= 18 && temCarteira) {
  console.log("Pode dirigir");
}

// OR (||) - pelo menos uma condição deve ser verdadeira
if (idade < 18 || !temCarteira) {  
  console.log("Não pode dirigir");
}

// NOT (!) - inverte o valor booleano
if (!temCarteira) {
  console.log("Precisa de carteira");
}


// Exemplo de if-else para prioridade de tarefas

let prioridade = 2; // 1: baixa, 2: média, 3: alta

if (prioridade === 3) { // === compara valor e tipo
  console.log("Prioridade Alta"); // se for prioridade 3, exibe "Prioridade Alta"
} else if (prioridade === 2) { 
    console.log("Prioridade Média") // se for prioridade 2, exibe "Prioridade Média"
} else if (prioridade === 1) {
    console.log("Prioridade Baixa") // se for prioridade 1, exibe "Prioridade Baixa"
} else if (prioridade === 4) {
    console.log("Prioridade Altíssima") // se for prioridade 4, exibe "Prioridade Altíssima"
} else {
  console.log("Prioridade desconhecida"); // se for qualquer outro valor, exibe "Prioridade desconhecida"
}

// Exemplo de switch para dias da semana

let diaSemana = new Date().getDay()

 switch (diaSemana) { // getDay() retorna um número de 0 a 6, onde 0 é domingo e 6 é sábado
    case 0:
      console.log("Domingo") // se for 0, exibe "Domingo"
        break;
    case 1:
      console.log("Segunda") // se for 1, exibe "Segunda"
        break;
    case 2:
      console.log("Terça") // se for 2, exibe "Terça"
        break;
    case 3:
      console.log("Quarta")// se for 3, exibe "Quarta"
        break;
    case 4:
      console.log("Quinta")// se for 4, exibe "Quinta"
        break;
    case 5:
      console.log("Sexta")// se for 5, exibe "Sexta"
        break;
    case 6:
      console.log("Sabado")// se for 6, exibe "Sábado"
        break;
    default:
         console.log("Dia desconhecido")// se for qualquer outro valor, exibe "Dia desconhecido"
        break;
 }

 // O for é ideal quando sabemos exatamente quantas vezes queremos repetir um bloco de código, como iterar sobre um array ou executar uma tarefa um número específico de vezes. Ele é compacto e fácil de ler, tornando-o uma escolha comum para loops controlados por contadores.
 
for (let i = 0; i < 5; i++) { // ++ so incrementa de 1 em 1
  console.log("Contagem:", i); 
} // muito versatil no dia a dia


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// O while é útil quando não sabemos quantas vezes o loop deve ser executado, mas queremos continuar enquanto uma condição for verdadeira. O do-while é ideal para situações onde queremos garantir que o código seja executado pelo menos uma vez, como em menus de opções ou validação de entrada do usuário.
let contador = 0;
while (contador < 5) {
  console.log("Contagem:", contador);
  contador++;
}
// no while voce é obrigado a declarar a variavel fora do while

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// O do-while é semelhante ao while, mas garante que o bloco de código seja executado pelo menos uma vez, mesmo que a condição seja falsa. Ele é útil para situações onde queremos executar um código antes de verificar a condição, como em menus de opções ou validação de entrada do usuário.
let numero = 5;
do {
  console.log("Número é:", numero);
  numero--;
} while (numero > 0);
// quando chegar no while para de ler o codigo


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//Exercício 1: Condicional de Acesso
// Crie uma variável nivelAcesso (1, 2 ou 3). Se o acesso for 3, exiba "Acesso Total"; se for 2, exiba "Acesso Parcial"; senão, exiba "Acesso Negado".

let nivelAcesso = 3
// 1 = acesso negado ; 2 = acesso parcial ; 3 = acesso total
switch (nivelAcesso) {
    case 1:
        console.log("Acesso negado")
        break;
    case 2:
        console.log("Acesso  parcial")
        break;
    case 3:
        console.log("Acesso total")
        break;
    default:
        console.log("Sem acesso")
        break;
}


//Exercício 2: Avaliação de Notas
// Crie uma variável nota. Use o switch para avaliar:

// Se 10, exiba "Nota Máxima".
// Se 8 ou 9, exiba "Muito Bom".
// Se 6 ou 7, exiba "Bom".
// Se 5, exiba "Regular".
// Caso contrário, exiba "Nota insuficiente"

// O switch é ideal para substituir múltiplos if-else quando temos várias condições baseadas em um mesmo valor, como em menus de opções ou avaliação de casos específicos. Ele torna o código mais organizado e fácil de ler, especialmente quando lidamos com muitas condições relacionadas a um único valor.
let nota = 8 
switch (nota) {
    case 5:
     console.log("Regular")
        break;
    case 6:
    case 7:
     console.log("Bom")
        break;
    case 8:
    case 9:
     console.log("Muito Bom")
        break;
    case 10:
     console.log("Nota Máxima")
        break;
    default:
        console.log("Nota Insuficiente")
        break;
}


//Exercício 3: Listando Números Pares
// Use um for para exibir apenas os números pares de 1 a 10 no console.

for(let i =1; i <= 10; 1++) {
    if (i % 2 === 0) {
        console.log("Par:", i);
    }
}

//Exercício 4: Soma com while
// Usando um while, some todos os números de 1 a 5 e exiba o resultado.
let soma = 0;
let i = 1;
while (i <= 5) {
    soma += i; // soma = soma + i
    i++;
}
console.log("Soma total:", soma);   

// Exercício 5: do/while de Contagem Regressiva
// Crie uma contagem regressiva usando do/while que inicie em 3 e vá até 1, exibindo "FIM!" ao término.
let contagem = 3;
do {
    console.log("Contagem:", contagem);
    contagem--;
} while (contagem > 0);
console.log("FIM!");

//Exercício 6: Calculadora Simples
// Peça ao usuário dois valores (prompt() ou atribuições diretas) e um operador (+, -, *, /). Use switch para realizar a operação e exibir o resultado.
let valor1 = 10;
let valor2 = 5;
let operador = "+";
let resultado;
switch (operador) { 
    case "+":
        resultado = valor1 + valor2; // se for +, realiza a soma
        break;
    case "-":
        resultado = valor1 - valor2; // se for -, realiza a subtração
        break;
    case "*":
        resultado = valor1 * valor2; // se for *, realiza a multiplicação
        break;
    case "/":
        resultado = valor1 / valor2; // se for /, realiza a divisão
        break;
    default:
        console.log("Operador inválido"); // se for qualquer outro operador, exibe "Operador inválido"
        break;
}

// Exercício 7: Sistema de Notas Escolares
// Crie um sistema que receba uma nota (0-10) e calcule a média de 3 notas. Use condicionais para determinar o conceito:

// A (9-10): Excelente
// B (7-8.9): Bom
// C (5-6.9): Regular
// D (3-4.9): Insuficiente
// F (0-2.9): Reprovado
let nota1 = 8;
let nota2 = 7;
let nota3 = 9;
let media = (nota1 + nota2 + nota3) / 3;
if (media >= 9 && media <= 10) { // se a média for entre 9 e 10, exibe "Conceito A: Excelente" (&& é o operador lógico AND, que verifica se ambas as condições são verdadeiras)
    console.log("Conceito A: Excelente");
} else if (media >= 7 && media < 9) { // se a média for entre 7 e 8.9, exibe "Conceito B: Bom" (&& é o operador lógico AND, que verifica se ambas as condições são verdadeiras)
    console.log("Conceito B: Bom");
} else if (media >= 5 && media < 7) { // se a média for entre 5 e 6.9, exibe "Conceito C: Regular" (&& é o operador lógico AND, que verifica se ambas as condições são verdadeiras)
    console.log("Conceito C: Regular");
} else if (media >= 3 && media < 5) { // se a média for entre 3 e 4.9, exibe "Conceito D: Insuficiente" (&& é o operador lógico AND, que verifica se ambas as condições são verdadeiras)
    console.log("Conceito D: Insuficiente");
} else if (media >= 0 && media < 3) { // se a média for entre 0 e 2.9, exibe "Conceito F: Reprovado" (&& é o operador lógico AND, que verifica se ambas as condições são verdadeiras)
    console.log("Conceito F: Reprovado");
} else {
    console.log("Nota inválida");
}

// Exercício 8: Tabuada Interativa
// Crie um programa que gere a tabuada de um número usando diferentes tipos de loops. Compare os resultados.
let numeroTabuada = 5;
console.log("Tabuada do", numeroTabuada, "usando for:");
for (let i = 1; i <= 10; i++) {
    console.log(numeroTabuada, "x", i, "=", numeroTabuada * i);
} // usando for para gerar a tabuada do número 5, iterando de 1 a 10 e exibindo o resultado da multiplicação

console.log("Tabuada do", numeroTabuada, "usando while:");
let x = 1;
while (x <= 10) {
    console.log(numeroTabuada, "x", x, "=", numeroTabuada * x);
    x++;
} // usando while para gerar a tabuada do número 5, iterando de 1 a 10 e exibindo o resultado da multiplicação

console.log("Tabuada do", numeroTabuada, "usando do-while:");
let y = 1;
do {
    console.log(numeroTabuada, "x", y, "=", numeroTabuada * y);
    y++;
} while (y <= 10); // usando do-while para gerar a tabuada do número 5, iterando de 1 a 10 e exibindo o resultado da multiplicação

