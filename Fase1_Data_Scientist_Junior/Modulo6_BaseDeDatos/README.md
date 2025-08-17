# 📊 Informe de Análisis – Miniproyecto Base de Datos (California)

## 📌 Introducción

Este proyecto forma parte de la **Fase 1 – Data Scientist Junior**, en el **Módulo 6: Base de Datos**.  
El objetivo principal es **conectar, almacenar y analizar datos en SQLite**, utilizando como fuente de información datos relacionados con **California**.

La práctica consiste en:

1. Consumir una API pública.
2. Guardar los datos en una base de datos SQLite.
3. Realizar consultas SQL para responder preguntas analíticas.

---

## 🔗 Fuente de datos

Utilizamos la API pública de **[REST Countries](https://restcountries.com/)** para obtener información global.  
Se enfocó en:  

- Nombre común y oficial  
- Capital  
- Región y subregión  
- Población  
- Idiomas  
- Moneda oficial  

---

## 🗄️ Base de Datos

Se creó una base llamada `california.db` con una tabla `california`:

```sql
CREATE TABLE california (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT,
  region TEXT,
  subregion TEXT,
  capital TEXT,
  poblacion INTEGER,
  moneda TEXT,
  idioma TEXT
);
```

## 🔍 Consultas Realizadas

1️⃣ Total de población registrada

```sql
SELECT SUM(poblacion) AS total_poblacion FROM california;
```

2️⃣ Idiomas hablados en California

```sql
SELECT idioma, COUNT(*) AS cantidad FROM california GROUP BY idioma;
```

3️⃣ Moneda oficial

```sql
SELECT DISTINCT moneda FROM california;
```

4️⃣ Información general del registro

```sql
SELECT nombre, capital, region, subregion FROM california;
```

---

## 📈 Resultados Principales

- Población: se obtiene el número registrado de habitantes.
- Idioma predominante: inglés (con posibles variantes locales).
- Moneda oficial: dólar estadounidense (USD).
- Región geográfica: América del Norte → Norteamérica.

---

## 📚 Conclusiones

- El uso de SQLite permite estructurar la información de una API en una base de datos ligera y manejable.
- A partir de los datos almacenados, se pueden realizar consultas analíticas rápidas.
- Este enfoque es una primera aproximación a proyectos de ETL (Extract, Transform, Load), que escalarán en fases futuras del roadmap.

---

## ⚙️ Tecnologías Utilizadas

- **Python**: Para consumir la API y manipular los datos.
- **SQLite**: Base de datos ligera para almacenamiento local.
- **Requests**: Librería para realizar peticiones HTTP a la API.
- **Pandas**: Para manipulación y análisis de datos (opcional, si se requiere).

---

Autor✍️ Autor: Diego González
📅 Proyecto desarrollado en el módulo 6 – Base de Datos
