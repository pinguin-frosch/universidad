package com.example.proyecto0002;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class Resultado extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_resultado);

        // Obtener el elemento para ingresar el resultado
        TextView resultado_texto = findViewById(R.id.tv_resultado);

        // Cargar el bundle y obtener el resultado de la otra actividad
        Bundle extras = this.getIntent().getExtras();
        String resultado = extras.getString("res");

        // Colocar el resultado en el elemento de texto
        resultado_texto.setText(resultado);
    }
}