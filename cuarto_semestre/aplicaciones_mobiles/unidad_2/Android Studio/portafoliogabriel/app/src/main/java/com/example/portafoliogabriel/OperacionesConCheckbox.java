package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.Toast;

public class OperacionesConCheckbox extends AppCompatActivity {

    EditText editTextNumero1, editTextNumero2;
    CheckBox checkBoxSumar, checkBoxRestar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_operaciones_con_checkbox);

        editTextNumero1 = findViewById(R.id.ochEditTextNumero1);
        editTextNumero2 = findViewById(R.id.ochEditTextNumero2);
        checkBoxSumar = findViewById(R.id.ochCheckBoxSumar);
        checkBoxRestar = findViewById(R.id.ochCheckBoxRestar);
    }

    @SuppressLint("DefaultLocale")
    public void operar(View view) {
        String stringNumero1 = editTextNumero1.getText().toString();
        String stringNumero2 = editTextNumero2.getText().toString();

        if (stringNumero1.equals("") || stringNumero2.equals("")) {
            return;
        }

        int intNumero1 = Integer.parseInt(stringNumero1);
        int intNumero2 = Integer.parseInt(stringNumero2);
        String stringResultado;

        if (checkBoxSumar.isChecked() && checkBoxRestar.isChecked()) {
            int suma = intNumero1 + intNumero2;
            int resta = intNumero1 - intNumero2;
            stringResultado = String.format("%d + %d = %d, %d - %d = %d", intNumero1, intNumero2, suma, intNumero1, intNumero2, resta);
        } else if (checkBoxSumar.isChecked()) {
            int suma = intNumero1 + intNumero2;
            stringResultado = String.format("%d + %d = %d", intNumero1, intNumero2, suma);
        } else if (checkBoxRestar.isChecked()) {
            int resta = intNumero1 - intNumero2;
            stringResultado = String.format("%d - %d = %d", intNumero1, intNumero2, resta);
        } else {
            return;
        }

        Toast.makeText(this, stringResultado, Toast.LENGTH_LONG).show();
    }
}