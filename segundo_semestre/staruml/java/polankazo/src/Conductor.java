public class Conductor extends Persona {
    private int codConductor;
    private Licencia licencia;

    // Constructores
    Conductor() {

    }
    Conductor(String run, String nombre, String direccion, int codConductor, Licencia licencia) {
        super(run, nombre, direccion);
        this.codConductor = codConductor;
        this.licencia = licencia;
    }

    // Getters
    public int getCodConductor() {
        return codConductor;
    }
    public Licencia getLicencia() {
        return licencia;
    }

    // Setters
    public void setCodConductor(int codConductor) {
        this.codConductor = codConductor;
    }
    public void setLicencia(int codigo, String tipo, String detalle) {
        this.licencia = new Licencia(codigo, tipo, detalle);
    }

    public String infoLicencia() {
        return String.format("Mi licencia de conducir es %d.", licencia.getCodigo());
    }
}