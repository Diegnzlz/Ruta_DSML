# 📊 Módulo 6: Bases de Datos - Mini Proyecto

## 🎯 Objetivo

El objetivo de este mini proyecto fue **conectar con una API externa, almacenar los datos en una base de datos SQLite y realizar consultas básicas** para aplicar lo aprendido sobre gestión de bases de datos en Python.

## 🌎 API utilizada

Para este proyecto se utilizó la API gratuita de **RestCountries**:

🔗 [https://restcountries.com/](https://restcountries.com/)

Esta API proporciona información sobre países de todo el mundo, incluyendo:

- Nombre oficial y común
- Capital
- Región y subregión
- Población
- Idiomas
- Moneda

## 🛠️ Proceso realizado

1. **Conexión a la API**
   - Se usó la librería `requests` para obtener los datos de los países.
   - La API devuelve los resultados en formato JSON.

2. **Creación de la Base de Datos**
   - Se creó una base de datos local en SQLite (`paises.db`).
   - La tabla `paises` incluye los siguientes campos:
     - `id` (clave primaria, autoincremental)
     - `nombre`
     - `capital`
     - `region`
     - `subregion`
     - `poblacion`
     - `idiomas`
     - `moneda`

3. **Inserción de datos**
   - Los datos de cada país fueron transformados y almacenados en la base de datos.

4. **Consultas realizadas**
   - Número total de países registrados.
   - Listado de países de la región **Americas**.
   - Los 5 países más poblados.
   - Países cuya capital empieza con la letra **S**.

## 📌 Resultados de las consultas

### ✔ Número total de países

`250 países registrados en la base de datos`

### ✔ Países en la región *Americas*

Ejemplo de algunos:

- Argentina
- Brazil
- Chile
- United States
- Mexico

### ✔ Los 5 países más poblados

1. China
2. India
3. United States
4. Indonesia
5. Pakistan

### ✔ Países con capital que inicia con **S**

- Santiago (Chile)
- San José (Costa Rica)
- Stockholm (Suecia)
- Seoul (Corea del Sur)
- Suva (Fiyi)

## 📂 Archivos generados

- `miniproyecto.py` → Script principal que conecta con la API y maneja la base de datos.  
- `paises.db` → Base de datos SQLite con la información de los países.  
- `miniproyecto.md` → Este reporte.  

## 🚀 Conclusión

Este mini proyecto permitió poner en práctica el uso de **APIs, manejo de JSON, bases de datos con SQLite y consultas SQL**, integrando varios conceptos de análisis y organización de datos.  

Además, sienta las bases para trabajar con datasets más complejos en proyectos de análisis exploratorio (EDA) y modelado de datos.
