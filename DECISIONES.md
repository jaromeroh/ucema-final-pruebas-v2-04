# Proceso documentado

Construcción docente en una sesión; no se atribuyen despliegues ni revisiones humanas inexistentes.

## Decisión 1: disponibilidad calculada, no inventada
La herramienta calcula intersecciones y el modelo debe conservarlas. Sin disponibilidad común, se devuelve una lista vacía y se solicita cambiar restricciones.

## Decisión 2: límites temporales explícitos
Una reunión que termina cuando otra empieza no se solapa. tests/test_tools.py comprueba ese borde, la ausencia de opciones y el ajuste de una reunión de 60 minutos dentro de la ventana.

## Decisión 3: recortar integraciones
Se usaron archivos locales en UTC para que terceros puedan reconstruir los cálculos. Se dejó fuera la escritura en calendarios y el manejo de preferencias o husos no indicados.

## Evidencia y limitaciones de la historia
Las pruebas guardadas muestran verificaciones realizadas sobre los archivos incluidos. El historial Git permite ubicar implementación y documentación. No se conserva una conversación completa con la IA ni una validación de campo empresarial. Las corridas preservan las instrucciones efectivamente enviadas al modelo; esas sí pueden auditarse literalmente.
