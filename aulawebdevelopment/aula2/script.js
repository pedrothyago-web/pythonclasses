// let a = 5, b = "5";

// console.log(a == b);   // true (igualdade)
// console.log(a === b);  // false (igualdade estrita)
// console.log(a != b);   // true (diferente)
// console.log(a !== b);  // true (diferente estrito)
// console.log(a < b);    // false (menor que)
// console.log(a > b);    // false (maior que)
// console.log(a <= b);   // true (menor ou igual)
// console.log(a >= b);   // true (maior ou igual)


// --------------------------------------------------------------------


// let idade = 25;
// let temCarteira = true;

// // AND (&&) - ambas condições devem ser verdadeiras
// if (idade >= 18 && temCarteira) {
//   console.log("Pode dirigir");
// }

// // OR (||) - pelo menos uma condição deve ser verdadeira
// if (idade < 18 || !temCarteira) {
//   console.log("Não pode dirigir");
// }

// // NOT (!) - inverte o valor booleano
// if (!temCarteira) {
//   console.log("Precisa de carteira");
// }


// --------------------------------------------------------------------


// let prioridade = 4; // 1: baixa, 2: média, 3: alta, 4: altissima

// if (prioridade === 3) {
//   console.log("Prioridade Alta");
// }
// else if (prioridade === 2) {
//     console.log("Prioridade Média")
// }
// else if (prioridade === 1) {
//   console.log("Prioridade Baixa");
// }
// else if (prioridade === 4) {
//   console.log("Prioridade Altíssima");
// }
// else {
//     console.log("Prioridade desconhecida")
// }

// --------------------------------------------------------------------


// let diaSemana = new Date().getDay(); // 0: Domingo, 1: Segunda, etc. 

// switch (diaSemana) {
//   case 0:
//     console.log("Domingo");
//     break;

//   case 1:
//     console.log("Segunda-feira");
//     break;

//   case 2:
//     console.log("Terça-feira");
//     break;

//   case 3:
//     console.log("Quarta-feira");
//     break;

//   case 4:
//     console.log("Quinta-feira");
//     break;

//   case 5:
//     console.log("Sexta-feira");
//     break;

//   case 6:
//     console.log("Sábado");
//     break;

//   default: // se nao for nenhum dos de cima, executa esse abaixo
//     console.log("Dia inválido");
//     break;
// }


// --------------------------------------------------------------------

// def variavel e define o valor inicial #1
// diz até onde vai #2
// incremento (i++ => i = i + 1) #3
// decremento (i-- => i = i - 1) #3
//       1        2         3
// for (let i = 0; i <= 5; i = i ++) {
//   console.log("Contagem:", i);
// }

// --------------------------------------------------------------------

// let i = 0;
// while (i < 5) {
//   console.log("Contagem:", i);
//   i++;
// }

// --------------------------------------------------------------------

// let numero = 0;
// do {
//   console.log("Número é:", numero);
//   numero--;
// } while (numero > 5);

// --------------------------------------------------------------------

// let pessoa = { nome: "João", idade: 30, cidade: "São Paulo" };

// for (let propriedade in pessoa) {
//   console.log(propriedade + ": " + pessoa[propriedade]);
// }
// // nome: João
// // idade: 30
// // cidade: São Paulo



// -------------------------------------------------------- exercicios da aula
// -------------------------------------------------------- exercicios da aula
// -------------------------------------------------------- exercicios da aula

// let numero = 9

// console.log("Tabuada do " + numero + "usando o for")
// for (let i = 1; i <= 10; i++) {
//   console.log(numero + " x " + i + " = " + (numero * i))
// }

// -------------------------------------------------------- exercicios da aula

// ex7: Crie um sistema que receba uma nota (0-10) e calcule a média de 3 notas. Use condicionais para determinar o conceito:
// A (9-10): Excelente
// B (7-8.9): Bom
// C (5-6.9): Regular
// D (3-4.9): Insuficiente
// F (0-2.9): Reprovado

// let nota1 = 6.3;
// let nota2 = 8.2;
// let nota3 = 7.0;

// let media = (nota1 + nota2 + nota3) /3;
// console.log("Média:", media.toFixed(1)); //.toFixed() é para virar int

// if (media >= 9) {
//     console.log("Excelente")
// }
// else if (media >= 7) {
//     console.log("Bom")
// }
// else if (media >= 5) {
//     console.log("Regular")
// }
// else if (media >= 3) {
//     console.log("Insuficiente")
// }
// else { 
//     console.log("Reprovado") // se for menor que 3, reprovado
// } 

// ------------------------------------------------------- exercicios da aula 2

// ex6:  Peça ao usuário dois valores (prompt() ou atribuições diretas) e um operador (+, -, *, /). Use switch para realizar a operação e exibir o resultado.

// let valor1 = Number(prompt("Digite um valor: "))
// let valor2 = Number(prompt("Digite outro valor: "))
// let operador = prompt("Digite um operador: (+, -, *, /)")

// switch (operador) {
//   case "+":
//         console.log(valor1 + valor2);
//     break;
//   case "-":
//         console.log(valor1 - valor2);
//     break;
//   case "/":
//         console.log(valor1 / valor2);
//     break;
//   case "*":
//         console.log(valor1 * valor2);
//     break;

//   default:
//       console.log("Isso não é um operador válido.")
//     break;
// }

// ------------------------------------------------------- exercicios da aula 3

// ex5: Crie uma contagem regressiva usando do/while que inicie em 3 e vá até 1, exibindo "FIM!" ao término.

// let i = 3;
// do {
//   console.log("Número é:", i);
//   i--;
// } while (i >= 1);

// console.log("Fim!")

// ------------------------------------------------------- exercicios da aula 4

// ex4: Usando um while, some todos os números de 1 a 5 e exiba o resultado.

// let soma = 0;
// let contador = 1;

// while (contador <= 5) {
//     soma += contador; // soma(0) + contador(1) = soma(1) e por ai vai.
//     contador++ //adiciona um no contador (porque quer varias somas, +1, +2, +3, +4, +5)
// }

// console.log("A soma total é:", soma);

// ------------------------------------------------------- exercicios da aula 5

// ex3: Use um for para exibir apenas os números pares de 1 a 10 no console.

// for (let i = 1; i <= 10; i++) {
//   if (i % 2 === 0) { // se o resto da divisao por 2 = 0 -> par
//       console.log("Par:", i);
//   }
// } 


// ------------------------------------------------------- exercicios da aula 6

// ex2: Crie uma variável nota. Use o switch para avaliar: 
// Se 10, exiba "Nota Máxima".
// Se 8 ou 9, exiba "Muito Bom".
// Se 6 ou 7, exiba "Bom".
// Se 5, exiba "Regular".
// Caso contrário, exiba "Nota insuficiente".

// let nota = 9;

// switch (nota) {
//   case 10:
//     console.log("Nota Máxima");
//     break;
//   case 9:
//   case 8:
//     console.log("Muito Bom");
//     break;
//   case 7:
//   case 6:
//     console.log("Bom");
//     break;
//   case 5:
//     console.log("Regular");
//     break;
//   default:
//     console.log("Nota insuficiente");
//     break;
// }

// ------------------------------------------------------- exercicios da aula 7

// ex1: Crie uma variável nivelAcesso (1, 2 ou 3). Se o acesso for 3, exiba "Acesso Total"; se for 2, exiba "Acesso Parcial"; senão, exiba "Acesso Negado".

// let nivelAcesso =  Number(prompt("Digite o nível de acesso (1-3): "))

// if (nivelAcesso == 3) {
//     console.log("Você tem acesso total.")
// }

// else if (nivelAcesso == 2) {
//     console.log("Você tem acesso parcial.")
// }

// else if (nivelAcesso == 1) {
//     console.log("Acesso negado.")
// }

// else {
//     console.log("O nível de acesso não existe.")
// }