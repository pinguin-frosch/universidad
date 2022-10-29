package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;

public class RadioActivity extends AppCompatActivity {

    RadioButton rbSumar, rbRestar, rbMultiplicar, rbDividir;
    EditText etNumero1, etNumero2;
    TextView tvResultado;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_radio);

        rbSumar = findViewById(R.id.raRbSumar);
        rbRestar = findViewById(R.id.raRbRestar);
        rbMultiplicar = findViewById(R.id.raRbMultiplicar);
        rbDividir = findViewById(R.id.raRbDividir);
        etNumero1 = findViewById(R.id.raEtNumero1);
        etNumero2 = findViewById(R.id.raEtNumero2);
        tvResultado = findViewById(R.id.raTvResultado);
    }

    public void operar(View view) {
        String sNumero1 = etNumero1.getText().toString();
        String sNumero2 = etNumero2.getText().toString();

        if (sNumero1.equals("") || sNumero2.equals("")) {
            return;
        }

        float fNumero1 = Float.parseFloat(sNumero1);
        float fNumero2 = Float.parseFloat(sNumero2);
        float fResultado;

        if (rbSumar.isChecked()) {
            fResultado = fNumero1 + fNumero2;
        } else if (rbRestar.isChecked()) {
            fResultado = fNumero1 - fNumero2;
        } else if (rbMultiplicar.isChecked()) {
            fResultado = fNumero1 * fNumero2;
        } else {
            fResultado = fNumero1 / fNumero2;
        }

        tvResultado.setText(String.valueOf(fResultado));
    }
}