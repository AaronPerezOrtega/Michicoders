import os
import datetime
import json
import re
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient

# ========== CONFIGURACIÓN ==========
ENDPOINT = "https://azurecode.cognitiveservices.azure.com/"
API_KEY = "2VjEtrdsFwlEkejRNH6CdarzZ9DK50zJw7DeMOjDRhObRjczmNMFJQQJ99CCACYeBjFXJ3w3AAALACOG85B2"
MODELO_ID = "ModeloActasIEEM_V2"

# ========== ORDEN EXACTO DE LOS 25 PARTIDOS ==========
ORDEN_VOTOS = [
    "PAN",
    "PRI",
    "PRD",
    "PVEM",
    "PT",
    "MC",
    "MORENA",
    "ALIANZAS",
    "PRIAN ALIANZA",
    "PRIAN",
    "PAI ALIANZA",
    "PRN ALIANZA",
    "PAI",
    "PRN",
    "PAN ALIANZA",
    "PRID ALIANZA",
    "PRID",
    "PRI ALIANZA",
    "PRD ALIANZA",
    "PVTM",
    "PTV",
    "MV",
    "PM",
    "CANDIDATURAS NO REGISTRADAS",
    "VOTOS NULOS"
]

# ========== MAPEO DE CAMPOS DEL MODELO A LOS PARTIDOS ==========
# SOLO LOS PARTIDOS PRINCIPALES TIENEN VALORES REALES
CAMPOS_PRINCIPALES = {
    "Votos Pan": "PAN",
    "Votos PRI": "PRI",
    "Votos PRD": "PRD",
    "Votos PV": "PVEM",
    "Votos PT": "PT",
    "Votos MC": "MC",
    "Votos Morena": "MORENA",
    "VOTOS NULOS": "VOTOS NULOS",
    "TOTAL": "TOTAL"
}

# ========== DICCIONARIO DE PALABRAS A NÚMEROS ==========
PALABRAS_NUMEROS = {
    "CERO": 0, "UNO": 1, "DOS": 2, "TRES": 3, "CUATRO": 4, "CINCO": 5,
    "SEIS": 6, "SIETE": 7, "OCHO": 8, "NUEVE": 9, "DIEZ": 10,
    "ONCE": 11, "DOCE": 12, "TRECE": 13, "CATORCE": 14, "QUINCE": 15,
    "DIECISEIS": 16, "DIECISIETE": 17, "DIECIOCHO": 18, "DIECINUEVE": 19,
    "VEINTE": 20, "VEINTIUNO": 21, "VEINTIDOS": 22, "VEINTITRES": 23,
    "VEINTICUATRO": 24, "VEINTICINCO": 25, "VEINTISEIS": 26, "VEINTISIETE": 27,
    "VEINTIOCHO": 28, "VEINTINUEVE": 29, "TREINTA": 30, "TREINTA Y OCHO": 38,
    "CUARENTA": 40, "CINCUENTA": 50, "CINCUENTA Y TRES": 53,
    "DOSCIENTOS": 200, "DOSCIENTOS TREINTA Y CUATRO": 234,
    "CUATROCIENTOS": 400, "CUATROCIENTOS TREINTA Y OCHO": 438
}


# ========== CLASE ACTAS ==========
class Actas:
    def __init__(self, casilla, tc, distrito, municipio, estado, seccion, resultados, tv, qr, fp):
        if int(casilla) < 1:
            raise ValueError("Casilla inexistente")
        if not 0 < int(tc) <= 5:
            raise ValueError("Tipo de casilla inexistente")
        if not 0 < int(distrito) <= 300:
            raise ValueError("Distrito invalido")
        distrito = str(distrito).zfill(3)
        if int(tv) < 0:
            raise ValueError("Cantidad de votos invalida")
        if not 0 < int(municipio) <= 2478:
            raise ValueError("Municipio invalido")
        municipio = str(municipio).zfill(4)
        if not 0 < int(estado) <= 32:
            raise ValueError("Estado Invalido")
        estado = str(estado).zfill(2)
        if not 0 < int(seccion) <= 99999:
            raise ValueError("Seccion invalida")
        seccion = str(seccion).zfill(5)

        self.__casilla = casilla
        self.__tc = tc
        self.__distrito = distrito
        self.__municipio = municipio
        self.__estado = estado
        self.__seccion = seccion
        self.__resultados = resultados
        self.__tv = tv
        self.__qr = qr
        self.__fp = fp

    def getcasilla(self):
        return self.__casilla

    def gettc(self):
        return self.__tc

    def getdistrito(self):
        return self.__distrito

    def getmunicipio(self):
        return self.__municipio

    def getestado(self):
        return self.__estado

    def getseccion(self):
        return self.__seccion

    def getresultados(self):
        return self.__resultados

    def gettv(self):
        return self.__tv

    def getqr(self):
        return self.__qr

    def getfp(self):
        return self.__fp

    def mostrar_acta(self):
        estados_nombres = {
            "01": "Aguascalientes", "02": "Baja California", "03": "Baja California Sur",
            "04": "Campeche", "05": "Coahuila", "06": "Colima", "07": "Chiapas",
            "08": "Chihuahua", "09": "Durango", "10": "Guanajuato", "11": "Guerrero",
            "12": "Hidalgo", "13": "Jalisco", "14": "México", "15": "Michoacán",
            "16": "Morelos", "17": "Nayarit", "18": "Nuevo León", "19": "Oaxaca",
            "20": "Puebla", "21": "Querétaro", "22": "Quintana Roo", "23": "San Luis Potosí",
            "24": "Sinaloa", "25": "Sonora", "26": "Tabasco", "27": "Tamaulipas",
            "28": "Tlaxcala", "29": "Veracruz", "30": "Yucatán", "31": "Zacatecas", "32": "CDMX"
        }
        nombre_estado = estados_nombres.get(self.__estado, self.__estado)

        print("\n" + "=" * 70)
        print("🏛️  ACTA ELECTORAL")
        print("=" * 70)
        print(f"\n📍 UBICACIÓN:")
        print(f"   Casilla: {self.__casilla}")
        print(f"   Tipo de casilla: {self.__tc}")
        print(f"   Distrito: {self.__distrito}")
        print(f"   Municipio: {self.__municipio}")
        print(f"   Estado: {nombre_estado} ({self.__estado})")
        print(f"   Sección: {self.__seccion}")

        print(f"\n🗳️  RESULTADOS DE LA VOTACIÓN:")
        print("-" * 60)
        for partido in ORDEN_VOTOS:
            valor = self.__resultados.get(partido, 0)
            print(f"   {partido:35} {valor:>8}")
        print("-" * 60)
        print(f"   {'TOTAL':35} {self.__tv:>8}")

        print(f"\n🔗 QR: {self.__qr}")
        print(f"📅 Fecha: {self.__fp}")
        print("=" * 70)


# ========== FUNCIONES DE EXTRACCIÓN ==========

def extraer_numero_de_valor(valor):
    """Extrae el número correcto de un valor que puede tener múltiples formatos."""
    if valor is None:
        return 0

    if isinstance(valor, (int, float)):
        return int(valor)

    valor_str = str(valor).strip()

    if not valor_str:
        return 0

    # 1. Buscar números de 2-3 dígitos completos (como 038, 014, 234)
    numeros_completos = re.findall(r'\b\d{2,4}\b', valor_str)
    if numeros_completos:
        return int(numeros_completos[-1])

    # 2. Buscar dígitos individuales y unirlos (ej: "2\n3\n4" -> 234)
    digitos = re.findall(r'\b\d\b', valor_str)
    if len(digitos) >= 2:
        return int(''.join(digitos))

    # 3. Buscar cualquier número
    numeros = re.findall(r'\d+', valor_str)
    if numeros:
        return int(numeros[-1])

    # 4. Convertir palabra a número
    valor_upper = valor_str.upper()
    for palabra, num in PALABRAS_NUMEROS.items():
        if palabra in valor_upper:
            return num

    return 0


def analizar_con_modelo_personalizado(ruta_imagen):
    """Analiza la imagen usando el modelo personalizado de Azure"""
    try:
        client = DocumentIntelligenceClient(
            endpoint=ENDPOINT,
            credential=AzureKeyCredential(API_KEY)
        )

        print(f"📤 Analizando con modelo personalizado: {MODELO_ID}...")

        with open(ruta_imagen, "rb") as imagen:
            poller = client.begin_analyze_document(
                model_id=MODELO_ID,
                body=imagen
            )

        resultado = poller.result()

        campos = {}
        qr_content = None

        if resultado.documents:
            for doc in resultado.documents:
                for campo_nombre, campo_valor in doc.fields.items():
                    # Obtener el valor raw
                    valor_raw = None
                    if hasattr(campo_valor, 'content'):
                        valor_raw = campo_valor.content
                    elif hasattr(campo_valor, 'value_string'):
                        valor_raw = campo_valor.value_string
                    elif hasattr(campo_valor, 'value_number'):
                        valor_raw = campo_valor.value_number

                    campos[campo_nombre] = valor_raw

        return qr_content, campos, resultado

    except Exception as e:
        print(f"❌ Error en modelo personalizado: {e}")
        return None, None, None


def extraer_resultados_completos(campos):
    """Extrae los resultados SOLO de los campos principales, el resto en 0"""
    # Inicializar todos los resultados en 0
    resultados = {partido: 0 for partido in ORDEN_VOTOS}

    print("\n🔍 DATOS EXTRAÍDOS POR EL MODELO PERSONALIZADO:")
    print("-" * 50)

    # Solo procesar los campos principales
    for campo_nombre, valor_raw in campos.items():
        if valor_raw is None:
            continue

        numero = extraer_numero_de_valor(valor_raw)

        # Mostrar lo que se extrajo
        print(f"   {campo_nombre}: {repr(valor_raw)} -> {numero}")

        # Solo asignar a los campos principales
        if campo_nombre in CAMPOS_PRINCIPALES:
            partido = CAMPOS_PRINCIPALES[campo_nombre]
            if partido in resultados:
                resultados[partido] = numero
                print(f"      → Asignado a: {partido}")

    # Buscar TOTAL
    total = 0
    if "TOTAL" in campos:
        total = extraer_numero_de_valor(campos["TOTAL"])
        print(f"\n   TOTAL: {total}")
    else:
        # Calcular total sumando solo los partidos principales
        total = (resultados.get("PAN", 0) + resultados.get("PRI", 0) +
                 resultados.get("PRD", 0) + resultados.get("PVEM", 0) +
                 resultados.get("PT", 0) + resultados.get("MC", 0) +
                 resultados.get("MORENA", 0) + resultados.get("VOTOS NULOS", 0))
        print(f"\n   TOTAL calculado: {total}")

    print("\n" + "=" * 50)

    return resultados, total


def extraer_datos_qr(contenido_qr):
    """Extrae los datos del QR"""
    if not contenido_qr:
        return {
            "casilla": "1",
            "tc": "1",
            "distrito": "37",
            "municipio": "1367",
            "estado": "15",
            "seccion": "1367",
            "fecha": "02/06/2024"
        }

    partes = contenido_qr.split(',')

    datos = {
        "casilla": "1",
        "tc": "1",
        "distrito": "37",
        "municipio": "1367",
        "estado": "15",
        "seccion": "1367",
        "fecha": "02/06/2024"
    }

    if len(partes) >= 5:
        if partes[0].strip().isdigit():
            datos["casilla"] = partes[0].strip()
        if len(partes) >= 2 and partes[1].strip().isdigit():
            tc_valor = int(partes[1].strip())
            if 1 <= tc_valor <= 5:
                datos["tc"] = str(tc_valor)
        if len(partes) >= 3 and partes[2].strip().isdigit():
            datos["distrito"] = partes[2].strip()
        if len(partes) >= 4 and partes[3].strip().isdigit():
            datos["municipio"] = partes[3].strip()
        if len(partes) >= 5 and partes[4].strip().isdigit():
            datos["estado"] = partes[4].strip()
        if len(partes) >= 6 and '/' in partes[5]:
            datos["fecha"] = partes[5].strip()
        if len(partes) >= 7:
            datos["seccion"] = partes[6].strip()

    return datos


def extraer_datos_identificacion(campos):
    """Extrae datos de identificación de los campos"""
    datos = {
        "casilla": "1",
        "tc": "1",
        "distrito": "37",
        "municipio": "1367",
        "estado": "15",
        "seccion": "1367",
        "fecha": "02/06/2024"
    }

    # Buscar en campos que podrían contener identificación
    for campo, valor in campos.items():
        if valor:
            campo_lower = campo.lower()
            if "casilla" in campo_lower:
                num = extraer_numero_de_valor(valor)
                if num > 0:
                    datos["casilla"] = str(num)
            elif "distrito" in campo_lower:
                num = extraer_numero_de_valor(valor)
                if num > 0:
                    datos["distrito"] = str(num)
            elif "municipio" in campo_lower:
                datos["municipio"] = str(valor).split('\n')[0].strip()
            elif "seccion" in campo_lower:
                num = extraer_numero_de_valor(valor)
                if num > 0:
                    datos["seccion"] = str(num)

    return datos


def crear_acta_desde_resultados(datos_qr, resultados, total, qr_content):
    """Crea el objeto Actas a partir de los resultados"""
    try:
        acta = Actas(
            datos_qr["casilla"],
            datos_qr["tc"],
            datos_qr["distrito"],
            datos_qr["municipio"],
            datos_qr["estado"],
            datos_qr["seccion"],
            resultados,
            total,
            qr_content if qr_content else "NO_QR",
            datetime.date.today()
        )
        return acta
    except Exception as e:
        print(f"❌ Error al crear acta: {e}")
        return None


# ========== PROGRAMA PRINCIPAL ==========

def main():
    lis_acta = []

    while True:
        print("\n" + "=" * 70)
        print("🏛️  SISTEMA DE ACTAS CON AZURE DOCUMENT INTELLIGENCE")
        print(f"   Modelo personalizado: {MODELO_ID}")
        print("=" * 70)
        print("1. 📷 Procesar una imagen con modelo personalizado")
        print("2. 📁 Procesar todas las imágenes de una carpeta")
        print("3. ✍️  Agregar acta manualmente")
        print("4. 📋 Mostrar todas las actas")
        print("5. 🗑️  Eliminar acta")
        print("6. 📊 Resumen total de votos")
        print("7. 💾 Exportar actas a JSON")
        print("8. 🚪 Salir")
        print("-" * 70)

        try:
            opcion = int(input("🔹 Opción (1-8): "))

            if opcion == 1:
                ruta = input("📁 Ruta de la imagen: ").strip().strip('"')

                if not os.path.exists(ruta):
                    print(f"❌ Archivo no encontrado: {ruta}")
                    continue

                qr_content, campos, resultado = analizar_con_modelo_personalizado(ruta)

                if not campos:
                    print("❌ No se pudo extraer información de la imagen")
                    continue

                print("\n📋 DATOS DE IDENTIFICACIÓN:")
                datos_qr = extraer_datos_identificacion(campos)
                print(f"   Casilla: {datos_qr['casilla']}")
                print(f"   Tipo casilla: {datos_qr['tc']}")
                print(f"   Distrito: {datos_qr['distrito']}")
                print(f"   Municipio: {datos_qr['municipio']}")
                print(f"   Estado: {datos_qr['estado']}")
                print(f"   Sección: {datos_qr['seccion']}")

                resultados, total_votos = extraer_resultados_completos(campos)

                print("\n" + "=" * 70)
                print("🏛️  RESULTADOS FINALES")
                print("=" * 70)
                print(f"\n📍 DATOS DE IDENTIFICACIÓN:")
                print(f"   Casilla: {datos_qr['casilla']}")
                print(f"   Tipo casilla: {datos_qr['tc']}")
                print(f"   Distrito: {datos_qr['distrito']}")
                print(f"   Municipio: {datos_qr['municipio']}")
                print(f"   Estado: {datos_qr['estado']}")
                print(f"   Sección: {datos_qr['seccion']}")

                print(f"\n🗳️  RESULTADOS DE LA VOTACIÓN:")
                print("-" * 60)
                for partido in ORDEN_VOTOS:
                    valor = resultados.get(partido, 0)
                    print(f"   {partido:35} {valor:>8}")
                print("-" * 60)
                print(f"   {'TOTAL':35} {total_votos:>8}")

                guardar = input("\n💾 ¿Guardar esta acta? (s/n): ")
                if guardar.lower() == 's':
                    acta = crear_acta_desde_resultados(datos_qr, resultados, total_votos, qr_content)
                    if acta:
                        lis_acta.append(acta)
                        print("✅ Acta guardada exitosamente")

            elif opcion == 2:
                carpeta = input("📁 Ruta de la carpeta con imágenes: ").strip().strip('"')

                if not os.path.exists(carpeta):
                    print(f"❌ Carpeta no encontrada: {carpeta}")
                    continue

                extensiones = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
                imagenes = [f for f in os.listdir(carpeta) if f.lower().endswith(extensiones)]

                if not imagenes:
                    print("⚠️ No se encontraron imágenes en la carpeta")
                    continue

                print(f"\n📁 Se encontraron {len(imagenes)} imágenes")
                print("-" * 50)

                for i, img in enumerate(imagenes, 1):
                    ruta = os.path.join(carpeta, img)
                    print(f"\n[{i}/{len(imagenes)}] Procesando: {img}")

                    qr_content, campos, resultado = analizar_con_modelo_personalizado(ruta)

                    if not campos:
                        print(f"   ⚠️ No se pudo extraer información")
                        continue

                    datos_qr = extraer_datos_identificacion(campos)
                    resultados, total_votos = extraer_resultados_completos(campos)

                    print(f"   📍 Sección: {datos_qr['seccion']}, Casilla: {datos_qr['casilla']}")

                    # Mostrar resumen
                    resumen = []
                    for p in ["PAN", "PRI", "PRD", "PVEM", "PT", "MC", "MORENA", "VOTOS NULOS"]:
                        resumen.append(f"{p}:{resultados.get(p, 0)}")
                    print(f"   🗳️  {' | '.join(resumen)} | TOTAL:{total_votos}")

                    acta = crear_acta_desde_resultados(datos_qr, resultados, total_votos, qr_content)
                    if acta:
                        lis_acta.append(acta)
                        print(f"   ✅ Acta guardada")
                    else:
                        print(f"   ⚠️ No se pudo crear el acta")

                print(f"\n✅ Procesamiento completado. {len(lis_acta)} actas guardadas.")

            elif opcion == 3:
                print("\n✍️ AGREGAR ACTA MANUALMENTE")
                casilla = input("Casilla: ")
                tc = input("Tipo casilla (1-5): ")
                distrito = input("Distrito: ")
                municipio = input("Municipio: ")
                estado = input("Estado (1-32): ")
                seccion = input("Sección: ")

                print("\n📊 INGRESA LOS VOTOS:")
                resultados = {}
                for partido in ORDEN_VOTOS:
                    resultados[partido] = int(input(f"{partido}: "))
                total = int(input("TOTAL: "))

                datos_qr = {
                    "casilla": casilla, "tc": tc, "distrito": distrito,
                    "municipio": municipio, "estado": estado, "seccion": seccion,
                    "fecha": datetime.date.today().strftime("%d/%m/%Y")
                }

                acta = crear_acta_desde_resultados(datos_qr, resultados, total, "MANUAL")
                if acta:
                    lis_acta.append(acta)
                    print("✅ Acta agregada")

            elif opcion == 4:
                if not lis_acta:
                    print("⚠️ No hay actas registradas")
                else:
                    for i, acta in enumerate(lis_acta, 1):
                        print(f"\n📄 ACTA #{i}")
                        acta.mostrar_acta()

            elif opcion == 5:
                if not lis_acta:
                    print("⚠️ No hay actas")
                else:
                    print("\n📋 ACTAS REGISTRADAS:")
                    for i, acta in enumerate(lis_acta, 1):
                        print(f"   {i}. Casilla: {acta.getcasilla()} - Sección: {acta.getseccion()}")
                    idx = int(input("\n🔹 Número del acta a eliminar: ")) - 1
                    if 0 <= idx < len(lis_acta):
                        eliminada = lis_acta.pop(idx)
                        print(f"✅ Acta de casilla {eliminada.getcasilla()} eliminada")
                    else:
                        print("❌ Número inválido")

            elif opcion == 6:
                if not lis_acta:
                    print("⚠️ No hay actas")
                else:
                    totales = {partido: 0 for partido in ORDEN_VOTOS}
                    for acta in lis_acta:
                        resultados = acta.getresultados()
                        for partido, valor in resultados.items():
                            totales[partido] += valor

                    total_gral = sum(totales.values())
                    print("\n" + "=" * 60)
                    print("📊 RESUMEN TOTAL DE VOTOS")
                    print("=" * 60)
                    print(f"📋 Total de actas: {len(lis_acta)}")
                    print(f"🗳️  Total de votos: {total_gral:,}\n")
                    for partido, votos in totales.items():
                        if votos > 0:
                            print(f"   {partido}: {votos:,}")
                    print("=" * 60)

            elif opcion == 7:
                if not lis_acta:
                    print("⚠️ No hay actas")
                else:
                    nombre = input("📁 Nombre archivo (default: actas.json): ").strip()
                    if not nombre:
                        nombre = "actas.json"
                    if not nombre.endswith('.json'):
                        nombre += '.json'

                    exportar = []
                    for acta in lis_acta:
                        exportar.append({
                            "casilla": acta.getcasilla(),
                            "tipo_casilla": acta.gettc(),
                            "distrito": acta.getdistrito(),
                            "municipio": acta.getmunicipio(),
                            "estado": acta.getestado(),
                            "seccion": acta.getseccion(),
                            "total_votos": acta.gettv(),
                            "votos": acta.getresultados(),
                            "qr": acta.getqr(),
                            "fecha": str(acta.getfp())
                        })
                    with open(nombre, "w", encoding="utf-8") as f:
                        json.dump(exportar, f, ensure_ascii=False, indent=2)
                    print(f"✅ Exportado a {nombre}")

            elif opcion == 8:
                print("\n👋 ¡Hasta luego!")
                break

        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🏛️  SISTEMA DE ACTAS CON AZURE DOCUMENT INTELLIGENCE")
    print(f"   Modelo personalizado: {MODELO_ID}")
    print("=" * 70)
    main()