# Opções de ações do menu
options = {
    1: "Adicionar um item ao carrinho",
    2: "Ver todos os itens do carrinho",
    3: "Selecionar um item do carrinho",
    4: "Remover um item do carrinho",
    5: "Finalizar execução"
}

# Classe com atributos e métodos de um item inserido em um carrinho
class Item():
    def __init__(self, id_user: str, id_product: str, price_product: float, quantity_product: int):
        self.id_user = id_user
        self.id_product = id_product
        self.price_product = price_product
        self.quantity_product = quantity_product

    # Método que retorna os atributos em um dicionário para ser adicionado ao carrinho
    def add_item(self):
        return {
            "id_user": self.id_user,
            "id_product": self.id_product,
            "price_product": self.price_product,
            "quantity_product": self.quantity_product,
        }
        

# Classe com atributos e métodos de um carrinho
class Cart:
    def __init__(self, cart: list):
        self.cart = cart
        
    # Método que pede as informações do item para o usuário ao instanciar a classe Item e o adiciona ao carrinho
    def add_new_item(self):
        id_user = input("Insira o id do usuário: ")
        id_product = input("Insira o id do produto: ")
        price_product = float(input("Insira o preço do produto: "))
        quantity_product = int(input("Insira a quantidade do produto: "))
        new_item = Item(id_user, id_product, price_product, quantity_product)
        self.cart.append(new_item.add_item())
        return new_item
    
    # Método que itera todos os itens do carrinho para exibir ao usuário
    def get_all_items(self):
        for item in self.cart:
            print(item)

    # Método que retorna apenas o item que o usuário solicitou pelo id do produto
    def get_item_by_id(self, id_product: str):
        for item in self.cart:
            if item["id_product"] == id_product:
                return item

    # Método que itera os itens e deleta o item solicitado pelo usuário do carrinho
    def remove_item_by_id(self, id_product):
        for index, item in enumerate(self.cart):
            if item["id_product"] == id_product:
                del self.cart[index]
                return item
        
        
# Classe utilizada para manipular os métodos do carrinho e o tempo de execução do script
class Menu():
    def __init__(self, running: bool, options: dict):
        self.running = running
        self.options = options
    
    # Método utilizado para exibir as opções de ações para o usuário
    def print_options(self):
        print("Insira o número da função que deseja realizar: ")
        for key, option in self.options.items():
            print(key, option)
    
    # Método utilizado para encerrar a execução do script
    def shutdown(self):
        self.running = False


# Função que dá inicio ao script (pendente de refatoração)
def init_cart():
    new_cart = Cart(cart=[])
    menu = Menu(True, options)
    while(menu.running == True):
        menu.print_options()
        chosen_option = int(input("Opção: "))
        # Estrutura de if-elif-else utilizada para executar os métodos de acordo com a ação selecionada
        # Queria ter feito com switch, mas não deu muito certo e vai ficar pra depois :)
        if chosen_option == 1:
            new_cart.add_new_item()
            print("Item adicionado!")
        elif chosen_option == 2:
            print("Todos os itens: ")
            new_cart.get_all_items()
        elif chosen_option == 3:
            id = input("Insira o id do produto que deseja selecionar: ")
            item = new_cart.get_item_by_id(id)
            if item is None:
                print("Item não encontrado!")
            else: 
                print("Item selecionado: ")    
                print(item)
        elif chosen_option == 4:
            id = input("Insira o id do produto que deseja remover: ")
            item = new_cart.remove_item_by_id(id)
            if item is None:
                print("Item não encontrado!")
            else:
                print("Item removido: ")
                print(item)
        else:
            print("Encerrando programa...")
            menu.shutdown()
        

init_cart()
