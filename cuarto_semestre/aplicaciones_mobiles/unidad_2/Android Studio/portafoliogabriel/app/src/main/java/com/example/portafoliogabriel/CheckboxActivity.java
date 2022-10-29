package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.Toast;

public class CheckboxActivity extends AppCompatActivity {

    EditText etNumero1, etNumero2;
    CheckBox cbSumar, cbRestar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_checkbox);

        etNumero1 = findViewById(R.id.chEtNumero1);
        etNumero2 = findViewById(R.id.chEtNumero2);
        cbSumar = findViewById(R.id.chCbSumar);
        cbRestar = findViewById(R.id.chCbRestar);
    }

    @SuppressLint("DefaultLocale")
    public void operar(View view) {
        String sNumero1 = etNumero1.getText().toString();
        String sNumero2 = etNumero2.getText().toString();

        if (sNumero1.equals("") || sNumero2.equals("")) {
            return;
        }

        int iNumero1 = Integer.parseInt(sNumero1);
        int iNumero2 = Integer.parseInt(sNumero2);
        String sResultado;

        if (cbSumar.isChecked() && cbRestar.isChecked()) {
            int suma = iNumero1 + iNumero2;
            int resta = iNumero1 - iNumero2;
            sResultado = String.format("%d + %d = %d, %d - %d = %d", iNumero1, iNumero2, suma, iNumero1, iNumero2, resta);
        } else if (cbSumar.isChecked()) {
            int suma = iNumero1 + iNumero2;
            sResultado = String.format("%d + %d = %d", iNumero1, iNumero2, suma);
        } else if (cbRestar.isChecked()) {
            int resta = iNumero1 - iNumero2;
            sResultado = String.format("%d - %d = %d", iNumero1, iNumero2, resta);
        } else {
            return;
        }

        Toast.makeText(this, sResultado, Toast.LENGTH_LONG).show();
    }
}