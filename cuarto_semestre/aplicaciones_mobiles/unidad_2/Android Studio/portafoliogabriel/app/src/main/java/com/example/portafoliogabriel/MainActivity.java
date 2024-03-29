package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void iniciarSumar(View view) {
        Intent i = new Intent(this, SumarActivity.class);
        startActivity(i);
    }

    public void iniciarOperacionesConRadio(View view) {
        Intent i = new Intent(this, RadioActivity.class);
        startActivity(i);
    }

    public void iniciarSigno(View view) {
        Intent i = new Intent(this, SignoActivity.class);
        startActivity(i);
    }

    public void iniciarOperacionesConCheckbox(View view) {
        Intent i = new Intent(this, CheckboxActivity.class);
        startActivity(i);
    }

    public void iniciarSpinnerActivity(View view) {
        Intent i = new Intent(this, SpinnerActivity.class);
        startActivity(i);
    }

    public void iniciarListViewActivity(View view) {
        Intent i = new Intent(this, ListViewActivity.class);
        startActivity(i);
    }

    public void iniciarAgendaActivity(View view) {
        Intent i = new Intent(this, AgendaActivity.class);
        startActivity(i);
    }
}