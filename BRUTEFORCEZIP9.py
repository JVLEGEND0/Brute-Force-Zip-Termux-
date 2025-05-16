import time
import threading
import os
from datetime import datetime
import pyzipper
import importlib.util

package_name = "pyzipper"
if importlib.util.find_spec(package_name) is not None:
    pass
else:
    exit(f"O pacote '{package_name}' não está instalado.")

global attempt, caracteres, stop, time1, password, password2, password3, password4, password5, thread, caminho_zip, pasta_destino, senhas
senhas = None
wordlis = None
stop = True
attempt = 0
caracteres = ['', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
stop_password = threading.Event()
lock = threading.Lock()

def arquivo_quebrado(senha):
  global stop, caminho_zip, pasta_destino, senhas
  if not stop_password.is_set():
    try:
        with pyzipper.AESZipFile(caminho_zip, 'r') as zip_ref:
            zip_ref.setpassword(senha.encode())
            zip_ref.extractall(pasta_destino)
        with lock:    
          if not stop_password.is_set():  
            print("Arquivo descompactado com sucesso!")
            senhas = 1
            stop = False
            stop_password.set()
    except RuntimeError as e:
        stop = True
    except:
        stop = True   
              
def arquivo_quebrado2(senha):
  global stop, caminho_zip, pasta_destino, senhas
  if not stop_password.is_set():
    try:
        with pyzipper.AESZipFile(caminho_zip, 'r') as zip_ref:
            zip_ref.setpassword(senha.encode())
            zip_ref.extractall(pasta_destino)
        with lock:    
          if not stop_password.is_set():  
            print("Arquivo descompactado com sucesso!")
            senhas = 2
            stop = False
            stop_password.set()
    except RuntimeError as e:
        stop = True
    except:
        stop = True   
        
def arquivo_quebrado3(senha):
  global stop, caminho_zip, pasta_destino, senhas
  if not stop_password.is_set():
    try:
        with pyzipper.AESZipFile(caminho_zip, 'r') as zip_ref:
            zip_ref.setpassword(senha.encode())
            zip_ref.extractall(pasta_destino)
        with lock:
          if not stop_password.is_set():      
            print("Arquivo descompactado com sucesso!")
            senhas = 3
            stop = False
            stop_password.set()
    except RuntimeError as e:
        stop = True
    except:
        stop = True           
        
def arquivo_quebrado4(senha):
  global stop, caminho_zip, pasta_destino, senhas
  if not stop_password.is_set():
    try:
        with pyzipper.AESZipFile(caminho_zip, 'r') as zip_ref:
            zip_ref.setpassword(senha.encode())
            zip_ref.extractall(pasta_destino)
        with lock:
          if not stop_password.is_set():      
            print("Arquivo descompactado com sucesso!")
            senhas = 4
            stop = False
            stop_password.set()
    except RuntimeError as e:
        stop = True
    except:
        stop = True            
        
def arquivo_quebrado5(senha):
  global stop, caminho_zip, pasta_destino, senhas
  if not stop_password.is_set():
    try:
        with pyzipper.AESZipFile(caminho_zip, 'r') as zip_ref:
            zip_ref.setpassword(senha.encode())
            zip_ref.extractall(pasta_destino)
        with lock:    
          if not stop_password.is_set():  
            print("Arquivo descompactado com sucesso!")
            senhas = 5
            stop = False
            stop_password.set()
    except RuntimeError as e:
        stop = True
    except:
        stop = True                  
        
def wordlist(lists):
    global password5
    if lists != None:
        while not stop_password.is_set():
            try:
                with open(lists, "r") as list:
                    for line in list:
                        password5 = line.strip()
                        arquivo_quebrado5(password5)   
            except FileNotFoundError:
                print("A Wordlist fornecida não foi encontrada")   
                break
    else:
        pass                 
        
def sep1():
    global attempt, caracteres, stop, password, caminho_zip, pasta_destino
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while not stop_password.is_set():
        password = caracteres[a] + caracteres[b] + caracteres[c] + caracteres[d] + caracteres[e]
        arquivo_quebrado(password)
        attempt += 1
        a += 1
        if a == 36:
            b += 1
            a = 0
        if b == 36:
            c += 1
            b = 0
        if c == 36:
            c = 0
            d += 1   
        if d == 36:
            d = 0
            e += 1
        if e == 16:
            print("senha não encontrada")
            stop = False
            yes = False
            break

def sep1_5():
    global attempt, caracteres, stop, password3, caminho_zip
    k = 17
    l = 36
    m = 36
    n = 36
    o = 36
    while not stop_password.is_set():
        password3 = caracteres[k] + caracteres[l] + caracteres[m] + caracteres[n] + caracteres[o]
        arquivo_quebrado3(password3)  
        attempt += 1
        o = o - 1
        if o == -1:
             n = n - 1
             o = 36
        if n == -1:
             m = m - 1
             n = 36
        if m == -1:
             l = l - 1
             m = 36
        if l == -1:
             l = 36
             k = k - 1
        if k == -1:    
             print("senha não encontrada")
             break 
             
def sep5_2():
    global attempt, caracteres, stop, password4, caminho_zip, pasta_destino
    a = 18
    b = 1
    c = 1
    d = 1
    e = 1
    while not stop_password.is_set():
        password4 = caracteres[a] + caracteres[b] + caracteres[c] + caracteres[d] + caracteres[e]
        arquivo_quebrado4(password4)
        attempt += 1
        a += 1
        if a == 36:
            b += 1
            a = 1
        if b == 36:
            c += 1
            b = 1
        if c == 36:
            c = 1
            d += 1   
        if d == 36:
            d = 1
            e += 1
        if e == 16:
            print("senha não encontrada")
            stop = False
            yes = False
            break

def sep2():
    global attempt, caracteres, stop, password2, caminho_zip
    f = 36
    g = 36
    h = 36
    i = 36
    j = 36
    while not stop_password.is_set():
        password2 = caracteres[f] + caracteres[g] + caracteres[h] + caracteres[i] + caracteres[j]
        arquivo_quebrado2(password2)  
        attempt += 1
        j = j - 1
        if j == -1:
             i = i- 1
             j = 36
        if i == -1:
             h = h - 1
             i = 36
        if h == -1:
             g = g - 1
             h = 36
        if g == -1:
             g = 36
             f = f - 1
        if f == -1:    
             print("senha não encontrada")
             break 

def salvar(nome, senha):
    agora = f"Data:{datetime.now().day}/{datetime.now().month}/{datetime.now().year} \
{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
    with open(".Saves.txt", "a") as file:
        file.write(f"\nSenha: {senha}\nArquivo: {nome}\n{agora}\n\n")
        
def historic():
    print("HISTÓRICO:")
    try:
        with open(".Saves.txt", "r") as file:
            linhas = file.readlines()
            for line in reversed(linhas):
                line = line.strip()
                print(line)
    except:
        print("Não tem histórico")      
    finally:
        print("O que você deseja fazer agora? \
\n(a) Inicio\n(clear) DELETAR HISTORICO")     
        try:
            esc = input(">>> ").lower()
            if esc == "a":
                os.system('clear') or None
                inicio()
            if esc == "clear":
                print("Você realmente deseja fazer isso?")
                print("(confirm) Confirmar\n(n) Isso foi um engano")
                esc2 = input(">>> ").lower()
                if esc2 == "confirm":
                    print("Seu desejo é uma ordem...")
                    os.remove(".Saves.txt")  
                    inicio()
                else:
                    inicio()    
            else:
                print("Isso não é uma opção")
                time.sleep(1)
                os.system('clear') or None
                historic()
        except:
            print("Isso não é uma opção")   
             
def quebra():             
    os.system('clear') or None
    global caminho_zip, pasta_destino
    caminho_zip = input('Insira o nome do arquivo (com a extensão dele) >>> ')
    if os.path.exists(caminho_zip):
        pass
    else:
        print("O arquivo específicado não existe")
        print("Aguarde...")
        time.sleep(1)
        inicio()
    if " " in caminho_zip:
        print("O nome do arquivo não pode conter espaços, remova-os")
        print("Aguarde...")
        time.sleep(1)
        inicio()
    if not (".zip" in caminho_zip or ".7z" in caminho_zip):
        print("Isso não é um arquivo .zip ou .7z")
        print("Aguarde...")
        time.sleep(1)
        inicio() 
    print("Insira o nome da pasta para onde irão os arquivos descompactados")
    pasta_destino = input('caso a pasta não for encontrada, o sistema criará uma pasta \ncom o nome específicado >>>  ')
    print("Você tem uma wordlist? (Opcional)")
    print("(s) sim")
    print("(n) não")
    esc = input(">>> ").lower()
    if esc == "n":
        letsgo()
    elif esc == "s":
        wordlis = input("Insira o nome da Wordlist >>> ")
        if os.path.exists(wordlis):
            letsgo()
        else:
            print("A Wordlist fornecida não foi encontrada\ndeseja \
            tentar novamente?")
            print("(s) sim")
            print("(n) não")
            print("(c) continuar mesmo assim")
            esc2 = input(">>> ").lower()
            if esc2 == "s":
                quebra()
            elif esc2 == "n":
                inicio()  
            elif esc2 == "c":
                letsgo()   
            else:
                print("Isso não é uma opção")
                inicio()

def inicio():
    os.system('clear') or None
    print("")            
    print("BEM VINDO AO QUEBRADOR DE SENHA DE ARQUIVOS ZIP")          
    print("Versão: 9.0")            
    print("Em próximas versões, maiores otimizações serão feitas")
    print("O uso desse script é destinado apenas para fins educacionais,")
    print("ou caso tenha esquecido a senha de SEU arquivo.")
    print("O que você deseja fazer?")
    print("(1) Iniciar \n(2) Histórico \n(3) Sair")
    try:
        esc = int(input())
        if esc == 1:
            quebra()
        elif esc == 2:
            historic()
        elif esc == 3:    
            pass
        else:
            print("Isso não é uma opção")
            inicio()
    except:
        print("Isso não é uma opção")
        inicio()


def letsgo():
     os.system('clear') or None
     global attempt, stop, password, password2, password3, password4, password5, thread, senhas, caminho_zip
     thread1 = threading.Thread(target=sep1)
     thread2 = threading.Thread(target=sep2)
     thread3 = threading.Thread(target=sep1_5)
     thread4 = threading.Thread(target=sep5_2)
     thread5 = threading.Thread(target=wordlist, args=(wordlis,))
     
     print("Aproximadamente 128000 combinações estão sendo testadas por minuto.")
     time.sleep(0.3)
     print("OBS: O tempo para testar todas as combinações possíveis")
     print("é de aproximadamente 2 horas (no máximo) dependendo da senha")
     time.sleep(0.3)
     print("Ferramenta iniciada com sucesso :D")
     time.sleep(0.3)
     print("Por favor aguarde...")
     
     thread1.start()           
     thread2.start() 
     thread3.start()           
     thread4.start() 
     thread5.start() 
     
     time1 = time.time()
     
     thread1.join()
     thread2.join()
     thread3.join()
     thread4.join()
     thread5.join()
     
     time2 = time.time() 
     time3 = time2 - time1
     
     time.sleep(2)
     os.system('clear') or None
     print(f"Código de conclusão: {senhas} (Caso não saiba o que \
     isso significa, apenas ignore)")
     if senhas == 1:
         print(f"A senha do arquivo é: {password}")
         salvar(caminho_zip ,password)
     elif senhas == 2:
         print(f"A senha do arquivo é: {password2}")
         salvar(caminho_zip ,password2)
     elif senhas == 3:
         print(f"A senha do arquivo é: {password3}")
         salvar(caminho_zip ,password3)
     elif senhas == 4:
         print(f"A senha do arquivo é: {password4}")  
         salvar(caminho_zip ,password4)    
     elif senhas == 5:
         print(f"A senha do arquivo é: {password5}")  
         salvar(caminho_zip ,password5)        
     else:
         print("Não foi possível encontrar a senha :(")
         
     if time3 < 1.5:
         print("Tempo de execução: instantâneo")
     else:
         print(f"Tempo de execução: {time3:.3f} segundos")
         
     print(f"Quantidade de tentativas: {attempt}")
     print("A senha do arquivo foi quebrada com sucesso!!!")
     
     time.sleep(3)
     inicio()

inicio()
