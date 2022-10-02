package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;

public class OperacionesConRadio extends AppCompatActivity {

    RadioButton radioButtonSumar, radioButtonRestar, radioButtonMultiplicar, radioButtonDividir;
    EditText editTextNumero1, editTextNumero2;
    TextView textViewResultado;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_operaciones_con_radio);

        radioButtonSumar = findViewById(R.id.ocrRadioButtonSumar);
        radioButtonRestar = findViewById(R.id.ocrRadioButtonRestar);
        radioButtonMultiplicar = findViewById(R.id.ocrRadioButtonMultiplicar);
        radioButtonDividir = findViewById(R.id.ocrRadioButtonDividir);
        editTextNumero1 = findViewById(R.id.ocrEditTextNumero1);
        editTextNumero2 = findViewById(R.id.ocrEditTextNumero2);
        textViewResultado = findViewById(R.id.ocrTextViewResultado);
    }

    public void operar(View view) {
        String stringNumero1 = editTextNumero1.getText().toString();
        String stringNumero2 = editTextNumero2.getText().toString();

        if (stringNumero1.equals("") || stringNumero2.equals("")) {
            return;
        }

        float floatNumero1 = Float.parseFloat(stringNumero1);
        float floatNumero2 = Float.parseFloat(stringNumero2);
        float floatResultado;

        if (radioButtonSumar.isChecked()) {
            floatResultado = floatNumero1 + floatNumero2;
        } else if (radioButtonRestar.isChecked()) {
            floatResultado = floatNumero1 - floatNumero2;
        } else if (radioButtonMultiplicar.isChecked()) {
            floatResultado = floatNumero1 * floatNumero2;
        } else {
            floatResultado = floatNumero1 / floatNumero2;
        }

        textViewResultado.setText(String.valueOf(floatResultado));
    }
}