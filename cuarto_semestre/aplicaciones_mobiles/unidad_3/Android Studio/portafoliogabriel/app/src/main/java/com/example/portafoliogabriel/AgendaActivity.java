package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class AgendaActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_agenda);
    }

    public void iniciarAgregarContactosActivity(View view) {
        Intent i = new Intent(this, AgregarContactosActivity.class);
        startActivity(i);
    }

}