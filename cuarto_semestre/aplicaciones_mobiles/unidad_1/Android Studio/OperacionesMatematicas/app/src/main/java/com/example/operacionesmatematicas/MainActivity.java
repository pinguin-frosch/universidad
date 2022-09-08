package com.example.operacionesmatematicas;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    // Declarar los elementos para que sean globales dentro de la clase
    EditText num1, num2;
    TextView res;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Obtener cada uno de los elementos
        num1 = findViewById(R.id.etn_num1);
        num2 = findViewById(R.id.etn_num2);
        res = findViewById(R.id.tv_res);
    }

    public void sumar(View view) {
        // Obtener el texto de los inputs
        String num1text = num1.getText().toString();
        String num2text = num2.getText().toString();

        // Si alguno está vació no haremos nada
        if (num1text.equals("") || num2text.equals("")) {
            return;
        }

        // Realizar la suma
        int numero1 = Integer.parseInt(num1text);
        int numero2 = Integer.parseInt(num2text);
        int suma = numero1 + numero2;

        // Actualizar el resultado con la suma
        res.setText(String.valueOf(suma));
        res.setText(String.format("%d + %d = %d", numero1, numero2, suma));
    }
}