import bs4 # Para parsear el HTML
import requests # Para hacer peticiones a la web
from datetime import date, timedelta, datetime

def convertir_fecha(fecha_str):
    # Diccionario para traducir los meses en texto (español/inglés) a números
    meses = {
        'ene': 1, 'jan': 1, 'feb': 2, 'mar': 3, 'abr': 4, 'apr': 4,
        'may': 5, 'jun': 6, 'jul': 7, 'ago': 8, 'aug': 8,
        'sep': 9, 'oct': 10, 'nov': 11, 'dic': 12, 'dec': 12
    }
    
    try:
        # fecha_str viene como "feb 16" o "Jan 30". Lo pasamos a minúsculas y separamos.
        partes = fecha_str.strip().lower().split()
        mes_txt = partes[0] # Recopilar el mes
        dia_num = int(partes[1]) # Recopilar el Dia
        
        mes_num = meses.get(mes_txt)
        
        # Creamos la fecha usando el año actual
        hoy = datetime.now()
        fecha_cargo = datetime(hoy.year, mes_num, dia_num)
        
        # Si la fecha calculada es mayor a hoy (ej: en enero vemos un cargo de "dic 20")
        # significa que es del año anterior
        if fecha_cargo > hoy:
            fecha_cargo = datetime(hoy.year - 1, mes_num, dia_num)
            
        return fecha_cargo
    except Exception as e:
        return None

url_base = "https://www.getonbrd.com/empleos-data-science"

# Cargos que fueron publcadas hace maximo 5 dias
mejores_cargos = []

# Crear Sopa
resultado = requests.get(url_base)
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# Seleccionar datos de los cargos
cargos = sopa.select('.gb-results-list__item') # Seleccionar todos los datos de los cargos
for cargo in cargos:

    # 1. Sacamos TODOS los elementos que tienen class 'opacity-half' que es la fecha
    elementos = cargo.select('.opacity-half.size0')
    
    # 2. Vamos a buscar en estos elementos cuál es realmente nuestra fecha
    fecha_valida = None
    for el in elementos:
        texto = el.get_text()
        # Tratamos de convertir todo lo que diga "opacity-half" a una fecha 
        resultado = convertir_fecha(texto)
        if resultado != None:
            fecha_valida = resultado
            break # Encontramos la fecha! salimos de este pequeño 'for'
            
    # Si logramos encontrar una fecha válida...        
    if fecha_valida != None:
        hoy = datetime.now()
        # Calculamos la diferencia en días.
        # En Python, restar fechas devuelve un objeto timedelta. De ahí sacamos los '.days'
        diferencia = (hoy - fecha_valida).days

        if diferencia <= 12:
            # Agarramos el titulo limpio usando select_one y get_text()
            titulo = cargo.select_one('.pr-3').get_text(strip=True)
            print(f"[{diferencia} días atrás] - {titulo}")


