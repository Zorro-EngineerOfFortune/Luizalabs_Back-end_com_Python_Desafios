# Luizalabs_Back-end_com_Python_Desafios

Repo armazena o código e projetos feitos como o parte do curso **Luizalabs Back-end com Python**

## Table of Contents:

| Lab # | Solution File(s) | Objective e conceitos principais |
|---|---|---|
| 1 | Desafio_1.py | <ol><li>*Estrutura de Funções*: Uso de várias funções para modularizar o código, tornando-o mais legível e fácil de manter.</li><li>*Argumentos de Função*: Uso de diferentes tipos de passagem de argumentos (posicionais, keyword-only, e positional-only), o que é um excelente exercício.</li><li>*Estruturas de Controle*: Uso de if/elif/else para validações e o loop while True para o menu principal.</li><li>*Estruturas de Dados*: Uso de tuples para usuários_tuple e contas_tuple com o objetivo de "evitar mudança de dados", o que é uma escolha conceitual interessante (embora a implementação de fato use concatenação de tuples para "adicionar" dados, criando novas tuples).</li></ol> |
| 2 | Desafio_2.py | <ol><li>Estrutura de Classes e Herança: Uso de classes (Cliente, Conta, Historico) e herança (PessoaFisica, ContaCorrente) para modelar o mundo real, reutilizar código e impor hierarquias.</li><li>Classes Abstratas (ABC): Uso de Transacao(ABC) para definir uma interface obrigatória (@abstractmethod) para todas as operações, garantindo que Saque e Deposito sigam um padrão.</li><li>Encapsulamento e Propriedades: Uso de atributos internos (_saldo, _historico) e decorators @property para controlar o acesso aos dados (dados protegidos e propriedades somente leitura).</li><li>Polimorfismo: O método sacar é sobrescrito em ContaCorrente para adicionar lógica de negócio (limite de saques e limite de crédito) antes de chamar a implementação da classe pai (Conta).</li></ol> |
|  |  |  |
|  |  |  |
|  |  |  |
