from datetime import datetime

def data_extenso(data):
    data = datetime.strptime(data, "%d/%m/%Y")

    dias = [
        "zero", "um", "dois", "três", "quatro", "cinco", "seis",
        "sete", "oito", "nove", "dez", "onze", "doze", "treze",
        "quatorze", "quinze", "dezesseis", "dezessete", "dezoito",
        "dezenove", "vinte", "vinte e um", "vinte e dois", "vinte e três",
        "vinte e quatro", "vinte e cinco", "vinte e seis", "vinte e sete",
        "vinte e oito", "vinte e nove", "trinta", "trinta e um"]
    
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
        "agosto", "setembro", "outubro", "novembro", "dezembro" 
    ]
        
    anos = [
        "dois mil", 
    ]
