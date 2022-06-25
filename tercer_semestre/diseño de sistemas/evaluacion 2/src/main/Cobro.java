package main;

import java.util.Date;

public class Cobro {
    private String tipoCobro;

    public String getTipoCobro() {
        return tipoCobro;
    }

    public void setTipoCobro(String tipoCobro) {
        this.tipoCobro = tipoCobro;
    }

    private Date fecha;

    public Date getFecha() {
        return fecha;
    }

    public void setFecha(Date fecha) {
        this.fecha = fecha;
    }

    private int montoCobro;

    public int getMontoCobro() {
        return montoCobro;
    }

    public void setMontoCobro(int montoCobro) {
        this.montoCobro = montoCobro;
    }

    Cobro(String tipoCobro, Date fecha, int montoCobro) {
        this.tipoCobro = tipoCobro;
        this.fecha = fecha;
        this.montoCobro = montoCobro;
    }
}
