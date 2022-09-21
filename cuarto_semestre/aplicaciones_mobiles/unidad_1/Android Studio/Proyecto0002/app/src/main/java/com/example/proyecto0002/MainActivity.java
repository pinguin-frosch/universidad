package com.example.proyecto0002;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    // Declarar las variables
    private EditText numero1, numero2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Obtener los elementos
        numero1 = findViewById(R.id.et_numero1);
        numero2 = findViewById(R.id.et_numero2);
    }

    public void sumar(View view) {
        // Obtener el texto de cada elemento
        String num1text = numero1.getText().toString();
        String num2text = numero2.getText().toString();

        // No seguir si no hay texto
        if (num1text.equals("") || num2text.equals("")) {
            return;
        }

        // Pasar a número cada texto
        int num1 = Integer.parseInt(num1text);
        int num2 = Integer.parseInt(num2text);

        // Calcular el resultado
        int resultado = num1 + num2;

        // Crear un bundle y guardar el resultado como string
        Bundle extras = new Bundle();
        extras.putString("res", String.valueOf(resultado));

        // Crear un intent, pasarle el bundle y iniciarlo
        Intent i = new Intent(this, Resultado.class);
        i.putExtras(extras);
        startActivity(i);
    }
}