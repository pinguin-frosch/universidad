package com.example.firebasegabriel.dao;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class DaoContacto {
    private final DatabaseReference referencia;

    public DaoContacto() {
        referencia = FirebaseDatabase.getInstance().getReference("contactos");
    }

    public DatabaseReference getReferencia() {
        return referencia;
    }

    public void insertarContacto(Contacto contacto) {
        referencia.push().setValue(contacto);
    }
}
