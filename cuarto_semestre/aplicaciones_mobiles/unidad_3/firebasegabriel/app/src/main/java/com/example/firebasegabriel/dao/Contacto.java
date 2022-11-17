package com.example.firebasegabriel.dao;

import androidx.annotation.NonNull;

public class Contacto {
    private String nombre;
    private String numero;

    public Contacto() {

    }

    @Override
    public String toString() {
        return nombre;
    }

    public Contacto(String nombre, String numero) {
        this.nombre = nombre;
        this.numero = numero;
    }

    public String getNombre() {
        if (nombre == null) {
            return "";
        }
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNumero() {
        if (numero == null) {
            return "";
        }
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }
}
