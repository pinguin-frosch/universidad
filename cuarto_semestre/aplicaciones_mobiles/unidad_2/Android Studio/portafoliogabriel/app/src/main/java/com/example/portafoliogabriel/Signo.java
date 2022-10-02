package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class Signo extends AppCompatActivity {

    EditText editTextNumero;
    TextView textViewSigno;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signo);

        editTextNumero = findViewById(R.id.editTextNumero);
        textViewSigno = findViewById(R.id.textViewSigno);
    }

    public void determinarSigno(View view) {
        String stringNumero = editTextNumero.getText().toString();

        if (stringNumero.equals("")) {
            return;
        }

        int intNumero = Integer.parseInt(stringNumero);

        String stringSigno;

        if (intNumero > 0) {
            stringSigno = "Positivo";
        } else if (intNumero < 0) {
            stringSigno = "Negativo";
        } else {
            stringSigno = "Neutro";
        }

        textViewSigno.setText(stringSigno);
    }
}