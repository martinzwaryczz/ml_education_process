# Encapsulamiento

## Ejercicios

1. Implementar la clase Nota

```java
class Nota {

    /**
     * pre : valorInicial está comprendido entre 0 y 10.
     * post: inicializa la Nota con el valor indicado.
     */
    public Nota(int valorInicial) { }
    
    /**
     * post: devuelve el valor numérico de la Nota, comprendido entre 0 y 10.
     */
    public int obtenerValor() { }
    
    /**
     * post: indica si la Nota permite o no la aprobación.
     */
    public boolean aprobado() { }
    
    /**
     * post: indica si la Nota implica desaprobación.
     */
    public boolean desaprobado() { }
    
}
```

1.2. Agregar a la clase Nota el método:

```java
    /**
     * pre : nuevoValor está comprendido entre 0 y 10.
     * post: modifica el valor numérico de la Nota, cambiándolo por nuevoValor, siempre y cuando nuevoValor sea superior al valor numérico actual de la Nota.
    */
    public void recuperar(int nuevoValor) { }
```

2. Defina una clase Punto que tendrá dos atributos, de tipo double, x e y, que representarán las coordenadas del punto dentro del plano. Implemente los siguientes métodos:

    ```java
    public boolean estaSobreElEjeX() {}
    public boolean estaSobreElEjeY() {}
    public boolean esElOrigenDeCoordenadas() {}
    public double distanciaAlOrigen() {}
    public static double distancia(Punto p1, Punto p2) {}
    public double distancia(Punto p) {}
    ```

2.1. Implementar una clase que modele un círculo, del que se desea manipular (obtener y cambiar):
    * radio
    * diámetro
    * perímetro
    * área

2.2. Implementar una clase que modele una corona circular utilizando la clase Circulo desarrollada previamente. Se desea manipular (obtener y cambiar):
    * radio interior
    * radio exterior
    * perímetro interior
    * perímetro exterior
    * área

3. Implementar la clase Cubo a partir de la siguiente interfaz:

```java
class Cubo {

    /**
     * pre : longitudLado es un valor mayor a 0.
     * post: inicializa el cubo a partir de la longitud de lado dada
     */
    public Cubo (double longitudLado) { }

    /**
     * post: devuelve la longitud de todos los lados del cubo
     */
    public double obtenerLado() { }
    
    /**
     * pre : longitudLado es un valor mayor a 0.
     * post: cambia la longitud de todos los lados del cubo
     */
    public void cambiarLado(double longitudLado) { }
    
    /**
     * post: devuelve el área de la superficie de las caras del cubo
     */
    public double obtenerAreaCara() { }
    
    /**
     * pre: areaCara es un valor mayor a 0.
     * post: cambia el área de las caras del cubo
     */
    public void cambiarAreaCara(double areaCara) { }

    /**
     * post: devuelve el volumen que encierra el cubo
     */
    public double obtenerVolumen() { }

    /**
     * pre: volumen es un valor mayor a 0.
     * post: cambia el volumen del cubo
     */
    public void cambiarVolumen(double volumen) { }
}
```

4. Implementar la clase TarjetaBaja a partir de la siguiente declaración:

```java
class TarjetaBaja {

    /**
     * post: saldo de la Tarjeta en saldoInicial.
     */
    public TarjetaBaja(double saldoInicial) { }

    /**
     * post: devuelve el saldo actual de la Tarjeta
     */
    public double obtenerSaldo() { } 

    /**
     * post: agrega el monto al saldo de la Tarjeta.
     */
    public void cargar(double monto) { }

    /**
     * pre : saldo suficiente.
     * post: utiliza 21.50 del saldo para un viaje en colectivo.
     */
    public void pagarViajeEnColectivo() { }

    /**
     * pre : saldo suficiente.
     * post: utiliza 19.50 del saldo para un viaje en subte. 
     */
    public void pagarViajeEnSubte() { }

    /**
     * post: devuelve la cantidad de viajes realizados.
     */
    public int contarViajes() { }

    /**
     * post: devuelve la cantidad de viajes en colectivo.
     */
    public int contarViajesEnColectivo() { }

    /**
     * post: devuelve la cantidad de viajes en subte.
     */
    public int contarViajesEnSubte() { }
}
```

5. Implementar la clase Ticket a partir de la siguiente interfaz

```java
class Ticket {

    /**
     * post: el Ticket se inicializa con importe 0.
     */
    public Ticket() { }

    /**
     * pre : cantidad y precio son mayores a cero. El ticket está abierto.
     * post: suma al Ticket un item a partir de la cantidad de productos y su precio unitario.
     */
    public void agregarItem(int cantidad, double precioUnitario) { }

    /**
     * pre : está abierto y no se ha aplicado un descuento previamente.
     * post: aplica un descuento sobre el total del importe.
     */
    public void aplicarDescuento(double porcentaje) { }

    /**
     * post: devuelve el importe acumulado hasta el momento, sin cerrar el Ticket.
     */
    public double calcularSubtotal() { }

    /**
     * post: cierra el Ticket y devuelve el importe total.
     */
    public double calcularTotal() { }

    /**
     * post: devuelve la cantidad total de productos.
     */
    public int contarProductos() { }

}
```

6. Implementar la clase CajaDeAhorro con la siguiente interfaz:

```java
class CajaDeAhorro {

    /**
     * post: la instancia queda asignada al titular indicado y con saldo igual a 0.
     */
    public CajaDeAhorro(String titularDeLaCuenta) { }
    
    /**
     * post: devuelve el nombre del titular de la Caja de Ahorro.
     */
    public String obtenerTitular() { }

    /**
     * post: devuelve el saldo de la Caja de Ahorro.
     */
    public double consultarSaldo() { }

    /**
     * pre : monto es un valor mayor a 0.
     * post: aumenta el saldo de la Caja de Ahorro según el monto depositado.  
     */
    public void depositar(double monto) { }
 
    /**
     * pre : monto es mayor a 0 y menor o igual que el saldo de la Caja de Ahorro.
     * post: disminuye el saldo de la Caja de Ahorro según el monto extraído.
     */
    public void extraer(double monto) { }
}
```

7. Implementar la clase Cerradura con los siguientes métodos. Indique axiomas de la clase, pre y post condiciones de los métodos. Cuando una Cerradura se bloquea no puede volver a abrirse nunca más.

```java
class Cerradura {

   public Cerradura(int claveDeApertura,int cantidadDeFallosConsecutivosQueLaBloquean)

    public boolean abrir(int clave)

    public void cerrar()

    public boolean estaAbierta()

    public boolean estaCerrada()

    public boolean fueBloqueada()

    public int contarAperturasExitosas()

    public int contarAperturasFallidas()

}
```

8. Implementar la clase ExpendedorDePasajes con los siguientes métodos. Indique axiomas de la clase, pre y post condiciones de los métodos.

```java
class ExpendedorDePasajes {

    public ExpendedorDePasajes(double precioPorKm)

    public double venderPasaje(double distanciaEnKm)

    public double venderPasajes(int cantidad, double distanciaEnKm)

    public int contarPasajesVendidos()

    public double obtenerDistanciaMaxima()

    public double calcularDistanciaPromedio()

    public double calcularVentaTotal()
}
```

9. Un Tragamonedas está compuesto por 3 Tambores. Cuando el Tragamonedas se activa, giran los 3 Tambores. Cada Tambor se detiene en una posición comprendida entre 1 y 8.  El Tragamonedas entrega un premio cada vez que, luego de ser activado los 3 Tambores se detienen en la misma posición. Implementar las clases Tragamonedas usando la clase Tambor:

```java
class Tambor {

    private int posicion;

    /**
     * post: inicialmente el Tambor está en la posición 1.
     */
    public Tambor() {

        posicion = 1;
    }

    /**
     * post: devuelve el número de posición en la que se encuentra el Tambor. Es un valor comprendido entre 1 y 8.
     */
    public int obtenerPosicion() { 

        return posicion;
    }

    /**
     * post: hace girar el tambor y luego se detiene en una posición comprendida entre 1 y 8.
     */
    public void girar() { 

        /* provee un número aleatorio en el rango [0.0, 1.0) */
        double aleatorio = Math.random();

        posicion = (int) (aleatorio * 8) + 1;
    }
}

class Tragamonedas {

    /**
     * post: los 3 Tambores del Tragamonedas están en la posición 1.
     */
    public Tragamonedas() { }

    /**
     * post: activa el Tragamonedas haciendo girar sus 3 Tambores.
     */
    public void activar() { }

    /**
     * post: indica si el Tragamonedas entrega un premio a partir de la posición de sus 3 Tambores.
     */
    public boolean entregaPremio() { }

/**
     * post: obtiene la posición del iésimo tambor del Tragamonedas
       pre:  i => 0; i < n (n = cantidad de tambores)
     */
    public int obtenerPosicionDelTambor(int i) { }
}
```

10. Defina una clase 'Monedero' que permita gestionar la cantidad de dinero de que una persona dispone en un momento dado. La clase deberá tener un constructor que permitirá crear un monedero con una cantidad de dinero inicial y deberá definir un método para meter dinero en el monedero, otro para sacarlo y finalmente, otro para consultar el disponible; solo podrá conocerse la cantidad de dinero del monedero a través de este último método. Por supuesto, no se podrá sacar más dinero del que haya en un momento dado en el monedero. Para probar el funcionamiento de la clase, escriba un método 'main' con una serie de instrucciones que hagan uso de los métodos definidos.

11. Se tiene un jugador de futbol definido por cantidad de goles y la cantidad de infracciones que hizo y cantidad de partidos en que jugó; además, se cuenta con un equipo de fútbol con 11 jugadores. De un campeonato con 10 equipos de fútbol se desea determinar cual es el equipo que hizo “juego sucio” y para cada equipo determinar “una figura”, para esto se deberá codificar los métodos:
    * esBuenjugador(): retorna true si hizo al menos 10 goles y cometió menos de 5 infracciones, retorna false en otro caso.
    * una Figura(): devuelve el número de jugador más goleador entre todos los “buenos jugadores” del equipo.
    * juegoSucio(): retorna true si todos los jugadores de un mismo equipo que hicieron algún gol y jugaron más de 2 partidos, cometieron alguna infracción, retorna false en otro caso.
    * Los datos para los 10 equipos del campeonato se generaran al azar y en un archivo de salida se guardaran los datos del campeonato.
    * Se deberán codificar las clases y métodos necesarios.

12. Escribir el código JAVA de una clase denominada ObraEdificio, con las siguientes características. Cada objeto de esta clase deberá tener información acerca de la superficie total a cimentar de una obra, y de la superficie que ya ha sido cimentada (en m^2, sin decimales). Existirán los siguientes métodos:
    * Constructor: en la creación se fijará el área total a cimentar para este edificio.
    * cimentando: recibirá un número indicando los metros de superficie que se están cimentando en ese momento. Si la suma de la superficie previamente cimentada más la que se supone que se está cimentando ahora, es mayor que la superficie total a cimentar, se escribirá un mensaje de error, y no se modificara nada. En caso contrario, se acumulara la cantidad de metros que se están cimentando con los que ya se habían cimentado antes.
    * restaPorCimentar: devolverá los metros que faltan por cimentar para alcanzar la superficie total.
    * terminado: devolverá verdadero si la superficie cimentada ya es igual a la superficie total a cimentar.

13. Definir una clase que represente a un número fraccionario. Una fracción está definida por un numerador y un denominador, ambos son números enteros. La clase deberá contener:
    * un constructor por defecto que inicialice la fracción en la fracción nula: 0/1
    * un constructor con dos parámetros: dos números enteros para inicializar el numerador y el denominador de la fracción. Se deberá tener en cuenta que el denominador debe ser no nulo.
    * Los métodos set y get respectivos.
    * El método toString()
    * El método ftor (): convierte una fracción a número real.
    * El método reducir(): simplifica la fracción hasta que queda irreducible.

14. Definir una clase que represente a un producto. El producto tendrá los siguientes atributos: código (int), descripcion (String), precio unitario (float), stock (int). La clase deberá contener:
    * un constructor por defecto.
    * un constructor con parámetros.
    * los métodos set y get respectivos.
    * el método toString().
