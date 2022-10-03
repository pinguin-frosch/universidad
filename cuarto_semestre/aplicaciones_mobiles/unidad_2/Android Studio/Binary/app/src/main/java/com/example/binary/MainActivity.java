package com.example.binary;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.CheckBox;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    CheckBox checkBox0, checkBox1, checkBox2, checkBox3;
    TextView textViewResultado;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        checkBox0 = findViewById(R.id.checkBox0);
        checkBox1 = findViewById(R.id.checkBox1);
        checkBox2 = findViewById(R.id.checkBox2);
        checkBox3 = findViewById(R.id.checkBox3);
        textViewResultado = findViewById(R.id.textViewResultado);
    }

    public void calcular(View view) {
        int valor = 0;

        if (checkBox0.isChecked()) {
            valor += Math.pow(2, 0);
        }
        if (checkBox1.isChecked()) {
            valor += Math.pow(2, 1);
        }
        if (checkBox2.isChecked()) {
            valor += Math.pow(2, 2);
        }
        if (checkBox3.isChecked()) {
            valor += Math.pow(2, 3);
        }

        textViewResultado.setText(String.valueOf(valor));
    }
}