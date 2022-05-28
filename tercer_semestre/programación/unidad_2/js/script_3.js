const formato = (numero) => {
  if (numero < 10) {
    numero = `0${numero}`
  }
  return numero
}

const main = () => {
  let tiempo = parseInt(prompt('Ingrese segundos: '))
  if (isNaN(tiempo)) {
    alert('No es un número válido')
    return
  }

  // Obtener horas
  let horas = parseInt(tiempo / 3600)
  tiempo = tiempo - 3600 * horas

  // Obtener minutos
  let minutos = parseInt(tiempo / 60)
  tiempo = tiempo - 60 * minutos

  // El resto son los segundos
  let segundos = tiempo

  // Corregir el formato
  horas = formato(horas)
  minutos = formato(minutos)
  segundos = formato(segundos)

  alert(`${horas}:${minutos}:${segundos}`)
}

main()