
![](https://img.shields.io/github/forks/marioggil/DownloadSui.svg?style=plastic)
![](https://img.shields.io/github/issues/marioggil/DownloadSui.svg?style=plastic)
![](https://img.shields.io/github/stars/marioggil/DownloadSui.svg?style=plastic)


# Proyecto Sui.

Esto es un script para descargar la parte de eelectricidad del "Sistema Único de Información de Servicios Públicos, administrado por la Superintendencia de Servicios Públicos Domiciliarios", Este sistema integra la parte financiera, adminsitrativa y operativa de los servicios en colombia [**here**](http://www.sui.gov.co)


# Fases e hitos.

La primera fase es un sistema que descargue el "Consolidado Energía por Empresa Departamento y Municipio", con precios, consumo y suscriptores   [**here**](http://reportes.sui.gov.co/fabricaReportes/frameSet.jsp?idreporte=ele_com_096).

Otras bases de datos objetivo son [**Datos PQR**](http://reportes.sui.gov.co/fabricaReportes/frameSet.jsp?idreporte=ele_com_090), [**Estado de Resultados**](http://reportes.sui.gov.co/fabricaReportes/frameSet.jsp?idreporte=ele_fin_054).


# Analisis.

## Consolidado Energía por Empresa Departamento y Municipio", con precios, consumo y suscriptores

Age: Año del dato  
Site: Tipo de ubicacion con tres opciones posibles Centro Urbano, Rural, Urbano  
Departamento: Departamento de la ubicacion.  
Municipio: Municipio de la ubicacion.  
Empresa: Empresa Prestadora de servicio (Deberia ser Distribucion pero es bueno confirmalo)  
### Datos de uso.
Hay 10 categorias de usuarios:
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

