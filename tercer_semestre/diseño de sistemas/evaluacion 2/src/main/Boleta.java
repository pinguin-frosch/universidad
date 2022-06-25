package main;

import java.util.ArrayList;

public class Boleta {
    private String numeroBoleta;

    public String getNumeroBoleta() {
        return numeroBoleta;
    }

    public void setNumeroBoleta(String numeroBoleta) {
        this.numeroBoleta = numeroBoleta;
    }

    private ArrayList<Cobro> cobros;

    public ArrayList<Cobro> getCobros() {
        return cobros;
    }

    public void setCobros(ArrayList<Cobro> cobros) {
        this.cobros = cobros;
    }

    Boleta(String numeroBoleta, ArrayList<Cobro> cobros) {
        this.numeroBoleta = numeroBoleta;
        this.cobros = cobros;
    }

    public void añadirCobro(Cobro cobro) {
        ArrayList<Cobro> cobros = getCobros();
        cobros.add(cobro);
        setCobros(cobros);
    }
}
