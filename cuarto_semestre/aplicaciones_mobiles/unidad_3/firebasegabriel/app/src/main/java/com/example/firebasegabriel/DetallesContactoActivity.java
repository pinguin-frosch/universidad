package com.example.firebasegabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

import com.example.firebasegabriel.dao.Contacto;

public class DetallesContactoActivity extends AppCompatActivity {

    public TextView tvNombre, tvNumero;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detalles_contacto);

        tvNombre = findViewById(R.id.deTvNombre);
        tvNumero = findViewById(R.id.deTvNumero);

        Bundle extras = getIntent().getExtras();
        Contacto contacto = (Contacto) extras.get("contacto");

        tvNombre.setText(contacto.getNombre());
        tvNumero.setText(contacto.getNumero());
    }
}