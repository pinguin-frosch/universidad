package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class SignoActivity extends AppCompatActivity {

    EditText etNumero;
    TextView tvSigno;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signo);

        etNumero = findViewById(R.id.siEtNumero);
        tvSigno = findViewById(R.id.siTvSigno);
    }

    public void determinarSigno(View view) {
        String sNumero = etNumero.getText().toString();

        if (sNumero.equals("")) {
            tvSigno.setText("");
            return;
        }

        double numero = Double.parseDouble(sNumero);
        String signo;

        if (numero > 0) {
            signo = "Positivo";
        } else if (numero < 0) {
            signo = "Negativo";
        } else {
            signo = "Neutro";
        }

        tvSigno.setText(signo);
    }
}