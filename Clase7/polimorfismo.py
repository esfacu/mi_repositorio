class Pato():
    def hablar(self):
        print("Cuack, cuack")
        
pato = Pato()
pato.hablar()

def llama_hablar(x):
    x.hablar()
    
llama_hablar(pato)