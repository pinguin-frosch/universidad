package com.example.a001;

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

    // Método para arrancar la actividad del checkbox (mini aplicación)
    public void startCheckBox(View view) {
        Intent i = new Intent(this, Checkbox.class);
        startActivity(i);
    }
}