#!/usr/bin/env python
# coding: utf-8

# # Librerias y Configuraciones

# In[1]:


import glob
from bs4 import BeautifulSoup
import os
import time
import datetime
from selenium import webdriver# I need to web scrap in chrome
from selenium.webdriver.support.select import Select # I need to select menu options
from random import randint
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 100)


# # Funciones

# In[2]:


def TransNum(Texto):
    Salida=Texto.replace(",","")
    return Salida
def leerarchivo(lugar):
    archi=open(lugar)
    temp='we'
    cuadros=""
    while temp != '':#lee todo
        temp=archi.readline()
        cuadros=cuadros+temp
    archi.close()
    return cuadros
def leerColumna(archivo,Sufijo):
    b=leerarchivo(archivo)
    soup=BeautifulSoup(b)
    Columns = []
    temp=[]
    table = soup.find_all('table')
    table_body = table[2].find('thead')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        Columns= ['Age', 'Month', 'Site']+[ele for ele in cols if ele]
        for k in range(7,len(Columns)):
            Columns[k]=Columns[k]+Sufijo
    return(Columns)
def leerData(archivo,Columns,patron):
        temp2=archivo.replace("./Data/","").replace(".html","").split("_")
        b=leerarchivo(archivo)
        soup=BeautifulSoup(b)
        data = []
        temp=[]
        table = soup.find_all('table')
        #print(table[2])
        table_body = table[2].find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            temp=[ele for ele in cols if ele]

            if 'ND' in set(temp[4:]) and len(set(temp[4:]))>1:
                data.append(temp2[:3]+temp)
        df = pd.DataFrame.from_records(data, columns=Columns)
        for ii in Columns[7:]:
            df[ii]=df[ii].apply(TransNum)
            df[ii]=pd.to_numeric(df[ii], errors='coerce')
        #df.info()
        df=df.drop(columns=['Variable Calculada', 'Total Residencial%s'%(patron),'Total No Residencial%s'%(patron)])
        return(df)
def SetPruebas(Data):
    Data.info()
    Data["Empresa"].value_counts()
def color_negative_red(val):
    if val < 0:
        color = 'red'
    else:
        color ='black'

    return 'color: %s' % color

def color_significant(val):
    if abs(val) > 0.3:
        color = 'yellow'
    else:
        color = 'white'
    return  'background-color: %s' % color
def initSelenium():
    sistemaop = os.name
    if sistemaop=="posix":
        driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
    else:
        driver = webdriver.Chrome('./chromedriver.exe')  # Optional argument, if not specified will search path.


# # Descarga de datos

# In[6]:


url="http://reportes.sui.gov.co/fabricaReportes/frameSet.jsp?idreporte=ele_com_096"
#initSelenium()
sistemaop = os.name
if sistemaop=="posix":
    driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
else:
    driver = webdriver.Chrome('./chromedriver.exe')  # Optional argument, if not specified will search path.

for i in [16]:#range(8,17):#Counter Age
    time_delay = 30
    print(30)
    driver.get(url)#Goto web
    print("inicio")
    #time.sleep(time_delay)
    print("fin")
    dheader=driver.find_element_by_xpath("//*[@id='header']")#Search Head
    driver.switch_to.frame(dheader)#Manipulate Head
    inputElementi = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/select/option[%s]"%(str(i+1)))
    age=inputElementi.text
    for ii in range(3):
        inputElementii = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td/table/tbody/tr[3]/td[2]/select/option[%s]"%(str(ii+1)))
        site=inputElementii.text
        for iii in [1,2,3]:
            inputElementiii = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td/table/tbody/tr[7]/td[2]/select/option[%s]"%(str(iii)))
            data=inputElementiii.text
            for iiii in range(12):
                try:
                    inputElementiiii = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/select/option[%s]"%(str(iiii+1)))
                    month=inputElementiiii.text
                    TEMP=age+"_"+month+"_"+site+"_"+data
                except:
                    continue
                try:
                    if os.path.exists("./ele_com_096/Data/"+TEMP+".html"):
                        print("Existe ./ele_com_096/Data/"+TEMP+".html")
                        time.sleep(1)
                        continue
                    nomonths=["Anual",'Trimestre 1','Trimestre 2','Trimestre 3','Trimestre 4','Semestre 1','Semestre 2']
                    if month in nomonths:
                        continue
                    driver.get(url)
                    dheader=driver.find_element_by_xpath("//*[@id='header']")
                    driver.switch_to.frame(dheader)
                    inputElementi = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/select/option[%s]"%(str(i+1)))
                    inputElementi.click()
                    inputElementii = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td/table/tbody/tr[3]/td[2]/select/option[%s]"%(str(ii+1)))
                    inputElementii.click()
                    inputElementiii = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td/table/tbody/tr[7]/td[2]/select/option[%s]"%(str(iii)))
                    inputElementiii.click()
                    inputElementiiii = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/select/option[%s]"%(str(iiii+1)))
                    inputElementiiii.click()
                    inputElement = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td[2]/table/tbody/tr/td/input[2]")
                    time.sleep(time_delay+5)
                    inputElement.click()
                    time.sleep(time_delay)
                    driver.switch_to.default_content()
                    dreport=driver.find_element_by_xpath("//*[@id='report']")
                    driver.switch_to.frame(dreport)
                    html = driver.page_source
                    file2 = open("./ele_com_096/Data/"+TEMP+".html","w+")
                    file2.write(html)
                    file2.close()
                    driver.switch_to.default_content()
                    dheader=driver.find_element_by_xpath("//*[@id='header']")
                    driver.switch_to.frame(dheader)
                except:
                    print(TEMP)


# # Stadistics DataBase

# In[25]:


a=glob.glob("./Data/*.html")
len(a)
iii=[]
SetData=glob.glob("./Data/*_Suscriptores.html")#["./Data/2009_Enero_Rural_Suscriptores.html","./Data/2013_Enero_Rural_Suscriptores.html"]
cont3=len(SetData)
Total=cont3
for i in a:
    ii=i.replace("./Data/","").replace(".html","").split("_")
    iii=iii+ii
iii=set(iii)
for i in iii:
    a=len(glob.glob("./Data/*%s*.html"%(i)))
    print( "La etiqueta %s posee %s sets"%(i,a))
SetData=glob.glob("./Data/*_Suscriptores.html")
TypeData=["_Suscriptores","_Consumo","_Valor Consumo"]
for i1 in SetData:
    cont3=cont3-1
    for i2 in TypeData:
        i3=i1.replace("_Suscriptores",i2)
        if not os.path.isfile(i3):
            print(i3)


# # Carga de base de datos en Memoria

# In[ ]:


SetData=glob.glob("./Data/*_Suscriptores.html")#["./Data/2009_Enero_Rural_Suscriptores.html","./Data/2013_Enero_Rural_Suscriptores.html"]
cont3=len(SetData)
Total=cont3
TiempoFin=0
TypeData=["_Suscriptores","_Consumo","_Valor Consumo"]
cont2=0
TiempoInit=datetime.datetime.now()
for i1 in SetData:

    cont3=cont3-1
    cont=0
    for i2 in TypeData:
        i3=i1.replace("_Suscriptores",i2)
        Temp1=leerColumna(i3,i2)
        Tabla=leerData(i3,Temp1,i2)
        if cont==0:
            FinalT=Tabla
            cont=cont+1
        else:
            FinalT=FinalT.merge(Tabla,on=['Age', 'Month', 'Site', 'Departamento', 'Municipio', 'Empresa'], suffixes=("ty", "fg"))
            cont=cont+1
    if cont2==0:
        FinalM=FinalT
        cont2=cont2+1

    else:
        FinalM=pd.concat([FinalM, FinalT])
        cont2=cont2+1
    TiempoFin=datetime.datetime.now()
    if cont3 %25==0:
        Estimador=(TiempoFin-TiempoInit)*cont3/(Total-cont3)
        TiemporPorData=(TiempoFin-TiempoInit)/(Total-cont3)
        print(Estimador,cont3, datetime.datetime.now()+ Estimador)


# In[4]:


FinalM = pd.read_csv(
    "./DataSui.csv",      # relative python path to subdirectory
    sep=',',           # Tab-separated value file.
    #quotechar="'",        # single quote allowed as quote character
    #dtype={"salary": int},             # Parse the salary column as an integer
    #usecols=['name', 'birth_date', 'salary'].   # Only load the three columns specified.
    #parse_dates=['birth_date'],     # Intepret the birth_date column as a date
    #skiprows=10,         # Skip the first 10 rows of the file
    na_values=''      # Take any '.' or '??' values as NA
)


# # Pruebas en base de datos

# In[5]:


FinalM.info()


# In[13]:


FinalM["Empresa"].value_counts()


# In[14]:


FinalM["Departamento"].value_counts()


# In[15]:


FinalM["Municipio"].value_counts()


# In[16]:


FinalM["Site"].value_counts()


# In[17]:


FinalM["Month"].value_counts()


# In[10]:


FinalM["Age"].value_counts()


# In[11]:


FinalM.describe()


# In[12]:


import matplotlib.pyplot as plt
FinalM.hist(bins=100, figsize=(90,90))
plt.savefig ('grafico01.png')


# In[21]:


FinalM.corr(method="kendall" ).style.applymap(color_negative_red).applymap(color_significant)


# # Exportar Base de datos

# In[18]:


FinalM.to_csv('DataSui2.csv')


# # Calculos Adicionales

# In[9]:


for i in FinalM.columns[6:16]:
    ConsumoMedio=i.replace("_Suscriptores","_ConsumoMedio")
    FacturaMedia=i.replace("_Suscriptores","_FacturaMedia")
    TarifaMedia=i.replace("_Suscriptores","_TarifaMedia")
    Consumo=i.replace("_Suscriptores","_Consumo")
    ValorConsumo=i.replace("_Suscriptores","_ValorConsumo")
    FinalM[ConsumoMedio]=FinalM[Consumo]/V[i]
    FinalM[FacturaMedia]=FinalM[ValorConsumo]/V[i]
    FinalM[TarifaMedia]=FinalM[ValorConsumo]/(V[Consumo])


# # Verificacion por Fila

# In[22]:


len(FinalM)#.columns[6:16]
jkl=FinalM.iloc[5]
jkl


# # Analisis por municipio

# In[17]:


V=FinalM#[FinalM["Municipio"]=="GUACARI"]
table = pd.pivot_table(V, index=['Age', 'Month', 'Site', 'Departamento', 'Municipio', 'Empresa'], values=['Estrato 1_Suscriptores', 'Estrato 2_Suscriptores',
       'Estrato 3_Suscriptores', 'Estrato 4_Suscriptores',
       'Estrato 5_Suscriptores', 'Estrato 6_Suscriptores',
       'Industrial_Suscriptores', 'Comercial_Suscriptores',
       'Oficial_Suscriptores', 'Otros_Suscriptores', 'Estrato 1_Consumo',
       'Estrato 2_Consumo', 'Estrato 3_Consumo', 'Estrato 4_Consumo',
       'Estrato 5_Consumo', 'Estrato 6_Consumo', 'Industrial_Consumo',
       'Comercial_Consumo', 'Oficial_Consumo', 'Otros_Consumo',
       'Estrato 1_Valor Consumo', 'Estrato 2_Valor Consumo',
       'Estrato 3_Valor Consumo', 'Estrato 4_Valor Consumo',
       'Estrato 5_Valor Consumo', 'Estrato 6_Valor Consumo',
       'Industrial_Valor Consumo', 'Comercial_Valor Consumo',
       'Oficial_Valor Consumo', 'Otros_Valor Consumo'],aggfunc=np.sum)
table2 = pd.pivot_table(V, index=['Age','Departamento', 'Municipio'], values=[ 'Comercial_Suscriptores',
       'Comercial_Consumo', 'Comercial_Valor Consumo'],aggfunc=np.sum)


# In[37]:


table2


# In[36]:


table2["TarifaMedia"]=table2['Comercial_Valor Consumo']/(table2['Comercial_Consumo'])


# In[38]:


table2.to_csv('Tarifas.csv')


# In[ ]:
