import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese las notas separadas por comas: ");
        String[] partes = scanner.nextLine().split(",");
        float total = 0;
        for (String nota : partes) {
            total += Float.parseFloat(nota);
        }
        float promedio = total / partes.length;
        System.out.println("Promedio: " + promedio);
        scanner.close();
    }
}
