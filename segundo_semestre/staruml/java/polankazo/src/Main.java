public class Main {
    public static void main(String[] args) throws Exception {
        Gerente gabriel = new Gerente("21.019.385-5", "Gabriel Barrientos", "Santa Teresa 738", "+56966842427", "gabri12.rubik@gmail.com", "password");
        Conductor mike = new Conductor("14.534.654-4", "Mike Gordon", "Ovalle 3424", 124324);
        Licencia fg = new Licencia(1234, "A", "permite conducir camiones");
        System.out.println(gabriel.infoPersona());
        System.out.println(mike.infoPersona());
        System.out.println(fg.infoLicencia());
    }
}