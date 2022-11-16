package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

import com.example.portafoliogabriel.DAO.Contacto;
import com.example.portafoliogabriel.DAO.DAOContacto;

public class AgregarContactosActivity extends AppCompatActivity {

    private EditText etNombre, etNumero;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_agregar_contactos);

        etNombre = findViewById(R.id.coEtNombre);
        etNumero = findViewById(R.id.coEtNumero);
    }

    public void agregarContacto(View view) {
        String nombre = etNombre.getText().toString();
        String numero = etNumero.getText().toString();

        if (nombre.equals("") || numero.equals("")) {
            return;
        }

        Contacto contacto = new Contacto(nombre, numero);
        DAOContacto dao = new DAOContacto();
        dao.InsertarContacto(contacto);

        etNombre.setText("");
        etNumero.setText("");
    }
}