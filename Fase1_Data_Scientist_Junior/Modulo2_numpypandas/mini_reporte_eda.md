# 📝 Mini-reporte EDA: Titanic Dataset

---

## 1. Resumen del dataset

- **Tamaño:** 1309 filas × 12 columnas.
- **Variables principales:** `PassengerId`, `Survived`, `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Ticket`, `Fare`, `Cabin`, `Embarked`, `Name`.
- **Contexto:**  
  Este dataset contiene información demográfica y de viaje de los pasajeros y tripulación del Titanic, incluyendo si sobrevivieron, la clase del boleto, edad, sexo y tarifa pagada. Es un clásico en la ciencia de datos y se usa para practicar análisis y machine learning.

---

## 2. Principales hallazgos

- **Valores nulos:**  
  - `Age`: 263 valores nulos (~20%)
  - `Cabin`: 1014 valores nulos (~77%)
  - `Embarked`: 2 valores nulos
  - `Fare`: 1 valor nulo

- **Distribución por género:**

  | Género    | Cantidad |
  |-----------|----------|
  | Masculino | 843      |
  | Femenino  | 466      |

- **Distribución de sobrevivientes:**  
  (Completa con el dato exacto de tu análisis si quieres, por ejemplo:)
  - Sobrevivieron: 500 (38%)
  - No sobrevivieron: 809 (62%)

- **Distribución por clase:**  
  - Primera clase: xxx pasajeros  
  - Segunda clase: xxx pasajeros  
  - Tercera clase: xxx pasajeros  

- **Correlación entre clase y supervivencia:**  
  El coeficiente de correlación entre `Pclass` y `Survived` es **-0.26**, lo que indica que los pasajeros de clases más altas tenían más probabilidades de sobrevivir, aunque la relación es débil.

- **Notas adicionales:**  
  No se detectaron valores atípicos evidentes, aunque destaca la gran cantidad de adultos de mediana edad en el barco. Sería útil realizar boxplots para investigar outliers en edad y tarifa.

---

## 3. Visualizaciones clave

#### a) Cantidad de pasajeros por clase
>
> El gráfico muestra que la mayoría de los pasajeros viajaba en tercera clase.

![Gráfico de barras de pasajeros por clase](Fase1_Data_Scientist_Junior/Modulo2_numpypandas/Pasajerosxclase.png)

#### b) Distribución de edades
>
> La distribución de edades presenta un pico en adultos jóvenes, pero hay presencia de niños y personas mayores.

![Histograma de edades](Fase1_Data_Scientist_Junior/Modulo2_numpypandas/grafico_edades.png)

(Opcional: puedes agregar un boxplot de edad por supervivencia si quieres profundizar.)

---

## 4. Conclusiones

- El dataset es variado, pero tiene valores nulos significativos en variables como **Age** y **Cabin**, lo que puede afectar el análisis y modelado.
- Predomina el sexo masculino y la mayoría de pasajeros viajaba en tercera clase.
- La correlación entre clase y supervivencia es negativa pero débil; se observa una tendencia, pero no es concluyente.
- Para análisis futuros, sería recomendable imputar los valores nulos en edad y tarifa, y explorar la relación entre tarifa pagada y supervivencia.
- El análisis visual ayuda a detectar patrones y posibles desbalances, y motiva preguntas para explorar en etapas posteriores (como la influencia de la edad, género o clase en la supervivencia).

---

*Autor: Diego González | EDA realizado como parte del curso de Data Science y Machine Learning (Fase 1)*
