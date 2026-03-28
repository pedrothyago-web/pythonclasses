// JS – Controle de Fluxo: Resumo de Estudo

// 1. OPERADORES — Comparação e Lógica

// Operador        O que faz                      Exemplo
// ===             Igual (valor + tipo)           5 === "5" → false
// !==             Diferente (valor + tipo)       5 !== "5" → true
// &&              AND — ambos verdadeiros        idade >= 18 && temCarteira
// ||              OR — um verdadeiro basta       x < 0 || x > 100
// !               NOT — inverte                  !temCarteira

// ⚠️ Sempre use (===) em vez de (==)— evita bugs de tipo.


// 2. CONDICIONAIS

// js if / else if / else
if (prioridade === 1) {
  // baixa
} else if (prioridade === 2) {
  // média
} else {
  // alta ou desconhecida
}

// switch — ideal pra múltiplos casos fixos
switch (diaSemana) {
  case 0: console.log("Domingo"); break;
  case 1: console.log("Segunda"); break;
  default: console.log("Outro dia");
}


// Regra prática: use if/else pra lógica variada, switch quando comparar uma variável contra vários valores fixos.


// 1. IF / ELSE — A lógica por trás
// O if avalia uma expressão e verifica se é truthy ou falsy — não necessariamente true ou false.

// Valores falsy em JS (tudo isso falha num if):
false, 0, "", null, undefined, NaN

// Valores truthy (tudo isso passa num if):
true, 1, "texto", [], {},


// js Exemplo prático — isso funciona!


// let nome = "João";
// if (nome) {
//   console.log("Nome existe"); // ✅ truthy
// }

// let carrinho = [];
// if (carrinho) {
//   console.log("Carrinho existe"); // ✅ array vazio ainda é truthy!
// }

// ⚠️ Armadilha clássica: [] e {} são truthy, mesmo vazios.


// 2. IF / ELSE — Estrutura completa

// let nota = 72;

// if (nota >= 90) {
//   console.log("A");
// } else if (nota >= 80) {
//   console.log("B");
// } else if (nota >= 70) {
//   console.log("C");
// } else if (nota >= 60) {
//   console.log("D");
// } else {
//   console.log("Reprovado");
// }

// O que o JS faz internamente:

// Testa a primeira condição
// Se falsa → vai pra próxima
// Na primeira verdadeira → executa e para (ignora o resto)
// Se nenhuma → cai no else


// 3. OPERADOR TERNÁRIO — if/else em 1 linha
// Sintaxe: condição ? valorSeTrue : valorSeFalse


// js  if/else tradicional
// let acesso;
// if (idade >= 18) {
//   acesso = "Permitido";
// } else {
//   acesso = "Negado";
// }

// Mesmo código com ternário
// let acesso = idade >= 18 ? "Permitido" : "Negado";

// Uso direto no console
console.log(saldo > 0 ? "Positivo" : "Negativo");

// Usa pra atribuições simples. Se a lógica for complexa, fica ilegível — prefira if/else.


// 4. SWITCH — Como realmente funciona


let plano = "premium";

switch (plano) {
  case "free":
    console.log("1GB de storage");
    break;
  case "basic":
    console.log("10GB de storage");
    break;
  case "premium":
    console.log("100GB de storage");
    break;
  default:
    console.log("Plano inválido");
}


// O que acontece SEM o break — Fall-through


let dia = 1;

switch (dia) {
  case 1:
    console.log("Segunda");   // executa
  case 2:
    console.log("Terça");     // também executa! ⚠️
  case 3:
    console.log("Quarta");    // também executa! ⚠️
    break;
}


// O JS continua executando os próximos cases até achar um break. Isso é um bug na maioria dos casos — mas pode ser intencional:


// js Fall-through INTENCIONAL — agrupar casos
switch (dia) {
  case 6:
  case 0:
    console.log("Final de semana"); // executa pra dia 6 ou 0
    break;
  default:
    console.log("Dia útil");
}

// 5. NULLISH COALESCING ?? e OPTIONAL CHAINING ?.
// Dois operadores modernos que substituem muito if/else:


// js  ?? — usa o valor da direita SE o da esquerda for null/undefined
let desconto = null;
let descontoFinal = desconto ?? 0;  // → 0

// Diferença do ||
let quantidade = 0;
console.log(quantidade || 10);   // → 10  ⚠️ (0 é falsy)
console.log(quantidade ?? 10);   // → 0   ✅ (0 não é null/undefined)

// ?. — acessa propriedade sem quebrar se o objeto for null
let usuario = null;
console.log(usuario?.nome1);        // → undefined (não dá erro)
console.log(usuario.nome1);         // → ❌ TypeError!



// 6. QUANDO USAR CADA UM
// Situação                                          Use
//  1–2 condições simples                            if/else
// Atribuir valor com condição simples               Ternário ? :
// Comparar 1 variável contra vários valores         switch
// Valor padrão pra null/undefined                   ??
// Acessar objeto que pode ser null                  ?.




// 7. LOOPS
//Loop                                      Quando usar
// for                                      Você sabe quantas vezes vai repetir
// while                                    Repete enquanto condição for true
// do/while                                 Executa pelo menos 1x, depois verifica
// for...of                                 Percorre valores de array
// for...in                                 Percorre chaves de objeto




// js  for clássico
for (let i = 0; i < 5; i++)

// for...of — arrays
for (let fruta of frutas) { console.log(fruta); }

// for...in — objetos
for (let chave in pessoa) { console.log(chave, pessoa[chave]); }

// 8. CONTROLE DENTRO DO LOOP

// break  //  sai do loop imediatamente
// continue  // pula pro próximo ciclo

// Precisa decidir?
  // ├── Poucos casos → if/else
  // └── Muitos casos fixos → switch

// Precisa repetir?
  // ├── Sabe quantas vezes → for
  // ├── Depende de condição → while
  // ├── Garante 1 execução → do/while
  // ├── Iterar array → for...of
  // └── Iterar objeto → for...in