package com.example.firebasegabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import com.example.firebasegabriel.dao.Contacto;
import com.example.firebasegabriel.dao.DaoContacto;

public class DetallesContactoActivity extends AppCompatActivity {

    private EditText etNombre, etNumero;
    private Contacto contacto;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detalles_contacto);

        etNombre = findViewById(R.id.deEtNombre);
        etNumero = findViewById(R.id.deEtNumero);

        Bundle extras = getIntent().getExtras();
        contacto = (Contacto) extras.get("contacto");

        etNombre.setText(contacto.getNombre());
        etNumero.setText(contacto.getNumero());
    }

    public void eliminarContacto(View view) {
        DaoContacto dao = new DaoContacto();
        dao.eliminarContacto(contacto);
        finish();
    }

    public void actualizarContacto(View view) {
        DaoContacto dao = new DaoContacto();

        String nombre = etNombre.getText().toString();
        String numero = etNumero.getText().toString();

        if (nombre.equals("")) {
            return;
        }

        contacto.setNombre(nombre);
        contacto.setNumero(numero);

        dao.actualizarContacto(contacto);

        finish();
    }
}