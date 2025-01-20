# > Proceso de software
Un ***proceso*** es un conjunto de actividades y resultados asociados que conducen a la generación de un producto.
Un ***proceso de software*** es, valga la redundancia, un conjunto de actividades y resultados asociados que conducen a la generación de un *producto de software*.

Diferentes tipos de software necesitan diferentes procesos de desarrollo.

No hay un único proceso de software, ni hay un proceso de software ideal.

Independientemente a esto, todas cuentas con sus cuatro actividades genéricas básicas:
                    - Especificación
                    - Construcción
                    - Verificación y validación
                    - Evolución
# > Especificación

Comprender y definir los servicios que brindará el software, las restricciones bajo las que operará y las características de calidad exigidas son parte de esta actividad.
Se lo conoce también *(y creo que se ve más en detalle en Ingeniera de software II)* como ***proceso de ingeniera de requisitos***.
Este no es un estudio de factibilidad.
En este se analizan los requisitos, para luego especificarlos y validarlos.
Esta luego se transforma en un producto ejecutable:
![[Pasted image 20241125201621.png]]
# > Construcción de software

Durante la construcción de software se:
                         - Diseña la arquitectura
                         - Diseña la interfaz
                         - Diseñan los componentes
                         - Diseña la estructura de datos
Durante la programación se escribirá el código fuente y se generará el código ejecutable/interpretable.
Este debe ser probado y los errores deberán ser depurados.
#  > Verificación y validación del software

Se comprueba que el software esté de acuerdo con las especificaciones y cumpla las expectativas de los clientes y usuarios.
Los programas se ejecutan con las correspondientes pruebas ya incluidas.
Las pruebas pueden ser:
                            - Pruebas de componentes: pruebas unitarias
                            - Pruebas del sistema: pruebas de integración
                            - Pruebas de aceptación: con datos reales y usuarios
# > Evolución del software

El proceso de de desarrollo y evolución no son procesos separados.
El software se va modificando continuamente aún antes no ponerlo en operación.
Muy poco software es un sistema completamente nuevo.
![[Pasted image 20241125202454.png]]

# > Actividades de gestión

Las actividades de gestión:
                             - Planificar y controlar el proyecto *(Costo - Tiempo - Recursos)*
                             - Administrar personal
                             - Administrar riesgos
                             - Administrar calidad
                             - Administrar la configuración del software
                             - Mejora del proceso de software

# > Modelos de proceso de software

Los modelos de proceso de software son ***representaciones abstractas de un proceso de software desde una perspectiva arquitectónica***.
Las características de estos son:
                             - No se describe en detalle cada actividad específica, sino el marco de trabajo del proceso
                             - Son modelos generales de desarrollo de software
                             - Se utilizan para explicar diferentes enfoques en el desarrollo de software
                             - También son llamados ***paradigmas de procesos***
Durante la cursada veremos 8, cada uno con sus ventanas y desventajas, en este apunte se explicarán con palabras propias, pero el archivo con todos estos explicados a detalle esta en el siguiente [recurso](http://campusvirtual.uno.edu.ar/moodle/pluginfile.php/168836/mod_resource/content/1/Notas%20de%20Clase%20-%20Introduccion%20Modelos%20de%20Proceso%20de%20Software%20-%202019v2.pdf).

# > Modelo de cascada

En este modelo cada actividad del proceso es una fase autónoma que produce una salida o documento aprobado.
La siguiente faso comienza cuando se ha finalizado con la anterior.
![[Pasted image 20241125203559.png]]
Las ventajas de este modelo son: 
                       - Buena visibilidad del proceso 
                       - Fácil de administrar
                       - Bien definidas las salidas a producir en cada fase para avanzar a la siguiente etapa
                       - Claro de entender por los clientes
                       - Separa análisis, diseño e implementación conduce a *sistemas robustos*.
Las desventajas son:
                      - Modelo inflexible: dificultades para hacer cambios entre etapas.
                      - Visión estática de los requisitos, ignora su *volatilidad natural*.
                      - Congelamiento prematuro de los requisitos:  puede implicar que el sistema no haga lo que los usuarios desean.
                      - No hay un compromiso de los clientes y usuarios a lo largo de todo el proceso de software.
                      - Presenta una visión de *manufactura de software*. No considera al proceso de software como un proceso de *resolución de problemas*. No trata los avances y retrocesos normales hasta crear el producto software.
                      - Errores y omisiones en los requisitos originales se descubren recién en las fases finales del ciclo.
    Su aplicación se da en:
                      - En contextos fácilmente comprendidos que permitan definir la totalidad de los requisitos en la etapa inicial.
                      - En procesos de desarrollo de software que son parte de proyectos grandes de ingeniería de sistemas.
                      - No aplicable en sistemas novedosos debido a problemas en las especificaciones y en el diseño.
                      - No aplicable a sistemas de software de alta complejidad, ya que cada etapa se realiza de manera independiente sin dividir el problema en partes.
# > Modelo de prototipos

Se construye y experimenta con una *imitación* del sistema de software, para comprender la funcionalidad requerida.
Se debe poder comprender inicialmente las necesidades de los clientes y usuarios para determinar objetivos y alcances del prototipo.
Aporta una comprensión unificada de lo que se necesita y de la solución que se propone. 
![[Pasted image 20241125205941.png]]Este a su vez tiene dos variantes:
                   - Prototipo evolutivo: este refina el prototipo hasta que se convierta en un sistema completo, el prototipo se considera como la especificación del sistema.
                   - Prototipo desechable o exploratorio: comienza con especificaciones poco entendidas, luego del prototipo se desecha, se sigue con un desarrollo convencional partiendo de los beneficios de este y por ultimo se genera un documento de especificación de requisitos basado en la comprensión obtenida al construir el prototipo. 
Sus ventanas, independientemente del caso a usar, son:
                  - Alta participación de clientes y usuarios.
                  - Reduce riesgos en el desarrollo debido a la mejora en la comprensión unificada entre desarrolladores y clientes.
                  - Provee a los usuarios de un modelo del sistema *(maqueta)* lo más temprano posible.
                  - Cumple con las necesidades inmediatas del cliente, pues se obtiene un desarrollo rápido *(prototipo evolutivo)*.
                  - La especificación de puede realizar en forma creciente.
                  - Reduce el costo total del desarrollo debido a que hay menos cambios por defectos en los requisitos durante el desarrollo con motivo del prototipo *(prototipo desechable)*.
Sus desventajas son:
                - Falta de visibilidad: difícil ver el avance del proceso. Hay poca documentación.
                - Los usuarios tienden a creer que el prototipo es *"ya"* la solución y se frustran por el retraso en la puesta en operación del software *(prototipo desechable)*
                - Requiere tecnología de avanzada (herramientas para producir el prototipo y para realizar un desarrollo rápido) y desarrolladores con habilidades en esas herramientas y técnicas.
                - Los sistemas tienden a una estructura deficiente por los cambios continuos sobre el prototipo *(prototipo evolutivo)*
                - La especificación del sistema es pobre, pues se construye sin una especificación inicial de requisitos.
                - Difícil establecer un nivel de calidad adecuado para un *prototipo evolutivo*.
Su aplicación es:
                -  Sistemas interactivos pequeños *(menos de 100.000 líneas de código)* o medianos *(hasta 500.000 líneas de código)*.
                - Sistemas de corta vida.
                - Partes de sistemas grandes.
                - Sistemas con especificaciones incompletas o incertidumbres en ellas.
                - Sistemas con especificaciones de alto riesgo.
                - Sistemas novedosos ya que las especificaciones y diseño se realizan paso a paso como parte del desarrollo del prototipo.