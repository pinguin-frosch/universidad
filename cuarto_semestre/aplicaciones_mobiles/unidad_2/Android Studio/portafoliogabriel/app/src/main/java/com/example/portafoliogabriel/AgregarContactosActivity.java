package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

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
        FirebaseDatabase baseDeDatos = FirebaseDatabase.getInstance();
        DatabaseReference referencia = baseDeDatos.getReference("contactos");

        Contacto contacto = new Contacto(nombre, numero);
        referencia.push().setValue(contacto);
    }
}