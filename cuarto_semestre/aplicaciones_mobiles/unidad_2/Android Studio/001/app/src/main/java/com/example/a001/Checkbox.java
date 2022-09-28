package com.example.a001;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.TextView;

public class Checkbox extends AppCompatActivity {

    // Declarar las variables a usar
    EditText numero1, numero2;
    CheckBox sumar, restar;
    TextView resultado;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_checkbox);

        // Vincular las variables con los controles
        numero1 = findViewById(R.id.et_numero1);
        numero2 = findViewById(R.id.et_numero2);
        sumar = findViewById(R.id.cb_sumar);
        restar = findViewById(R.id.cb_restar);
        resultado = findViewById(R.id.tv_resultado);
    }

    public void operar(View view) {
        // Obtener el texto de cada número
        String num1text = numero1.getText().toString();
        String num2text = numero2.getText().toString();

        // Cerrar si ambos números están vacíos
        if (num1text.equals("") || num2text.equals("")) {
            return;
        }

        // Si no hay ningún elemento marcado salir
        if (!sumar.isChecked() && !restar.isChecked()) {
            return;
        }

        // Pasar los números a int
        int num1int = Integer.parseInt(num1text);
        int num2int = Integer.parseInt(num2text);

        // Declarar variables para las operaciones
        int resultado_suma;
        int resultado_resta;
        String resultadoString;

        if (sumar.isChecked() && restar.isChecked()) {
            // Suma y resta
            resultado_suma = num1int + num2int;
            resultado_resta = num1int - num2int;
            resultadoString = String.format("%d + %d = %d, %d - %d = %d", num1int, num2int, resultado_suma, num1int, num2int, resultado_resta);

        } else if (sumar.isChecked()) {
            // Solo suma
            resultado_suma = num1int + num2int;
            resultadoString = String.format("%d + %d = %d", num1int, num2int, resultado_suma);

        } else {
            // Solo resta
            resultado_resta = num1int - num2int;
            resultadoString = String.format("%d - %d = %d", num1int, num2int, resultado_resta);
        }

        // Colocar el resultado en el TextView
        resultado.setText(resultadoString);
    }
}