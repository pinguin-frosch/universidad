package com.example.firebasegabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

import com.example.firebasegabriel.dao.Contacto;
import com.example.firebasegabriel.dao.DaoContacto;

public class AgregarContactoActivity extends AppCompatActivity {

    private EditText etNombre, etNumero;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_agregar_contacto);

        etNombre = findViewById(R.id.agEtNombre);
        etNumero = findViewById(R.id.agEtNumero);
    }

    public void agregarContacto(View view) {
        String nombre = etNombre.getText().toString();
        String numero = etNumero.getText().toString();

       if (nombre.equals("")) {
            return;
        }

        Contacto contacto = new Contacto(nombre, numero);
        DaoContacto dao = new DaoContacto();
        dao.insertarContacto(contacto);

        etNombre.setText("");
        etNumero.setText("");
    }

}