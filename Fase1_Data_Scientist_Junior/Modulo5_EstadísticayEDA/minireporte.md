### 📝 Insights Clave del EDA

1. **HouseAge**:  
   - La mayoría de las viviendas tienen entre 10 y 40 años (`mediana = 29`).  
   - Distribución uniforme, sin outliers extremos.

2. **AveRooms**:  
   - Promedio de habitaciones: ~5 (con outliers > 20, posible error de datos).  
   - Sesgo positivo: pocas viviendas con muchas habitaciones.

3. **Correlaciones**:  
   - `MedInc` y `MedHouseVal` muestran correlación fuerte (+0.68).  
   - `AveRooms` y `AveBedrooms` están altamente correlacionadas (+0.85).  

**Insights Esperados**:
Outliers:
AveRooms tiene valores extremos (>15 habitaciones), probablemente errores o mansiones.
Population muestra distritos con población anormalmente alta.
Asimetrías:
AveOccup (ocupación promedio) está sesgada a la derecha → Muchos distritos con baja ocupación.
Correlaciones:
MedHouseVal también se correlaciona con HouseAge (-0.3): viviendas más antiguas tienden a valer menos.
