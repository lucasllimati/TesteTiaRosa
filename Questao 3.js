// Questão 03: Vezes que uma letra aparece na frase

function vezesLetraAparece(frase, letra) {

  // Variavel que conta o número de vezes que a letra aparece na frase
  var resultado = 0;

  // Ele percorre toda a frase e verificar quantas vezes uma determinada letra aparece.
  for (var indiceLetra = 0; indiceLetra < frase.length; indiceLetra++) {
    if (frase[indiceLetra] === letra) {
      resultado++; // Somamos 1 ao contador.
    }
  }

  // Frase: The Lord of The Rings
  // Letra: o
    // A letra 'o' aparece duas vezes na frase (primeira na palavra 'Lord' e depois 'of')

  // Resultado: 2

  return resultado;
}