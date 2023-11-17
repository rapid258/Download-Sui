
![](https://img.shields.io/github/forks/marioggil/DownloadSui.svg?style=plastic)
![](https://img.shields.io/github/issues/marioggil/DownloadSui.svg?style=plastic)
![](https://img.shields.io/github/stars/marioggil/DownloadSui.svg?style=plastic)


# Proyecto Sui.

This is a script to download the electricity part of the "Single Public Services Information System, administered by the Superintendence of Home Public Services", This system integrates the financial, administrative and operational part of the services in Colombia [**here**](http://www.sui.gov.co)


# Fases e hitos

La primera fase es un sistema que descargue el "Consolidado Energía por Empresa Departamento y Municipio", con precios, consumo y suscriptores   [**here**](http://reportes.sui.gov.co/fabricaReportes/frameSet.jsp?idreporte=ele_com_096).

Otras bases de datos objetivo son [**Datos PQR**](http://reportes.sui.gov.co/fabricaReportes/frameSet.jsp?idreporte=ele_com_090), [**Estado de Resultados**](http://reportes.sui.gov.co/fabricaReportes/frameSet.jsp?idreporte=ele_fin_054).


# Analisis

## Consolidado Energía por Empresa Departamento y Municipio", con precios, consumo y suscriptores

Age: Year of the data
Site: Type of location with three possible options Urban Center, Rural, Urban
Department: Department of the location.
Municipality: Municipality of the location.
Company: Service provider company (It should be Distribution but it is good to confirm it)
### Usage data.
There are 10 categories of users:
 - Estrato 1.  
 - Estrato 2.  
 - Estrato 3.  
 - Estrato 4.  
 - Estrato 5.  
 - Estrato 6.  
 - Industrial.  
 - Comercial.  
 - Oficial.  
 - Otros.  
Y Cada Cateroria de Usuario tiene 3 variables provenientes de la base de datos:   
- Suscriptores (Usuarios del servicio)  
- Consumo(Cantidad de Kw consumidos) y Valor Consumo (Dinero que llego a la compañia por ese consumo).  
Ademas hay 3 categorias Calculadas:   
- Consumo por Suscriptor (Cuanto es el consumo promedio por los usuarios declarados).  
- Valor por suscriptor (Cuanto paga en promedio cada suscriptor).  
- Precio por Vatio (Cuanto es el precio por Kv en ese periodo.).

## Descargas.

## Preanalisis y limpieza de datos.

