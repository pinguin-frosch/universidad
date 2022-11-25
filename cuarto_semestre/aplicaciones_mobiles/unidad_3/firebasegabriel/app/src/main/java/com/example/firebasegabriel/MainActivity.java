package com.example.firebasegabriel;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;

import com.example.firebasegabriel.dao.Contacto;
import com.example.firebasegabriel.dao.DaoContacto;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.ValueEventListener;

public class MainActivity extends AppCompatActivity {
    private ListView listaContactos;
    private ArrayAdapter<Contacto> adaptador;
    private EditText etNombre;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etNombre = findViewById(R.id.etNombre);
        listaContactos = findViewById(R.id.lvContactos);
        adaptador = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1);
        listaContactos.setAdapter(adaptador);

        listaContactos.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                iniciarDetallesContactoActivity(adaptador.getItem(i));
            }
        });

        DaoContacto dao = new DaoContacto();
        dao.getReferencia().orderByChild("nombre").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                adaptador.clear();

                for (DataSnapshot contactoActual : snapshot.getChildren()) {
                    Contacto contacto = contactoActual.getValue(Contacto.class);
                    if (contacto != null) {
                        contacto.setId(contactoActual.getKey());
                        adaptador.add(contacto);
                    }
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });
    }

    public void iniciarAgregarContactosActivity(View view) {
        Intent i = new Intent(this, AgregarContactoActivity.class);
        startActivity(i);
    }

    public void iniciarDetallesContactoActivity(Contacto contacto) {
        Bundle extras = new Bundle();
        extras.putSerializable("contacto", contacto);

        Intent i = new Intent(this, DetallesContactoActivity.class);
        i.putExtras(extras);
        startActivity(i);
    }

    public void buscarContactos(View view) {
        String nombre = etNombre.getText().toString();

        DaoContacto dao = new DaoContacto();

        dao.getReferencia().orderByChild("nombre").startAt(nombre).endAt(nombre + "ÿ").addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                adaptador.clear();

                for (DataSnapshot contactoActual : snapshot.getChildren()) {
                    Contacto contacto = contactoActual.getValue(Contacto.class);
                    if (contacto != null) {
                        contacto.setId(contactoActual.getKey());
                        adaptador.add(contacto);
                    }
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });
    }

}