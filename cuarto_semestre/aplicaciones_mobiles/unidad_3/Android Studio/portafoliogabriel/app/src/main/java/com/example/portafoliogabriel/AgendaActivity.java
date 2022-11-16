package com.example.portafoliogabriel;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import com.example.portafoliogabriel.DAO.Contacto;
import com.example.portafoliogabriel.DAO.DAOContacto;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.ValueEventListener;

public class AgendaActivity extends AppCompatActivity {

    private ListView lvListView;
    private ArrayAdapter<String> adaptador;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_agenda);
        lvListView = findViewById(R.id.agLvListView);
        adaptador = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1);

        DAOContacto dao = new DAOContacto();
        dao.getReferencia().addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                adaptador.clear();

                for (DataSnapshot contacto_actual : snapshot.getChildren()) {
                    Contacto contacto = contacto_actual.getValue(Contacto.class);
                    if (contacto != null) {
                        adaptador.add(contacto.getNombre());
                    }
                }

                lvListView.setAdapter(adaptador);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });
    }

    public void iniciarAgregarContactosActivity(View view) {
        Intent i = new Intent(this, AgregarContactosActivity.class);
        startActivity(i);
    }

}