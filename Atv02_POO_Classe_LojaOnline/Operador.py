

class Pedido:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor
        self.cliente = None
        
    def associar_cliente(self, cliente):
        self.cliente = cliente
        
    def __str__(self):
        return f"Pedido: {self.descricao} - R$ {self.valor:.2f}"

class cliente:
    def __init__(self, nome):
        self.nome = nome
        self.pedidos = []
        
    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)
        pedido.associar_cliente(self)
        
    def listar_pedidos(self):
        if not self.pedidos:
            return f"{self.nome} não tem pedidos!"
        
        return f"\n".join(str(pedido) for pedido in self.pedidos)
    
    def __str__(self):
        return f"Cliente: {self.nome}"
    

cliente_joao = cliente("João")
cliente_maria = cliente("Maria")

pedido1 = Pedido("Notebook", 4500)
pedido2 = Pedido("Smartphones", 2000)
pedido3 = Pedido("Fones de Ouvido", 250)

cliente_joao.adicionar_pedido(pedido1)
cliente_joao.adicionar_pedido(pedido3)
cliente_maria.adicionar_pedido(pedido2)

print(f"Pedidos de {cliente_joao}: ")
print(cliente_joao.listar_pedidos())

print(f"\nPedidos de {cliente_maria}: ")
print(cliente_maria.listar_pedidos())