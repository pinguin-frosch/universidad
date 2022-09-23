package com.example.evaluacion1gabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class Resultado extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_resultado);

        TextView resultado_signo = findViewById(R.id.tv_signo);
        Bundle extras = getIntent().getExtras();
        String signo = extras.getString("signo");

        resultado_signo.setText(signo);
    }
}