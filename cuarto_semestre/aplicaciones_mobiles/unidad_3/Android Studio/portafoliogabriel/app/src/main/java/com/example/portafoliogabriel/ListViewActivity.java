package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;

public class ListViewActivity extends AppCompatActivity {

    private ListView lvNombres;
    private TextView tvNumero;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_list_view);

        lvNombres = findViewById(R.id.lvListView);
        tvNumero = findViewById(R.id.lvTvNumero);

        String[] nombres = {"asdf", "fdsa", "afsd"};
        String[] numeros = {"1234", "4321", "1423"};

        ArrayAdapter<String> adaptador = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, nombres);
        lvNombres.setAdapter(adaptador);

        lvNombres.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                tvNumero.setText(numeros[i]);
            }
        });
    }
}