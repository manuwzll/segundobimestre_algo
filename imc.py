def calculadora_imc(pessoa):
    imc= pessoa ["peso"]/ (pessoa ["altura"] * pessoa ["altura"])
    resultado = f"0 imc {pessoa["nome"]} é {imc:.2f}"
    #comando ternário
    saudavel = 18.5 < imc < 25

    return{
        "nome": pessoa ["nome"],
        "imc": imc,
        "resultado": resultado,
        "saudavel": saudavel
    }

pessoa1={
        "nome":"josé",
        "peso": 110,
        "altura": 1.75
    }
print (calculadora_imc(pessoa1))

pessoa2={
        "nome":"maria",
        "peso":20,
        "altura": 1.80

}