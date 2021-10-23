public class Main {
    public static void main(String[] args) throws Exception {
        Licencia camion = new Licencia(1234, "A", "permite conducir camiones");
        Conductor mike = new Conductor("14.534.654-4", "Mike Gordon", "Ovalle 3424", 124324, camion);
        // mike.setLicencia(4321, "B", "solo para autos");
        System.out.println(camion.infoLicencia());
        System.out.println(mike.infoLicencia());

        System.out.println("");

        Profesion vaquero = new Profesion("vaquero", "a1b2c3");
        Gerente billy = new Gerente("12.533.631-5", "Bill Nye", "ajsdjf 35", "+56951892378", "test@test.com", "que", vaquero);

        System.out.println(vaquero.infoProfesion());
        System.out.println(billy.infoProfesion());

        System.out.println("");

        System.out.println(mike.infoPersona());
        System.out.println(billy.infoPersona());
    }
}