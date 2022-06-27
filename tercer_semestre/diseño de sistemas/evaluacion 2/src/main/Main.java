package main;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Dueño dueño = new Dueño("21.019.385-5", "Gabriel", "Barrientos", "Santa Teresa 738");
        Empleador empleador = new Empleador("21.153.307-2", "Charlotte", "Rodriguez", "+56948261973");
        ArrayList<Boleta> boletas = new ArrayList<Boleta>();
        Medidor medidor = new Medidor("1111", dueño, boletas);

        ArrayList<Cobro> cobros = new ArrayList<Cobro>();
        Boleta boleta = new Boleta("1", cobros);
        Cobro consumoMensual = empleador.hacerMedicion(15000);

        boleta.añadirCobro(consumoMensual);

        for (Cobro cobro : boleta.getCobros()) {
            System.out.println(cobro.getTipoCobro());
            System.out.println(cobro.getMontoCobro());
        }
    }
}
