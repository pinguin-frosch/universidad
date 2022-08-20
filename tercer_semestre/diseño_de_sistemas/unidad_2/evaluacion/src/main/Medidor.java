package main;

import java.util.ArrayList;

public class Medidor {
    private String identificador;

    public String getIdentificador() {
        return identificador;
    }

    public void setIdentificador(String identificador) {
        this.identificador = identificador;
    }

    private Dueño dueño;

    public Dueño getDueño() {
        return dueño;
    }

    private ArrayList<Boleta> boletas;

    public ArrayList<Boleta> getBoletas() {
        return boletas;
    }

    public void setBoletas(ArrayList<Boleta> boletas) {
        this.boletas = boletas;
    }

    private ArrayList<Pago> pagos;

    public ArrayList<Pago> getPagos() {
        return pagos;
    }

    public void setPagos(ArrayList<Pago> pagos) {
        this.pagos = pagos;
    }

    public Medidor(String identificador, Dueño dueño, ArrayList<Boleta> boletas) {
        this.identificador = identificador;
        this.dueño = dueño;
        this.boletas = boletas;
    }

    public void registroPago(Pago pago) {
        ArrayList<Pago> pagos = getPagos();
        pagos.add(pago);
        setPagos(pagos);
    }

    public void registroBoleta(Boleta boleta) {
        ArrayList<Boleta> boletas = getBoletas();
        boletas.add(boleta);
        setBoletas(boletas);
    }
}
