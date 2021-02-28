from tkinter import *
import time

root=Tk()
root.title("Calculadora")
root.iconbitmap("msh.ico")

calFrame = Frame(root)
calFrame.pack(padx=2, pady=4)

# Variables globales
ultimaTecla=""
enPantalla = StringVar()
enPantalla.set("0")
enVisor = StringVar()
enVisor.set("")

# Pantalla
visor = Label(calFrame, textvariable=enVisor)
visor.grid(row=0, column=0, padx=2, pady=2, columnspan=5)
visor.config(bg="lightgrey",fg="grey", font=("Arial",8), anchor="e", width=40)

pantalla = Label(calFrame, textvariable=enPantalla)
pantalla.grid(row=1,column=0, padx=2, pady=2, columnspan=5)
pantalla.config(bg="black", fg="#00FA11", font=("Arial",12), anchor="e", width=27)

# Botones
botonDel = Button(calFrame, text="<<", width=5, command=lambda:botonPulsado("<<"))
botonDel.grid(row=2,column=0) 
botonCE = Button(calFrame, text="CE", width=5, command=lambda:botonPulsado("CE"))
botonCE.grid(row=3,column=0) 
botonAC = Button(calFrame, text="AC", width=5, command=lambda:botonPulsado("AC"))
botonAC.grid(row=4,column=0) 
botonSN = Button(calFrame, text="+/-", width=5, command=lambda:botonPulsado("+/-"))
botonSN.grid(row=5,column=0)

boton7 = Button(calFrame, text="7", width=5, command=lambda:botonPulsado("7"))
boton7.grid(row=2,column=1) 
boton8 = Button(calFrame, text="8", width=5, command=lambda:botonPulsado("8"))
boton8.grid(row=2,column=2) 
boton9 = Button(calFrame, text="9", width=5, command=lambda:botonPulsado("9"))
boton9.grid(row=2,column=3) 
botonDiv = Button(calFrame, text="/", width=5, command=lambda:botonPulsado("/"))
botonDiv.grid(row=2,column=4)

boton4 = Button(calFrame, text="4", width=5, command=lambda:botonPulsado("4"))
boton4.grid(row=3,column=1) 
boton5 = Button(calFrame, text="5", width=5, command=lambda:botonPulsado("5"))
boton5.grid(row=3,column=2) 
boton6 = Button(calFrame, text="6", width=5, command=lambda:botonPulsado("6"))
boton6.grid(row=3,column=3) 
botonMul = Button(calFrame, text="X", width=5, command=lambda:botonPulsado("*"))
botonMul.grid(row=3,column=4)

boton1 = Button(calFrame, text="1", width=5, command=lambda:botonPulsado("1"))
boton1.grid(row=4,column=1) 
boton2 = Button(calFrame, text="2", width=5, command=lambda:botonPulsado("2"))
boton2.grid(row=4,column=2) 
boton3 = Button(calFrame, text="3", width=5, command=lambda:botonPulsado("3"))
boton3.grid(row=4,column=3) 
botonRes = Button(calFrame, text="-", width=5, command=lambda:botonPulsado("-"))
botonRes.grid(row=4,column=4)

boton0 = Button(calFrame, text="0", width=5, command=lambda:botonPulsado("0"))
boton0.grid(row=5,column=1) 
botonPun = Button(calFrame, text=",", width=5, command=lambda:botonPulsado(","))
botonPun.grid(row=5,column=2) 
botonIgu = Button(calFrame, text="=", width=5, command=lambda:botonPulsado("="))
botonIgu.grid(row=5,column=3) 
botonSum = Button(calFrame, text="+", width=5, command=lambda:botonPulsado("+"))
botonSum.grid(row=5,column=4)

# Pulsaciones de teclado
def botonPulsado(tecla):

    global ultimaTecla
    
    if ultimaTecla=="=":
        strVisor=""
        enVisor.set("")

    strPantalla=enPantalla.get()
    strVisor=enVisor.get()

    if tecla=="<<":
        if len(strPantalla)>1:
            strPantalla=strPantalla[:-1]
        else:
            strPantalla="0"
    elif tecla=="CE":
        strPantalla="0"
    elif tecla=="AC":
        strPantalla="0"
        strVisor=""
    elif tecla=="+/-":
        if strPantalla[0]=="-":
            strPantalla=strPantalla[1:]
        else:
            strPantalla="-" + strPantalla
    elif tecla==",":
        if tecla not in strPantalla:
            strPantalla+=tecla
    elif tecla in "0123456789ABCDEF":
        if ultimaTecla in "/*-+=":
            strPantalla=""
        strPantalla+=tecla
        if "," not in strPantalla:
            strPantalla=strPantalla.lstrip("0")
        if strPantalla=="":
            strPantalla="0"
    elif tecla in "/*-+=":
        if strPantalla[-1] == ",":
            strPantalla = strPantalla[:-1]
        strVisor+= strPantalla  + tecla
        if tecla == "=":
            strAux=strPantalla.replace(".","")
            strAux=strAux.replace(",",".")
            strAux=str(eval(strVisor[:-1]))
            strAux=strAux.replace(".",",")
            strVisor+= strAux
            strPantalla=strAux
    ultimaTecla=tecla    
    enPantalla.set(strPantalla)
    enVisor.set(strVisor)

# Simular la pulsación con el ratón desde el teclado
def simulaPulsacion(boton):
        boton.event_generate("<Button-1>")
        root.update()
        time.sleep(0.04)
        boton.invoke()
        boton.event_generate("<ButtonRelease-1>")

# Pulsaciones con ratón en botones de la calculadora
def calPulsacion(evento):
    if evento.char=="0":
        simulaPulsacion(boton0)
    elif evento.char=="1":
        simulaPulsacion(boton1)
    elif evento.char=="2":
        simulaPulsacion(boton2)
    elif evento.char=="3":
        simulaPulsacion(boton3)
    elif evento.char=="4":
        simulaPulsacion(boton4)
    elif evento.char=="5":
        simulaPulsacion(boton5)
    elif evento.char=="6":
        simulaPulsacion(boton6)
    elif evento.char=="7":
        simulaPulsacion(boton7)
    elif evento.char=="8":
        simulaPulsacion(boton8)
    elif evento.char=="9":
        simulaPulsacion(boton9)
    elif evento.char=="+":
        simulaPulsacion(botonSum)
    elif evento.char=="-":
        simulaPulsacion(botonRes)
    elif evento.char=="*" or evento.char=="x" or evento.char=="X":
        simulaPulsacion(botonMul)
    elif evento.char=="/" or evento.char=="/":
        simulaPulsacion(botonDiv)
    elif evento.char=="." or evento.char==",":
        simulaPulsacion(botonPun)
    elif evento.char=="" and (evento.keysym=="minus" or evento.keysym=="plus"):
        simulaPulsacion(botonSN)
    elif evento.char=="=" or evento.keysym=="Return":
        simulaPulsacion(botonIgu)
    elif evento.keysym=="Delete" or evento.char=="\x08":
        simulaPulsacion(botonDel)
    elif evento.char=="\x7F":
        simulaPulsacion(botonCE)
    elif evento.char=="" and evento.keysym=="BackSpace":
        simulaPulsacion(botonAC)

root.bind("<Key>", calPulsacion)
root.mainloop()
