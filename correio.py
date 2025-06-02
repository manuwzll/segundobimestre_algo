
pacotes = (
    ("ABC123", "Enviado"),
    ("XYZ789", "Recebido"),
    ("DEF456", "Em Trânsito"),
    ("KL321",  "Enviado"),
    ("MNO654", "Recebido"),
    ("PQR987", "Em Trânsito"),
    ("STU741", "Enviado")
)


enviado     = 0
recebido    = 0
em_transito = 0

for _, status in pacotes:
    if status == "Enviado":
        enviado += 1
    elif status == "Recebido":
        recebido += 1
    elif status == "Em Trânsito":
        em_transito += 1

print("Contagem de pacotes:")
print(f"  Enviados    : {enviado}")
print(f"  Recebidos   : {recebido}")
print(f"  Em Trânsito : {em_transito}")


print("\nPacotes em 'Em Trânsito':")
for codigo, status in pacotes:
    if status == "Em Trânsito":
        print(f"  {codigo}")


def buscar_status(codigo):
    for cod, status in pacotes:
        if cod == codigo:
            return f"Status do pacote {codigo}: {status}"
    return f"Pacote {codigo} não está cadastrado."

print("\nConsulta de status:")
print(" ", buscar_status("DEF456"))
print(" ", buscar_status("ZZZ000"))


pacotes_ordenados = tuple(sorted(pacotes))

print("\nPacotes ordenados por código:")
for codigo, status in pacotes_ordenados:
    print(f"  {codigo} - {status}")
