# SUMATIVA2_IDN
Repositorio para evaluación N°2 Inteligencia de negocios.


# DATOS HISTORICOS DE BITCOIN
**DATASET**  https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data  

## **Contexto del dataset** 
*Este dataset contiene información de la criptomoneda bitcoin, la información es desde el 01/01/2012 hasta mas o menos el 09/09/2025 (Aqui lo descargué, este dataset se actualiza a diario al parecer), entre las variables que podemos encontrar es la fecha en formato UNIX "Timestamp", valor de apertura "Open", el valor más alto "High", el valor mas bajo "Low", el valor de cierre "Close", Volumen transaccionado "Volume". Este dataset se maneja en ventanas de 1 segundo por lo que tiene la información completa, la idea es inicialmente transformarlo a dia para reducir la cantidad de valores a trabajar.*
## **Variables**
***Timestamp** - UNIX / segundos*  
***Open** - apertura*  
***High** - valor más alto*  
***Low** - valor más bajo*  
***Close** - valor de cierre*  
***Volume** - cantidad transaccionada*  

## **Objetivo** 
*El objetivo de este proyecto es analizar el comportamiento de la criptomoneda bitcoin en relación a su comportamiento con apertura, cierre, altos y bajos. El la medida de tiempo a utilizar es en dias, este dataset se actualiza a diario por lo que podría variar la información dependiendo de cuando se descargado del link superior.*  

## **Hipotesis a utilizar** 
*Las caídas en el precio mínimo (Low) tienen un efecto más fuerte sobre el precio de cierre que los incrementos en el precio máximo (High), lo que sugiere un sesgo bajista en la dinámica de mercado de Bitcoin.*

## **=================================================**  
## **Pasos para utilizar / Principalmente en VSC de ser posible**
**python -m venv venv**  
**.\venv\Scripts\Activate**  
**pip install -r requirements.txt**  
**Proceder a ver los notebooks - No olvidar subir el archivo "btcusd_1-min-data.csv" a 01_raw**


## **Dependencias**
**Se utilizo Python 3.13.9**  
**Manipulación de datos**  
*pandas>=2.0.0*  
*pyyaml>=6.0.0*  
  
**Archivos adicionales (Excel y Parquet)**  
*openpyxl>=3.1.0*  
*pyarrow>=15.0.0*  

**Entorno Notebook**  
*jupyter>=1.0.0*  
*notebook>=7.0.0*  
*ipykernel>=6.29.0*  

