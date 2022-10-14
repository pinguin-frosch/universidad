package com.example.portafoliogabriel;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;

public class ListViewActivity extends AppCompatActivity {

    private ListView listViewNombres;
    private TextView textViewNumero;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_list_view);

        listViewNombres = findViewById(R.id.lvListView);
        textViewNumero = findViewById(R.id.lvTextView);

        String[] nombres = {"asdf", "fdsa", "afsd"};
        String[] numeros = {"1234", "4321", "1423"};

        ArrayAdapter adapter = new ArrayAdapter(this, android.R.layout.simple_list_item_1, nombres);
        listViewNombres.setAdapter(adapter);

        listViewNombres.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                textViewNumero.setText(numeros[i]);
            }
        });
    }
}