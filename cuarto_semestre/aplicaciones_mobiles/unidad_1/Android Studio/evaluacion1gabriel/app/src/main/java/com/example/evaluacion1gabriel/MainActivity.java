package com.example.evaluacion1gabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    EditText numero;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        numero = findViewById(R.id.et_number);
    }

    public void detectar(View view) {
        String numText = numero.getText().toString();

        if (numText.equals("")) {
            return;
        }

        int numInt = Integer.parseInt(numText);

        String signo;

        if (numInt > 0) {
            signo = "El número es positivo";
        } else if (numInt < 0) {
            signo = "El número es negativo";
        } else {
            signo = "El número es neutro";
        }

        Bundle extras = new Bundle();
        extras.putString("signo", signo);

        Intent i = new Intent(this, Resultado.class);
        i.putExtras(extras);
        startActivity(i);
    }
}