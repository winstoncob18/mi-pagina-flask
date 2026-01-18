from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# ================= REGISTRO =================
def guardar_visita(ip, fecha):
    with open("visitas.txt", "a", encoding="utf-8") as f:
        f.write(f"{ip} | {fecha}\n")

def leer_visitas():
    try:
        with open("visitas.txt", "r", encoding="utf-8") as f:
            return f.readlines()
    except:
        return []

# ================= BIENVENIDA =================
@app.route("/")
def inicio():
    ip = request.remote_addr
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    guardar_visita(ip, fecha)

    return """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Bienvenida</title>
<style>
body{
    margin:0;
    height:100vh;
    background:white;
    font-family:Arial;
    display:flex;
    justify-content:center;
    align-items:center;
    text-align:center;
}
.box{max-width:650px}
.book{font-size:100px;margin-bottom:20px}
button{
    padding:15px 40px;
    font-size:20px;
    background:#00c853;
    color:white;
    border:none;
    border-radius:10px;
    cursor:pointer;
}
footer{
    position:fixed;
    bottom:10px;
    width:100%;
    color:#555;
}
</style>
</head>
<body>
<div class="box">
<div class="book">📚</div>
<h1>Bienvenido a mi página de artículos científicos</h1>
<p>Producción académica con acceso directo a DOI</p>
<button onclick="location.href='/articulos'">Comenzar</button>
</div>
<footer>Página web creada por Graciela Celedonia Sosa Bueno</footer>
</body>
</html>
"""

# ================= ARTÍCULOS =================
@app.route("/articulos")
def articulos():
    articulos = [
        {
            "titulo": "Análisis del estrés crónico y la carga mental para reducir el impacto de los riesgos silenciosos",
            "revista": "Arandu UTIC",
            "anio": "2025-07-31 | Journal article",
            "contributors": "Graciela Celedonia Sosa Bueno; Evelin Anabel Beltrán Borbor; Luis Miguel Asencio Suarez; Jessenia Maritza Aguilera Suárez",
            "doi": "https://doi.org/10.69639/arandu.v12i2.1257"
        },
        {
            "titulo": "Control de la Moniliasis en la Producción de Cacao con Trichoderma Spp",
            "revista": "Revista Veritas de Difusão Científica",
            "anio": "2025-07-18 | Journal article",
            "contributors": "Graciela Celedonia Sosa Bueno; Gómez Segarra Roberto Alejandro; Parra Menoscal Jefferson David; Rodriguez Suarez Giovanna Gabriela",
            "doi": "https://doi.org/10.61616/rvdc.v6i2.700"
        },
        {
            "titulo": "Diseño de Horno de Fundición de Metales con Análisis de Materiales, Funcionalidad y Normativa",
            "revista": "Revista Veritas de Difusão Científica",
            "anio": "2025-07-18 | Journal article",
            "contributors": "Dra. Graciela Celedonia Sosa Bueno; Paúl Eitel Rodríguez Moriel",
            "doi": "https://doi.org/10.61616/rvdc.v6i2.701"
        },
        {
            "titulo": "Estrés Laboral y su Relación con la Satisfacción Laboral",
            "revista": "Revista Veritas de Difusão Científica",
            "anio": "2025-07-18 | Journal article",
            "contributors": "Dra. Graciela Celedonia Sosa Bueno; Jiménez González Octavio Alfonso; Geraldine Romina Terranova Malavé; Íngrid Estefanía Suárez Asencio",
            "doi": "https://doi.org/10.61616/rvdc.v6i2.699"
        },
        {
            "titulo": "Evaluación del Desempeño de los Sistemas de Drenaje Urbano Sostenible Para Mitigar Inundaciones",
            "revista": "Revista Veritas de Difusão Científica",
            "anio": "2025-07-18 | Journal article",
            "contributors": "Graciela Celedonia Sosa Bueno; Jhon Alex González Tómala",
            "doi": "https://doi.org/10.61616/rvdc.v6i2.698"
        },
        {
            "titulo": "Manejo de Imágenes Satelitales Obtenidas del Sensor Remoto MODIS de la NASA, Ejecutado en Estudios de la Ingeniería Civil",
            "revista": "Revista Veritas de Difusão Científica",
            "anio": "2025-07-18 | Journal article",
            "contributors": "Dra. Graciela Celedonia Sosa Bueno; Daniel Alexander Muñiz Villegas; Castro Solórzano Kenneth Ariel; Juan Carlos Reyes Naranjo; Villon Zambrano Endy Yerovi",
            "doi": "https://doi.org/10.61616/rvdc.v6i2.700"
        },
        {
            "titulo": "Análisis de innovaciones en la síntesis química de plásticos biodegradables",
            "revista": "Revista Veritas de Difusão Científica",
            "anio": "2025-06-30 | Journal article",
            "contributors": "Maritza E. Morales Mejillón; Israel M. Guachamin Adun; Danna N. García Maldonado; María L. Morales Mejillón; Graciela Celedonia Sosa Bueno",
            "doi": "https://doi.org/10.61616/rvdc.v6i2.655"
        },
        {
            "titulo": "Auditoría de Calidad Para El Mejoramiento Del Proceso Productivo En Plantas Compactas",
            "revista": "Arandu UTIC",
            "anio": "2025-01-14 | Journal article",
            "contributors": "Dayanna Dennys Veliz Caicedo; Johnny Alonso Morán Quimí; Jonathan Daniel Santos Carvajal; William Joel Perero Reyes; Graciela Celedonia Sosa Bueno",
            "doi": "https://doi.org/10.69639/arandu.v11i2.502"
        },
        {
            "titulo": "Manufactura esbelta para la mejora del proceso operacional",
            "revista": "Arandu UTIC",
            "anio": "2025-01-14 | Journal article",
            "contributors": "Jacinto Daniel Espinales Meza; Bryan Patricio Salvatierra Rogel; Ángel José Vera Rodríguez; Karen Antonella Tigrero González; Graciela Celedonia Sosa Bueno",
            "doi": "https://doi.org/10.69639/arandu.v11i2.497"
        },
        {
            "titulo": "Efecto de la aplicación de talleres BPM en la producción de yogurt",
            "revista": "Ciencia Latina Revista Científica Multidisciplinar",
            "anio": "2024-07-16 | Journal article",
            "contributors": "Graciela Celedonia Sosa Bueno; José Daniel Guerra",
            "doi": "https://doi.org/10.37811/cl_rcm.v8i3.12016"
        },
        {
            "titulo": "Tendencias en el uso de la mecánica de materiales",
            "revista": "Polo del Conocimiento",
            "anio": "2024-07-01 | Journal article",
            "contributors": "Graciela Celedonia Sosa Bueno",
            "doi": "https://doi.org/10.23857/pc.v9i7.7571"
        },
        {
            "titulo": "Impacto en la Educación en Procesamiento de Alimentos: Deshidratación de Frutas como Proyecto STEM",
            "revista": "Revista Veritas de Difusão Científica",
            "anio": "2024-06-13 | Journal article",
            "contributors": "Graciela Celedonia Sosa Bueno; José Daniel Guerra Viteri; Mishelle Abigail Solórzano Sosa",
            "doi": "https://doi.org/10.61616/rvdc.v5i2.84"
        },
        {
            "titulo": "Métodos de enseñanza del razonamiento lógico matemático para estudiantes universitarios",
            "revista": "RECIMUNDO:Revista Científica de la Investigación y el Conocimiento",
            "anio": "2024 | Journal article",
            "contributors": " Graciela C. Sosa Bueno, Carlos Alfredo Banguera Díaz, Fulton Leopoldo López Bermúdez, María Alejandra Borbor Bajaña",
            "doi": "https://dialnet.unirioja.es/servlet/articulo?codigo=10293590"
        },
        {
            "titulo": "Mejoramiento del pensamiento crítico mediante una propuesta de comprensión lectora",
            "revista": "Sinergias Educativas",
            "anio": "2022-06-20| Journal article",
            "contributors": " Guisele Livia Pintado, Graciela Celedonia Sosa Bueno, Victor Francisco Cruz Cisneros",
            "doi": "https://doi.org/10.37954/se.vi.344"
        },
        {
            "titulo": "La Integración de la Nanotecnología en la Educación Alimentaria como Innovación en la Seguridad de Alimentos",
            "revista": "Revista Científica NOBILIS.",
            "anio": "2024-03-12 | Journal article",
            "contributors": "José Daniel Guerra Viteri, MSc.; Graciela Sosa Bueno, PhD.",
            "doi": "https://nobilis.ube.edu.ec/index.php/nobilis/article/view/11"

        },
        {
            "titulo": "Innovación en la Educación Superior: Paradigmas, Transformaciones y Buenas Prácticas Educativas",
            "revista": "Ciencia Latina Revista Científica Multidisciplinar",
            "anio": "2023-07-03 | Journal article",
            "contributors": "Graciela Celedonia Sosa Bueno",
            "doi": "https://doi.org/10.37811/cl_rcm.v7i3.6662"

        },
        {
            "titulo": "Avances Recientes en la Mecánica de Materiales: Tendencias Actuales",
            "revista": "Ibero Ciencias - Revista Científica Y Académica",
            "anio": "2024-09-19 | Journal article",
            "contributors": "Graciela Celedonia Sosa Bueno",
            "doi": "https://doi.org/10.63371/ic.v3.n1.a22"

        },
        {
            "titulo": "Avances Recientes en la Mecánica de Materiales: Tendencias ActualesDiseño de Planos y sus Estructuras: Impacto en la Eficiencia de Construcción",
            "revista": "Revista Veritas De Difusão Científica",
            "anio": "2025-01-08 | Journal article",
            "contributors": "Nùñez Zamora, A. E., Reyes Sandoval, Y. J., Freire Freire, J. R., Neira Muñoz, C. W., De La Cruz Yagual, C. L., Cedeño Bayona, A. L., & Sosa Bueno, G. C. ",
            "doi": "https://doi.org/10.61616/rvdc.v5i3.333"

        },
        {
            "titulo": "El Papel de la Responsabilidad Social Empresarial en la Construcción de Sociedades Sostenibles",
            "revista": "Revista Científica Tecnologik",
            "anio": "2025-10-23 | Journal article",
            "contributors": "Sosa Bueno Graciela Celedonia; Sosa Bueno Mishelle Abigail",
            "doi": "https://revista.tec.istb.edu.ec/index.php/ojs_files/article/view/32"

        },
        {
            "titulo": "Programa ecológico para desarrollar cultura ambiental en estudiantes de Offset",
            "revista": "Revista Científica colloquium biblioteca",
            "anio": "2022-06-03 | Journal article",
            "contributors": "Sosa Bueno, G. C. ., Livia Pintado, G. ., & Astudillo Flores, L. del S.",
            "doi": "https://colloquiumbiblioteca.com/index.php/web/article/view/125"

        },
        {
            "titulo": "Tendencias en el uso de la mecánica de materiales",
            "revista": "Revista Científico-Académica Multidisciplinaria",
            "anio": "2024-11-07 | Journal article",
            "contributors": "Graciela Celedonia Sosa Bueno",
            "doi": "https://polodelconocimiento.com/ojs/index.php/es/article/view/7571"

        },
        {
            "titulo": "Mejoramiento del desempeño docente mediado por una evaluación formativa",
            "revista": "Sinergias Educativas",
            "anio": "2022-06-20 | Journal article",
            "contributors": "Graciela Celedonia Sosa Bueno, Liliana del Socorro Astudillo Flores",
            "doi": "https://doi.org/10.37954/se.vi.337"

        },
        {
            "titulo": "Fortalecimiento de la Cultura Ambiental mediante un programa ecológico en estudiantes del nivel superior",
            "revista": "Sinergias Educativas",
            "anio": "2022-06-20 | Journal article",
            "contributors": "Graciela Celedonia Sosa Bueno, Liliana del Socorro Astudillo Flores, Guiselle Livia Pintado",
            "doi": "https://doi.org/10.37954/se.vi.356"

        },    
    ]

    cards = ""
    for a in articulos:
        cards += f"""
        <div class="card">
            <h3>{a['titulo']}</h3>
            <p><strong>{a['revista']}</strong></p>
            <p>{a['anio']}</p>
            <p><strong>Contributors:</strong> {a['contributors']}</p>
            <a href="{a['doi']}" target="_blank">Ver artículo (DOI)</a>
            <p class="source">✔ Source: Crossref</p>
        </div>
        """

    return f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Artículos Científicos</title>
<style>
body{{background:#f5f5f5;font-family:Arial}}
.container{{max-width:1000px;margin:40px auto}}
.card{{background:white;padding:25px;border-radius:15px;margin-bottom:25px;
box-shadow:0 5px 15px rgba(0,0,0,0.1)}}
.card h3{{color:#00695c}}
.card a{{background:#00c853;color:white;padding:10px 20px;border-radius:8px;
text-decoration:none;display:inline-block;margin-top:10px}}
.source{{color:#2e7d32;font-size:20px;margin-top:10px}}
footer{{background:#eee;color:#555;text-align:center;padding:20px}}
</style>
</head>
<body>
<div class="container">
<h1 style="text-align:center">Artículos Científicos</h1>
{cards}
<p><a href="/registro">Ver registro de visitas</a></p>
</div>
<footer>Página web creada por Graciela Celedonia Sosa Bueno</footer>
</body>
</html>
"""

# ================= REGISTRO =================
@app.route("/registro")
def registro():
    filas = ""
    for v in leer_visitas():
        ip, fecha = v.strip().split(" | ")
        filas += f"<tr><td>{ip}</td><td>{fecha}</td></tr>"

    return f"""
<!DOCTYPE html>
<html>
<body style="background:white;font-family:Arial;padding:40px">
<h1>Registro de Visitas</h1>
<table border="1" cellpadding="10" width="100%">
<tr><th>IP</th><th>Fecha</th></tr>
{filas}
</table>
</body>
</html>
"""

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)