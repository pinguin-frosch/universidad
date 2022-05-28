const main = () => {
  let notas = []

  let cantidad = parseInt(prompt('Ingrese la cantidad de notas: '))
  if (verificar_valor(cantidad)) {
    alert('No es una cantidad válida')
    return
  }

  for (let i = 0; i < cantidad; i++) {
    let nota = parseFloat(prompt('Ingrese una nota: '))
    if (verificar_valor(nota)) {
      alert('No es una nota válida')
      return
    }
    notas.push(nota)
  }

  alert(`Promedio: ${promedio(notas)}`)
}

const verificar_valor = (valor) => {
  return isNaN(valor)
}

const promedio = (notas) => {
  const total = notas.reduce((total, valor) => total + valor, 0)
  return total / notas.length
}

main()