public class Conductor extends Persona {
    private int codConductor;

    // Constructores
    Conductor() {

    }
    Conductor(String run, String nombre, String direccion, int codConductor) {
        super(run, nombre, direccion);
        this.codConductor = codConductor;
    }

    // Getters
    public int getCodConductor() {
        return codConductor;
    }

    // Setters
    public void setCodConductor(int codConductor) {
        this.codConductor = codConductor;
    }
}