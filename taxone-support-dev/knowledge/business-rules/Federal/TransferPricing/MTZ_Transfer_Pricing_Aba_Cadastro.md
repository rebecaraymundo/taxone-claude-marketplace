# MTZ_Transfer_Pricing_Aba_Cadastro

- **Fonte:** MTZ_Transfer_Pricing_Aba_Cadastro.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 33 KB

---

# Módulo \- Transfer Pricing \- Lei 12\.715/12

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3645

Conversão da Medida Provisória Nº 563/12 na* *lei 12\.715/12  \- “Plano Brasil Maior”

Esse documento contempla as regras definidas para atendimento a Lei 12\.715/12 do produto Transfer Pricing/Mastersaf\.

MFS\-651

Atualização Legal, implementação do Método PCI de acordo com as regras estabelecidas pela IN 1\.312/12

Esse documento contempla as regras definidas para o Cálculo do Preço Praticado para atendimento a Lei 12\.715/12 e IN 1\.312/2012 do produto Transfer Pricing/Mastersaf\.

OS4098

Alteração do Produto 

Criação de Parâmetro para cálculo do Custo Médio Ponderado do Preço Parâmetro

MFS7787

Alteração do produto

Criação do campo "Utilizar preço independente relativo à operação do ano\-calendário anterior"

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Aba __Cadastro__ 🡪 link \(menu\) Produto

Campo: __“Calcula PRL Rev Lei 12\.715/12 \*”__ \- Caso esta opção seja marcada o sistema irá gerar para o produto a monitoração da importação para o método PRL Revenda instituído conforme a Lei 12\.715/12\.

OS3645

__RN01__

Aba __Cadastro__ 🡪 link \(menu\) Produto

Campo: __“Calcula PRL Prod Lei 12\.715/12 \*”__ \- Caso esta opção seja marcada o sistema irá gerar para o produto a monitoração da importação para o método PRL Produção instituído conforme a Lei 12\.715/12\.

OS3645

__RN02__

Campo: “__Margem \(PRL Lei 12\.715/12\*\)__” \- Margem de Lucro prevê para utilização no cálculo do preço Parâmetro de acordo com o método PRL instituído na Lei 12\.715/12\.

Obs: Se o campo da RN00 estiver marcado, este campo torna\-se obrigatório e o usuário deve informar 40%, 30% ou 20% de acordo com o setor de atividade econômica, conforme instrui o parágrafo 12 do Artigo 18 Da lei 12\.715/12\.

OS3645

__RN03__

Aba Cadastro 🡪 Parâmetros de Cálculo \(Seleciona a Empresa\)

Campos para Alteração de Parâmetros de cálculo relacionados à apuração do Custo para o Método PCI:

Custo do Produto;

Imposto de Importação;

Frete;

Seguro;

Outras Despesas;

O Processamento dos campos mencionados deverá seguir a mesma regra dos métodos já existentes;

__Campo Tipo Custo Médio Ponderado:__

Tipo: DropDown

Obrigatório: Sim

Default: “Calcular Custo Médio Ponderado a partir do Custo Contábil”

Irá listar as opções “Calcular Custo Médio Ponderado a partir do Custo Contábil” e “Utilizar Cadastro de Custo Médio Ponderado”

MFS\-651/

OS4098

__RN04__

Aba Cadastro 🡪 link \(menu\) Produto

Campo: “Calcula PCI \*” \- Caso esta opção seja marcada o sistema irá gerar para o produto a monitoração da importação para o método Preço sob Cotação na Importação conforme determina a IN 1\.312 de 28/12/2012

MFS\-651

__RN05__

Aba Cadastro 🡪 link \(menu\) Produto

Campo: “Calcula PECEX\*” \- Caso esta opção seja marcada o sistema irá gerar para o produto a monitoração da exportação para o método “Preço sob Cotação na Exportação”  conforme determina a IN 1\.312 de 28/12/2012\.

MFS\-651

__RN06__

Aba Cadastro 🡪 link \(menu\) Parâmetros de Calculo \- Método PIC

Campo "Utilizar preço independente relativo à operação do ano\-calendário anterior"

Tipo: Dropdown

Valores: Sim/Não

Default: “Não”

Caso selecionada a opção “Sim“ só deverá ser utilizado o preço independente relativo a operação do ano\-calendário anterior se não houver notas de entrada ou DI´s de pessoas não vinculadas ou valores de terceiros para o produto a ser calculado\.

Obs: Campo deverá ser criado abaixo do campo “Custos Considerados no Cálculo”\.

MFS\-7787

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

