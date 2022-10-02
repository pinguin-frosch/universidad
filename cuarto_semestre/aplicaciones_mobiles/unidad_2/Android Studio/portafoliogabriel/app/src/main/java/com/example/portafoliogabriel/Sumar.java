package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class Sumar extends AppCompatActivity {

    EditText editTextNumero1, editTextNumero2;
    TextView textViewResultado;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sumar);

        editTextNumero1 = findViewById(R.id.editTextNumero1);
        editTextNumero2 = findViewById(R.id.editTextNumero2);
        textViewResultado = findViewById(R.id.textViewResultado);
    }

    public void sumar(View view) {
        String stringNumero1 = editTextNumero1.getText().toString();
        String stringNumero2 = editTextNumero2.getText().toString();

        if (stringNumero1.equals("") || stringNumero2.equals("")) {
            return;
        }

        int intNumero1 = Integer.parseInt(stringNumero1);
        int intNumero2 = Integer.parseInt(stringNumero2);

        int intResultado = intNumero1 + intNumero2;

        textViewResultado.setText(String.valueOf(intResultado));
    }
}