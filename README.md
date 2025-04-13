# Projeto Mercado

## Descrição
O **Projeto Mercado** é uma aplicação interativa desenvolvida em Python que simula o funcionamento de um sistema de compras em um mercado. O programa permite que os usuários visualizem uma lista de produtos, adicionem itens ao carrinho, utilizem cupons de desconto e escolham diferentes formas de pagamento, incluindo parcelamento.

## Funcionalidades
- **Listagem de Produtos**: Exibe uma lista de produtos disponíveis com seus respectivos preços.
- **Carrinho de Compras**: Permite adicionar produtos ao carrinho e visualizar o total acumulado.
- **Cupons de Desconto**: Aceita cupons válidos para aplicar descontos no valor total da compra.
- **Formas de Pagamento**:
  - À vista (dinheiro ou cheque) com 10% de desconto.
  - À vista no cartão com 5% de desconto.
  - Parcelamento em até 2x sem juros.
  - Parcelamento em 3x ou mais no cartão com 20% de juros.
- **Interface Interativa**: O programa utiliza mensagens coloridas para guiar o usuário durante o processo de compra.

## Como Funciona
1. O programa inicia com uma mensagem de boas-vindas e exibe um manual com instruções.
2. O usuário pode digitar comandos como:
   - `lista`: Para visualizar a lista de produtos e preços.
   - Nome do produto: Para verificar o preço e adicionar ao carrinho.
   - `total`: Para visualizar o total acumulado e os itens no carrinho.
   - `cupom`: Para inserir um código de desconto.
   - `0`: Para finalizar a compra.
3. Após finalizar a compra, o programa solicita a escolha da forma de pagamento e calcula o valor final com base nas condições aplicáveis.

## Tecnologias Utilizadas
- **Linguagem de Programação**: Python
- **Recursos Utilizados**: Estruturas de controle, manipulação de tuplas, entrada e saída de dados interativos.

## Como Executar o Projeto
1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/Projeto-Mercado.git
   ```
3. Acesse o diretório do projeto:
   ```bash
   cd Projeto-Mercado
   ```
4. Execute o programa:
   ```bash
   python code_1.py
   ```

## Exemplo de Uso
- Visualizar a lista de produtos:
  ```
  lista
  ```
- Adicionar um produto ao carrinho:
  ```
  açúcar
  ```
- Aplicar um cupom de desconto:
  ```
  cupom
  ```
- Finalizar a compra:
  ```
  0
  ```

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).