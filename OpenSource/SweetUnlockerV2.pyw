import customtkinter as ctk
from tkinter import filedialog, messagebox
import subprocess
import os
import sys

VERSION = "1.0 BETA"

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def selecionar_mod():
    global mod_path
    mod_path = filedialog.askopenfilename(
        title="Selecione um .scs ou .zip",
        filetypes=[("Mod files", "*.scs *.zip")]
    )
    if mod_path:
        lbl_mod.configure(text=os.path.basename(mod_path))
        btn_desbloquear.configure(state="normal")
    else:
        lbl_mod.configure(text="Nenhum arquivo selecionado")
        btn_desbloquear.configure(state="disabled")

def desbloquear_mod():
    if not mod_path:
        messagebox.showwarning("Aviso", "Nenhum mod selecionado!")
        return

    extractor = resource_path("extractor.exe")
    if not os.path.exists(extractor):
        messagebox.showerror("Erro", "extractor.exe não encontrado!")
        return

    # Executa o extractor.exe
    subprocess.run([extractor, mod_path, "--deep", "--dest", "SweetRlk"])
    messagebox.showinfo("Concluído", "Mod desbloqueado com sucesso!")

def abrir_pasta():
    caminho_pasta = os.path.abspath("SweetRlk")
    if os.path.exists(caminho_pasta):
        os.startfile(caminho_pasta)
    else:
        messagebox.showerror("Erro", "A pasta SweetRlk não foi encontrada!\nDesbloqueie um mod primeiro.")

app = ctk.CTk()
app.title(f"Sweet Unlocker v{VERSION}")
app.geometry("500x280")
app.geometry("500x320")

frame = ctk.CTkFrame(app, corner_radius=12)
frame.pack(pady=20, padx=20, fill="both", expand=True)

lbl_title = ctk.CTkLabel(frame, text="Selecione um Mod (.scs / .zip)", font=("Arial", 18))
lbl_title.pack(pady=10)

btn_selecionar = ctk.CTkButton(frame, text="Selecionar Mod", command=selecionar_mod)
btn_selecionar.pack(pady=10)

lbl_mod = ctk.CTkLabel(frame, text="Nenhum arquivo selecionado", text_color="gray")
lbl_mod.pack(pady=10)

btn_desbloquear = ctk.CTkButton(frame, text="Desbloquear Mod", command=desbloquear_mod, state="disabled")
btn_desbloquear.pack(pady=15)

btn_abrir = ctk.CTkButton(frame, text="Abrir Pasta SweetRlk", command=abrir_pasta, fg_color="green", hover_color="darkgreen")
btn_abrir.pack(pady=5)

lbl_status = ctk.CTkLabel(frame, text="Verificando status...", font=("Arial", 12))
lbl_status.pack(pady=5)

lbl_version = ctk.CTkLabel(frame, text=f"Versão: {VERSION}", font=("Arial", 10), text_color="gray")
lbl_version.pack(pady=2)

def verificar_status():
    if os.path.exists(resource_path("extractor.exe")):
        lbl_status.configure(text="Status: Extractor ON", text_color="green")
    else:
        lbl_status.configure(text="Status: Extractor OFF", text_color="red")

verificar_status()

app.mainloop()
