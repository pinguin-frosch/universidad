// Import the functions you need from the SDKs you need
import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.8.4/firebase-app.js'
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
import { getDatabase, ref, set } from 'https://www.gstatic.com/firebasejs/9.8.4/firebase-database.js'

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: 'AIzaSyBWvB9LR97aLNaVZ_qiH7TnZnshUhN3RcE',
  authDomain: 'empleadosgb-f1d6e.firebaseapp.com',
  projectId: 'empleadosgb-f1d6e',
  storageBucket: 'empleadosgb-f1d6e.appspot.com',
  messagingSenderId: '1091063224428',
  appId: '1:1091063224428:web:473be1c604c500d9a6e049'
}

// Initialize Firebase
const app = initializeApp(firebaseConfig)

// Initialize Realtime Database and get a reference to the service
const database = getDatabase(app)

const agregar_empleado = () => {
  let rut_empleado = document.getElementById('rut').value
  let nombre = document.getElementById('nombre').value
  let email = document.getElementById('email').value
  let telefono = document.getElementById('telefono').value
  let foto = document.getElementById('foto').value
  // set(ref(database, `empleados/${rut_empleado}`), {
  //   nombre: nombre,
  //   email: email,
  //   telefono: telefono,
  //   url_foto: foto
  // })
}

const button = document.getElementById('agregarEmp')
button.addEventListener('click', agregar_empleado)

