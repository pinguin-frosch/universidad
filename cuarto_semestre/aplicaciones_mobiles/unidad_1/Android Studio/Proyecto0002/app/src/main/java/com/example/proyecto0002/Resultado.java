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
        TextView tv_suma = findViewById(R.id.tv_suma);
        TextView tv_resta = findViewById(R.id.tv_resta);
        TextView tv_multiplicacion = findViewById(R.id.tv_multiplicacion);
        TextView tv_division = findViewById(R.id.tv_division);

        // Cargar el bundle y obtener el resultado de la otra actividad
        Bundle extras = this.getIntent().getExtras();
        String res_suma = extras.getString("res_suma");
        String res_resta = extras.getString("res_resta");
        String res_multiplicacion = extras.getString("res_multiplicacion");
        String res_division = extras.getString("res_division");

        // Colocar el resultado en el elemento de texto
        tv_suma.setText(res_suma);
        tv_resta.setText(res_resta);
        tv_multiplicacion.setText(res_multiplicacion);
        tv_division.setText(res_division);
    }
}