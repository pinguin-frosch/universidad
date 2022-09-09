package com.example.operacionesmatematicas;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    // Declarar los elementos para que sean globales dentro de la clase
    private EditText num1, num2;
    private TextView res;
    private RadioButton sumar, restar, multiplicar, dividir;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Obtener cada uno de los elementos
        num1 = findViewById(R.id.etn_num1);
        num2 = findViewById(R.id.etn_num2);
        res = findViewById(R.id.tv_res);
        sumar = findViewById(R.id.rb_sumar);
        restar = findViewById(R.id.rb_restar);
        dividir = findViewById(R.id.rb_dividir);
        multiplicar = findViewById(R.id.rb_multiplicar);
    }

    public void operar(View view) {
        // Obtener el texto de los inputs
        String num1text = num1.getText().toString();
        String num2text = num2.getText().toString();

        int numero1 = Integer.parseInt(num1text);
        int numero2 = Integer.parseInt(num2text);

        int resultado;

        if (sumar.isChecked()) {
            // Sumar
            resultado = numero1 + numero2;
        } else if (restar.isChecked()) {
            // Restar
            resultado = numero1 - numero2;
        } else if (multiplicar.isChecked()) {
            // Multiplicar
            resultado = numero1 * numero2;
        } else if (dividir.isChecked()) {
            // Dividir
            resultado = numero1 / numero2;
        } else {
            resultado = 0;
        }

        // Actualizar el resultado con la suma
        res.setText(String.valueOf(resultado));
    }
}