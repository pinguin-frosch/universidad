package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
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
            return;
        }

        int iNumero = Integer.parseInt(sNumero);

        String sSigno;

        if (iNumero > 0) {
            sSigno = "Positivo";
        } else if (iNumero < 0) {
            sSigno = "Negativo";
        } else {
            sSigno = "Neutro";
        }

        tvSigno.setText(sSigno);
    }
}