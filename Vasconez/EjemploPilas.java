import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ListaTareas {
    public static void main(String[] args) {
        List<String> tareas = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        String opcion;

        do {
            System.out.println("== Aplicación de Lista de Tareas ==");
            System.out.println("1. Agregar tarea");
            System.out.println("2. Mostrar tareas");
            System.out.println("3. Eliminar tarea");
            System.out.println("4. Salir");
            System.out.print("Ingrese una opción: ");
            opcion = scanner.nextLine();

            switch (opcion) {
                case "1":
                    System.out.print("Ingrese la tarea a agregar: ");
                    String nuevaTarea = scanner.nextLine();
                    tareas.add(nuevaTarea);
                    System.out.println("Tarea agregada con éxito.");
                    break;
                case "2":
                    System.out.println("Lista de tareas:");
                    for (int i = 0; i < tareas.size(); i++) {
                        System.out.println((i + 1) + ". " + tareas.get(i));
                    }
                    break;
                case "3":
                    System.out.print("Ingrese el número de la tarea a eliminar: ");
                    int numeroTareaEliminar = Integer.parseInt(scanner.nextLine());
                    if (numeroTareaEliminar >= 1 && numeroTareaEliminar <= tareas.size()) {
                        tareas.remove(numeroTareaEliminar - 1);
                        System.out.println("Tarea eliminada correctamente.");
                    } else {
                        System.out.println("Número de tarea inválido.");
                    }
                    break;
                case "4":
                    System.out.println("¡Hasta luego!");
                    break;
                default:
                    System.out.println("Opción inválida. Intente nuevamente.");
            }

            System.out.println();
        } while (!opcion.equals("4"));
    }
}