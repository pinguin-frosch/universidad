package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.Toast;

public class CheckboxActivity extends AppCompatActivity {

    EditText etNumero1, etNumero2;
    CheckBox cbSumar, cbRestar, cbMultiplicar, cbDividir;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_checkbox);

        etNumero1 = findViewById(R.id.chEtNumero1);
        etNumero2 = findViewById(R.id.chEtNumero2);
        cbSumar = findViewById(R.id.chCbSumar);
        cbRestar = findViewById(R.id.chCbRestar);
        cbMultiplicar = findViewById(R.id.chCbMultiplicar);
        cbDividir = findViewById(R.id.chCbDividir);
    }

    public void operar(View view) {
        String sNumero1 = etNumero1.getText().toString();
        String sNumero2 = etNumero2.getText().toString();

        if (sNumero1.equals("") || sNumero2.equals("")) {
            return;
        }

        double numero1 = Double.parseDouble(sNumero1);
        double numero2 = Double.parseDouble(sNumero2);

        if (cbSumar.isChecked()) {
            String resultadoSuma = Double.toString(numero1 + numero2);
            Toast.makeText(this, String.format("Suma: %s", resultadoSuma), Toast.LENGTH_SHORT).show();
        }

        if (cbRestar.isChecked()) {
            String resultadoResta = Double.toString(numero1 - numero2);
            Toast.makeText(this, String.format("Resta: %s", resultadoResta), Toast.LENGTH_SHORT).show();
        }

        if (cbMultiplicar.isChecked()) {
            String resultadoMultiplicacion = Double.toString(numero1 * numero2);
            Toast.makeText(this, String.format("Multiplicación: %s", resultadoMultiplicacion), Toast.LENGTH_SHORT).show();
        }

        if (cbDividir.isChecked()) {
            if (numero2 == 0) return;
            String resultadoDivision = Double.toString(numero1 / numero2);
            Toast.makeText(this, String.format("División: %s", resultadoDivision), Toast.LENGTH_SHORT).show();
        }

    }
}