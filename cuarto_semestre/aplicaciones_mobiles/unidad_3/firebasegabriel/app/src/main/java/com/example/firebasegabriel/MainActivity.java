package com.example.firebasegabriel;

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

    public void iniciarAgregarContactosActivity(View view) {
        Intent i = new Intent(this, AgregarContactoActivity.class);
        startActivity(i);
    }

}