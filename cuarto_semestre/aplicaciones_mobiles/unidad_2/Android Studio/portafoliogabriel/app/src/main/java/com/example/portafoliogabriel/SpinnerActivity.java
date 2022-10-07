package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;

public class SpinnerActivity extends AppCompatActivity {

    private EditText editTextNumero1, editTextNumero2;
    private Spinner spinnerOpciones;
    private TextView textViewResultado;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_spinner);

        editTextNumero1 = findViewById(R.id.sEditTextNumero1);
        editTextNumero2 = findViewById(R.id.sEditTextNumero2);
        spinnerOpciones = findViewById(R.id.sSpinnerOpciones);
        textViewResultado = findViewById(R.id.sTextViewResultado);

        String[] opciones = {"Sumar", "Restar", "Multiplicar", "Dividir"};
        ArrayAdapter<String> adaptador = new ArrayAdapter<String>(this, androidx.appcompat.R.layout.support_simple_spinner_dropdown_item, opciones);
        spinnerOpciones.setAdapter(adaptador);
    }

    public void operar(View view) {
        String stringNumero1 = editTextNumero1.getText().toString();
        String stringNumero2 = editTextNumero2.getText().toString();

        if (stringNumero2.equals("") || stringNumero1.equals("")) {
            textViewResultado.setText("");
            return;
        }

        String opcion = spinnerOpciones.getSelectedItem().toString();

        int intNumero1 = Integer.parseInt(stringNumero1);
        int intNumero2 = Integer.parseInt(stringNumero2);

        if (opcion.equals("Sumar")) {
            int resultado = intNumero1 + intNumero2;
            textViewResultado.setText(String.valueOf(resultado));
        } else if (opcion.equals("Restar")) {
            int resultado = intNumero1 - intNumero2;
            textViewResultado.setText(String.valueOf(resultado));
        } else if (opcion.equals("Multiplicar")) {
            int resultado = intNumero1 * intNumero2;
            textViewResultado.setText(String.valueOf(resultado));
        } else {
            if (intNumero2 == 0) {
                textViewResultado.setText("");
                return;
            }
            int resultado = intNumero1 / intNumero2;
            textViewResultado.setText(String.valueOf(resultado));
        }
    }
}