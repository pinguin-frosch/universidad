package com.example.firebasegabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import com.example.firebasegabriel.dao.Contacto;
import com.example.firebasegabriel.dao.DaoContacto;

public class DetallesContactoActivity extends AppCompatActivity {

    private TextView tvNombre, tvNumero;
    private Contacto contacto;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detalles_contacto);

        tvNombre = findViewById(R.id.deTvNombre);
        tvNumero = findViewById(R.id.deTvNumero);

        Bundle extras = getIntent().getExtras();
        contacto = (Contacto) extras.get("contacto");

        tvNombre.setText(contacto.getNombre());
        tvNumero.setText(contacto.getNumero());
    }

    public void eliminarContacto(View view) {
        DaoContacto dao = new DaoContacto();
        dao.eliminarContacto(contacto);
        finish();
    }
}