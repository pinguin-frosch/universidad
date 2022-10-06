package com.example.contador;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private long contador;
    private TextView tvContador;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        contador = 0;
        tvContador = findViewById(R.id.tvContador);
        mostrar();
    }

    public void sumar(View view) {
        contador += 1;
        mostrar();
    }

    public void restar(View view) {
        if (contador > 0) {
            contador -= 1;
        }
        mostrar();
    }

    public void reiniciar(View view) {
        contador = 0;
        mostrar();
    }

    private void mostrar() {
        tvContador.setText(String.valueOf(contador));
    }
}