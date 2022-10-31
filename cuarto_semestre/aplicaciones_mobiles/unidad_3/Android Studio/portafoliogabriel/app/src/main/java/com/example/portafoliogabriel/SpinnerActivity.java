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
    private Spinner sOpciones;
    private TextView tvResultado;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_spinner);

        etNumero1 = findViewById(R.id.sEditTextNumero1);
        etNumero2 = findViewById(R.id.sEditTextNumero2);
        sOpciones = findViewById(R.id.sSpinnerOpciones);
        tvResultado = findViewById(R.id.sTextViewResultado);

        String[] opciones = {"Sumar", "Restar", "Multiplicar", "Dividir"};
        ArrayAdapter<String> adaptador = new ArrayAdapter<String>(this, androidx.appcompat.R.layout.support_simple_spinner_dropdown_item, opciones);
        sOpciones.setAdapter(adaptador);
    }

    public void operar(View view) {
        String sNumero1 = etNumero1.getText().toString();
        String sNumero2 = etNumero2.getText().toString();

        if (sNumero2.equals("") || sNumero1.equals("")) {
            tvResultado.setText("");
            return;
        }

        String opcion = sOpciones.getSelectedItem().toString();

        int iNumero1 = Integer.parseInt(sNumero1);
        int iNumero2 = Integer.parseInt(sNumero2);

        if (opcion.equals("Sumar")) {
            int resultado = iNumero1 + iNumero2;
            tvResultado.setText(String.valueOf(resultado));
        } else if (opcion.equals("Restar")) {
            int resultado = iNumero1 - iNumero2;
            tvResultado.setText(String.valueOf(resultado));
        } else if (opcion.equals("Multiplicar")) {
            int resultado = iNumero1 * iNumero2;
            tvResultado.setText(String.valueOf(resultado));
        } else {
            if (iNumero2 == 0) {
                tvResultado.setText("");
                return;
            }
            int resultado = iNumero1 / iNumero2;
            tvResultado.setText(String.valueOf(resultado));
        }
    }
}