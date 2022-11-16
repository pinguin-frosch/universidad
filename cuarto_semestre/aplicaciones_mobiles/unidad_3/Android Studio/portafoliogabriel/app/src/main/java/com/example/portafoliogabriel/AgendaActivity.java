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

    // Declarar el listView y el adaptador
    // No se pueden asignar aquí porque aún no se "crean"
    // los elementos de android que necesitamos (id, layout, etc)
    private ListView listaContactos;
    private ArrayAdapter<String> adaptador;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_agenda);

        // Asignar el listView a su elemento correspondiente en el .xml
        listaContactos = findViewById(R.id.agLvListView);

        // Asignar el adaptador con el contexto, además de indicar que tendrá el estilo
        // de un elemento simple en una lista
        adaptador = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1);

        // Vincular el listView con el adaptador
        listaContactos.setAdapter(adaptador);

        // Obtener dao para trabajar con las referencias de la base de datos
        DAOContacto dao = new DAOContacto();

        // Añadir un escuchador de evento de firebase
        dao.getReferencia().addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {

                // Borrar elementos del adaptador
                adaptador.clear();

                // Iterar por cada uno de los contactos
                for (DataSnapshot contacto_actual : snapshot.getChildren()) {
                    Contacto contacto = contacto_actual.getValue(Contacto.class);

                    // Agregar el nombre del contacto al adaptador solo si no es nulo
                    if (contacto != null) {
                        adaptador.add(contacto.getNombre());
                    }

                }
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