// Crie duas variáveis (nome e idade). Exiba a frase: "Meu nome é [nome] e tenho [idade] anos." no console.

// let myName = "Pedro";
// let myAge = 19;
// console.log(`My name is ${myName} and i have ${myAge} years old.`);

// ----------------------------------------------------------------------------------------------

// Crie duas variáveis numéricas (valor1 e valor2) e exiba soma, subtração, multiplicação e divisão.

// let valueOne = 10
// let valueTwo = 5


// console.log(`The sum of ${valueOne} and ${valueTwo} is:`, valueOne + valueTwo);
// console.log(`The substraction of ${valueOne} and ${valueTwo} is:`, valueOne - valueTwo);
// console.log(`The multiplication of ${valueOne} and ${valueTwo} is:`, valueOne * valueTwo);
// console.log(`The division of ${valueOne} and ${valueTwo} is:`, valueOne / valueTwo);

// ----------------------------------------------------------------------------------------------

// Crie variáveis para representar uma tarefa (título, descrição e status booleano). Mostre essas informações no console.

// let taskTitle = "Learning JS.";
// let descTask = "Learn the basics of JS.";
// let taskCompleted = true;
// console.log(`Tarefa: ${taskTitle}
// Descrição: ${descTask}
// Concluída: ${taskCompleted}`);
        
// ----------------------------------------------------------------------------------------------

// Copie o trecho abaixo e observe o resultado no console. Por que o resultado é "105" ao invés de 15?
// Explique a razão no comentário do próprio código. Em seguida, modifique-o para realizar a soma corretamente.

// let numero1 = 10;
// let numero2 = "5";
// console.log(numero1 + Number(numero2)); // 15

// RESPOSTA: está sendo concatenado porque o numero2(5) é uma str e não um number(int)

// ----------------------------------------------------------------------------------------------

// Crie uma variável versaoApp (número) e exiba a mensagem: "Bem-vindo ao aplicativo [nome] versão [versaoApp]" usando template strings.

// let appName = "TaskMaster";
// let appVersion = 1.0;
// let welcomeMessage = `Welcome to the app ${appName} version: ${appVersion}!`;

// console.log(welcomeMessage);
// alert(welcomeMessage); // adicionei isso apenas para testes e melhor aprendizado

// ----------------------------------------------------------------------------------------------

// Peça ao usuário dois valores (pode usar prompt() ou atribuições diretas) e compare usando ==, === e >. Mostre no console o resultado de cada comparação.

// let a = Number(prompt("Enter the value of A: "));  
// let b = prompt("Enter the value of B: ");  
// let c = Number(prompt("Enter the value of C: "));  

// console.log("Results: ")
// console.log("A == B:", a == b);   // true se os valores forem iguais
// console.log("A === B:", a === b); // false (comparação de número (a) com string (b))
// console.log("A === C:", a === c); // false (comparação de número (a) com string (b))
// console.log("A > B:", a > b);     // false se forem iguais ou conforme os valores

//  ----------------------------------------------------------------------------------------------

// Crie uma variável prioridade (valor inicial 3) e use operadores de incremento e atribuição para aumentar até 5. Exiba no console cada passo.

// let priority = 3;
// console.log("Prioridade inicial:", priority);

// priority++; // soma 1 (3 + 1)
// console.log("Before 1° increment:", priority);

// priority++; // soma 1 (4 + 1)
// console.log("Before 2° increment:", priority);

// if(priority > 5) { //garante q nao vai passar de 5, porque se for maior que 5, volta a ser 5
//   priority = 5;
// }
// console.log("Máx value 5:", priority);
        