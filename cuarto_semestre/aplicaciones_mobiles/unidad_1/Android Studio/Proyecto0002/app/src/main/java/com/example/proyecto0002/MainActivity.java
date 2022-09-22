package com.example.proyecto0002;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
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

    @SuppressLint("DefaultLocale") public static String processNumber(double number) {
        if (Math.ceil(number) != Math.floor(number)) {
            // Mostrar decimales con 4 digitos
            return String.format("%.4f", number);
        } else {
            // Para los enteros no usar decimales
            return String.format("%.0f", number);
        }
    }

    @SuppressLint("DefaultLocale")
    public void sumar(View view) {
        // Obtener el texto de cada elemento
        String num1text = numero1.getText().toString();
        String num2text = numero2.getText().toString();

        // No seguir si no hay texto
        if (num1text.equals("") || num2text.equals("")) {
            return;
        }

        // Pasar a número cada texto
        double num1 = Double.parseDouble(num1text);
        double num2 = Double.parseDouble(num2text);

        // Crear un bundle para guardar los resultados
        Bundle extras = new Bundle();

        // Suma
        double res_suma = num1 + num2;
        extras.putString("res_suma", processNumber(res_suma));

        // Resta
        double res_resta = num1 - num2;
        extras.putString("res_resta", processNumber(res_resta));

        // Multiplicación
        double res_multiplicacion = num1 * num2;
        extras.putString("res_multiplicacion", processNumber(res_multiplicacion));

        // División
        if (num2 == 0) {
            // No se puede dividir por 0
            extras.putString("res_division", "Error");
        } else {
            double res_division = num1 / num2;
            extras.putString("res_division", processNumber(res_division));
        }

        // Crear un intent, pasarle el bundle y iniciarlo
        Intent i = new Intent(this, Resultado.class);
        i.putExtras(extras);
        startActivity(i);
    }
}