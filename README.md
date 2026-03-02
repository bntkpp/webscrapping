# Web Scraper de Empleos - Get On Board 🚀

Este es un script en Python diseñado para automatizar la búsqueda de ofertas de empleo desde la plataforma [Get On Board](https://www.getonbrd.com/). 

## 📌 Características
- **Extracción de datos (Web Scraping):** Utiliza `requests` y `BeautifulSoup` para navegar y procesar el código HTML de la página web.
- **Procesamiento inteligente de fechas:** Analiza los textos de las fechas en formato bilingüe (ej: "feb 16" o "Jan 30") y los convierte a objetos de fecha reales en Python (`datetime`), detectando incluso cambios de año.
- **Filtro automático:** Filtra automáticamente los vacantes de trabajo, mostrando en consola **únicamente** aquellos cargos que fueron publicados en los **últimos 5 días**, para asegurar que siempre postules a ofertas frescas.
- **Area de Gusto:** Puedes cambiar el area que te gustaria obtener cambiando la url.

## 🛠️ Requisitos
Para poder ejecutar este proyecto, necesitas tener instalado Python 3.x y las siguientes librerías de terceros:

- `requests`
- `beautifulsoup4`
- `lxml` (como parser para BeautifulSoup)

Puedes instalarlas rápidamente usando `pip`:

```bash
pip install requests beautifulsoup4 lxml
```

## 🚀 Uso
1. Clona o descarga este repositorio en tu máquina local.
2. Abre tu terminal.
3. Navega hacia la carpeta del proyecto.
4. Ejecuta el archivo principal:

```bash
python web_scrapping.py
```

En la consola verás impreso algo similar a esto:
```text
[0 días atrás] - Ingeniero de Seguridad de la Información...
[2 días atrás] - Analista SOC Junior...
```

## 💡 Próximas posibles mejoras
- Ampliar el script para que no solo busque empleos de "Ciberseguridad", sino que acepte el área o etiqueta dinámica por consola.
- Extraer más datos relevantes (ej. modalidad remota, empresa, link del empleo) y exportarlos a un archivo `.csv` o `.xlsx`.
- Enviar notificaciones automáticas (ej. por Telegram o Email) cuando se encuentre un nuevo empleo disponible.
