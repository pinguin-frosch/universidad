const main = () => {
  const mes = prompt('Ingrese un mes: ')
  const dia = parseInt(prompt('Ingrese un día: '))
  console.log(`Signo zodiacal: ${signo_zodiacal(mes, dia)}`)
}

const signo_zodiacal = (mes, dia) => {
  switch (mes) {
    case "1":
      if (dia_valido(mes, dia)) {
        if (dia >= 21) {
          return 'Acuario'
        } else {
          return 'Capricornio'
        }
      }
      return 'Día no válido'
    case "2":
      if (dia_valido(mes, dia)) {
        if (dia >= 21) {
          return 'Piscis'
        } else {
          return 'Acuario'
        }
      }
      return 'Día no válido'
    case "3":
      if (dia_valido(mes, dia)) {
        if (dia >= 21) {
          return 'Aries'
        } else {
          return 'Piscis'
        }
      }
      return 'Día no válido'
    case "4":
      if (dia_valido(mes, dia)) {
        if (dia >= 21) {
          return 'Tauro'
        } else {
          return 'Aries'
        }
      }
      return 'Día no válido'
    case "5":
      if (dia_valido(mes, dia)) {
        if (dia >= 21) {
          return 'Gémisis'
        } else {
          return 'Tauro'
        }
      }
      return 'Día no válido'
    case "6":
      if (dia_valido(mes, dia)) {
        if (dia >= 21) {
          return 'Cáncer'
        } else {
          return 'Gémisis'
        }
      }
      return 'Día no válido'
    case "7":
      if (dia_valido(mes, dia)) {
        if (dia >= 21) {
          return 'Leo'
        } else {
          return 'Cáncer'
        }
      }
      return 'Día no válido'
    case "8":
      if (dia_valido(mes, dia)) {
        if (dia >= 21) {
          return 'Virgo'
        } else {
          return 'Leo'
        }
      }
      return 'Día no válido'
    case "9":
      if (dia_valido(mes, dia)) {
        if (dia >= 21) {
          return 'Libra'
        } else {
          return 'Virgo'
        }
      }
      return 'Día no válido'
    case "10":
      if (dia_valido(mes, dia)) {
        if (dia >= 21) {
          return 'Escorpio'
        } else {
          return 'Libra'
        }
      }
      return 'Día no válido'
    case "11":
      if (dia_valido(mes, dia)) {
        if (dia >= 21) {
          return 'Sagitario'
        } else {
          return 'Escorpio'
        }
      }
      return 'Día no válido'
    case "12":
      if (dia_valido(mes, dia)) {
        if (dia >= 21) {
          return 'Capricornio'
        } else {
          return 'Sagitario'
        }
      }
      return 'Día no válido'
    default:
      return 'Mes no válido'
  }
}

const dia_valido = (mes, dia) => {
  const fechas = {
    "1": 31, "2": 28, "3": 31, "4": 30,
    "5": 31, "6": 30, "7": 31, "8": 31,
    "9": 30, "10": 31, "11": 30, "12": 31
  }
  return dia >= 1 && dia <= fechas[mes]
}

main()