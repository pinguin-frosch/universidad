package com.example.evaluacion3gabrielbarrientos.dao;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class DaoUsuario {
    private final DatabaseReference referencia;

    public DaoUsuario() {
        referencia = FirebaseDatabase.getInstance().getReference("usuarios");
    }

    public DatabaseReference getReferencia() {
        return referencia;
    }

    public void insertarUsuario(Usuario usuario) {
        String rut = usuario.getRut();
        usuario.setRut(null);
        referencia.child(rut).setValue(usuario);
    }

    public void eliminarUsuario(Usuario usuario) {
        String rut = usuario.getRut();
        referencia.child(rut).removeValue();
    }
}
