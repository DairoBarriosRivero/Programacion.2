import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
//
//@Dairo
//
public class Vector {

    public static void main(String[] args) {
        // 1.
        List<String> listaVacia = new ArrayList<>();
        System.out.println("Lista vacía creada: " + listaVacia);
        
        // 2.
        List<Integer> listaConElementos = new ArrayList<>();
        listaConElementos.add(10);
        listaConElementos.add(20);
        listaConElementos.add(30);
        listaConElementos.add(40);
        listaConElementos.add(50);
        listaConElementos.add(60);
        System.out.println("Lista con más de 5 elementos: " + listaConElementos);
        
        // 3.
        System.out.println("Longitud de la lista vacía: " + listaVacia.size());
        System.out.println("Longitud de la lista con más de 5 elementos: " + listaConElementos.size());
        
        // 4.
        var primerElemento = listaVacia.isEmpty() ? null : listaVacia.get(0);
        int elementoCentral = listaConElementos.isEmpty() ? null : listaConElementos.get(listaConElementos.size() / 2);
        int ultimoElemento = listaConElementos.isEmpty() ? null : listaConElementos.get(listaConElementos.size() - 1);

        System.out.println("Primer elemento de la lista vacía: " + primerElemento);
        System.out.println("Elemento central de la lista con más de 5 elementos: " + elementoCentral);
        System.out.println("Último elemento de la lista con más de 5 elementos: " + ultimoElemento);

        
        // 5.
        List<String> datosPersonales = new ArrayList<>();
        datosPersonales.add("Dairo");
        datosPersonales.add("17 años");
        datosPersonales.add("180 cm");
        datosPersonales.add("Soltero");
        datosPersonales.add("Calle Principal, San jose de los campanos");

        System.out.println("Datos personales: " + datosPersonales);
        
        //6.
        List<String> itCompanies = new ArrayList<>();
        itCompanies.add("Facebook");
        itCompanies.add("Google");
        itCompanies.add("Microsoft");
        itCompanies.add("Apple");
        itCompanies.add("IBM");
        itCompanies.add("Oracle");
        itCompanies.add("Amazon");

        System.out.println("Empresas de tecnología: " + itCompanies);
        // 7.
        itCompanies.add("Samsung");
        System.out.println("Empresas de tecnología actualizadas: " + itCompanies);
        
        // 8.
        String empresaBuscada = "Microsoft";
        boolean existe = itCompanies.contains(empresaBuscada);
        System.out.println("¿La empresa " + empresaBuscada + " existe en la lista? " + existe);
        
        // 9.
        Collections.sort(itCompanies);
        System.out.println("Empresas de tecnología ordenadas alfabéticamente: " + itCompanies);
        
        // 10.
        Collections.reverse(itCompanies);
        System.out.println("Empresas de tecnología invertidas en orden descendente: " + itCompanies);
            
        // 11.
        itCompanies.remove(0);
        System.out.println("Lista de empresas de tecnología después de eliminar la primera empresa: " + itCompanies);
        
        // 12.
        itCompanies.clear();
        System.out.println("Lista de empresas de tecnología después de eliminar todas: " + itCompanies);  
       }
}