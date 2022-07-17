// Import the functions you need from the SDKs you need
import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.8.4/firebase-app.js'
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
import { getDatabase, ref, set, get, child, remove } from 'https://www.gstatic.com/firebasejs/9.8.4/firebase-database.js'

// Your web app's Firebase configuration
const firebaseConfig = {
  databaseURL: "https://empleadosgb-f1d6e-default-rtdb.firebaseio.com",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig)

// Initialize Realtime Database and get a reference to the service
const database = getDatabase(app)

const boton_agregar = document.getElementById('agregar_empleado')
boton_agregar.addEventListener('click', () => {
  let rut = document.getElementById('rut')
  let nombre = document.getElementById('nombre')
  let email = document.getElementById('email')
  let telefono = document.getElementById('telefono')
  let foto = document.getElementById('foto')
  let id = rut.value.replace(/\./g, '')
  set(ref(database, `empleados/${id}`), {
    rut: rut.value,
    nombre: nombre.value,
    email: email.value,
    telefono: telefono.value,
    foto: foto
  })
})

const boton_buscar = document.getElementById('buscar_empleado')
boton_buscar.addEventListener('click', async () => {
  let rut = document.getElementById('rut')
  let nombre = document.getElementById('nombre')
  let email = document.getElementById('email')
  let telefono = document.getElementById('telefono')
  let id = rut.value.replace(/\./g, '')

  const snapshot = await get(child(ref(getDatabase()), `empleados/${id}`))
  if (snapshot.exists()) {
    const values = snapshot.val()
    nombre.value = values.nombre
    email.value = values.email
    telefono.value = values.telefono
  } else {
    console.error('No existe ese empleado')
  }
})

const boton_eliminar = document.getElementById('eliminar_empleado')
boton_eliminar.addEventListener('click', async () => {
  let rut = document.getElementById('rut')
  let id = rut.value.replace(/\./g, '')
  remove(ref(getDatabase()), `empleados/${id}`)
})
