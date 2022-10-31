package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;

public class SpinnerActivity extends AppCompatActivity {

    private EditText etNumero1, etNumero2;
    private Spinner spOpciones;
    private TextView tvResultado;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_spinner);

        etNumero1 = findViewById(R.id.spEtNumero1);
        etNumero2 = findViewById(R.id.spEtNumero2);
        spOpciones = findViewById(R.id.spSpOpciones);
        tvResultado = findViewById(R.id.spTvResultado);

        String[] opciones = {"Sumar", "Restar", "Multiplicar", "Dividir"};
        ArrayAdapter<String> adaptador = new ArrayAdapter<>(this, androidx.appcompat.R.layout.support_simple_spinner_dropdown_item, opciones);
        spOpciones.setAdapter(adaptador);
    }

    public void operar(View view) {
        String sNumero1 = etNumero1.getText().toString();
        String sNumero2 = etNumero2.getText().toString();

        if (sNumero2.equals("") || sNumero1.equals("")) {
            tvResultado.setText("");
            return;
        }

        String opcion = spOpciones.getSelectedItem().toString();

        double numero1 = Double.parseDouble(sNumero1);
        double numero2 = Double.parseDouble(sNumero2);

        if (opcion.equals("Sumar")) {
            double resultado = numero1 + numero2;
            tvResultado.setText(String.valueOf(resultado));
        } else if (opcion.equals("Restar")) {
            double resultado = numero1 - numero2;
            tvResultado.setText(String.valueOf(resultado));
        } else if (opcion.equals("Multiplicar")) {
            double resultado = numero1 * numero2;
            tvResultado.setText(String.valueOf(resultado));
        } else {
            if (numero2 == 0) {
                tvResultado.setText("");
                return;
            }
            double resultado = numero1 / numero2;
            tvResultado.setText(String.valueOf(resultado));
        }
    }
}