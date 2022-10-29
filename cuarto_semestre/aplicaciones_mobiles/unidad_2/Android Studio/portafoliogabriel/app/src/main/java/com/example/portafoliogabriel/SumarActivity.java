package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class SumarActivity extends AppCompatActivity {

    EditText etNumero1, etNumero2;
    TextView tvResultado;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sumar);

        etNumero1 = findViewById(R.id.suEtNumero1);
        etNumero2 = findViewById(R.id.suEtNumero2);
        tvResultado = findViewById(R.id.suTvResultado);
    }

    public void sumar(View view) {
        String sNumero1 = etNumero1.getText().toString();
        String sNumero2 = etNumero2.getText().toString();

        if (sNumero1.equals("") || sNumero2.equals("")) {
            return;
        }

        int iNumero1 = Integer.parseInt(sNumero1);
        int iNumero2 = Integer.parseInt(sNumero2);

        int intResultado = iNumero1 + iNumero2;

        tvResultado.setText(String.valueOf(intResultado));
    }
}