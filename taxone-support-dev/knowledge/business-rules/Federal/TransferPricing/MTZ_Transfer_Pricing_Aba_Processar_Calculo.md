# MTZ_Transfer_Pricing_Aba_Processar_Calculo

- **Fonte:** MTZ_Transfer_Pricing_Aba_Processar_Calculo.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 33 KB

---

# Módulo \- Transfer Pricing \- Aba Processar Cálculo \- Lei 12\.715/12

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3645

Conversão da Medida Provisória Nº 563/12 na* *lei 12\.715/12  \- “Plano Brasil Maior”

Esse documento contempla as regras definidas para atendimento a Lei 12\.715/12 do produto Transfer Pricing/Mastersaf\.

MFS\-651

Atualização Legal, implementação dos Métodos PCI e PECEX de acordo com as regras estabelecidas pela IN 1\.312/12

Esse documento contempla as regras definidas para o Cálculo do Preço Praticado para atendimento a Lei 12\.715/12 e IN 1\.312/2012 do produto Transfer Pricing/Mastersaf\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Aba __Processar Cálculo__ 🡪 Tela Processos de Cálculo 

Campo ID: Este campo é de preenchimento automático pelo sistema

Campo Descrição: Definido pelo usuário 

ComboBox Tipo: Cálculo de Preços default

Após definida as opções acima, o sistema disponibilizará a visualização da __Lista de Processos de Cálculo __possibilitando a seleção do cálculo a ser executado\.

OS3645

__RN01__

Regras para__ Parâmetros do Processo__

Após selecionado o ID definido conforme RN00, o sistema ira apresentar os seguintes Campos/CheckBox/ComboBox/Botões:

“Empresa” 

“Produto Inicial” 

“Produto Final” 

“Gerar Fichas DIPJ” 

“Métodos de Importação” 

“Executar” 

OS3645

__RN02__

Combobox “__Empresa__” Deverá ser selecionado a empresa previamente cadastrada para qual se deseja a obtenção dos cálculos

OS3645

__RN03__

Para o parâmetro “__Produto Inicial e Produto Final__”

Campo: “Empresa ou estabelecimento” \(habilitado somente para pesquisa através do ComBox do lado direito da tela\)

Campo: “Código”   
  
Se preenchido: O sistema deverá ira executar o cálculo somente do Produto que contém o código informado, previamente cadastrado/Integrado\. 

  
Campo: “Descrição” \(habilitado somente para pesquisa através do ComBox do lado direito da tela\)

OS3645

__RN04__

ChekBox “__Gerar Fichas DIPJ”: __Opção sistema processar as informações para a opção “__Meio Magnético__” contido na aba “__Relatórios__”

OS3645

__RN05__

ChekBox “__Métodos de Importação__” Opções para o sistema processar os seguintes métodos de cálculo se selecionado:

PRL Rev LEI12\.715/12

PRL Prod LEI12\.715/12

PRL20

PRL60

CPL

PIC

PCI

OS3645

MFS\-651

__RN06__

ComboBox “__Executar__”: Opção para que o sistema efetue a geração do calculo\.

OS3645

__RN07__

ChekBox “__Métodos de Exportação__” Opções para o sistema processar os seguintes métodos de cálculo se selecionado:

CAP

PVEX

PVA

PVV

PECEX

MFS\-651

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

