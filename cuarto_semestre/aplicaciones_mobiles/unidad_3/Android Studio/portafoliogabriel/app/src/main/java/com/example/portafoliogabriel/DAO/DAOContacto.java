package com.example.portafoliogabriel.DAO;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class DAOContacto {
    private final DatabaseReference referencia;

    public DAOContacto() {
        referencia = FirebaseDatabase.getInstance().getReference("contactos");
    }

    public DatabaseReference getReferencia() {
        return referencia;
    }

    public void InsertarContacto(Contacto contacto) {
        referencia.push().setValue(contacto);
    }

}
