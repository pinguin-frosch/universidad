const operacion = () => {
  let num_1 = prompt('Ingresa un número: ')
  num_1 = parseFloat(num_1)
  if (isNaN(num_1)) {
    alert('No es un número')
    return
  }

  let num_2 = prompt('Ingresa otro número: ')
  num_2 = parseFloat(num_2)
  if (isNaN(num_2)) {
    alert('No es un número')
    return
  }

  alert(`${num_1} + ${num_2} = ${num_1 + num_2}`)
  alert(`${num_1} - ${num_2} = ${num_1 - num_2}`)
  alert(`${num_1} * ${num_2} = ${num_1 * num_2}`)
  if (num_2 !== 0) {
    alert(`${num_1} / ${num_2} = ${num_1 / num_2}`)
  } else {
    alert('No se puede dividir por 0')
  }
}

operacion()