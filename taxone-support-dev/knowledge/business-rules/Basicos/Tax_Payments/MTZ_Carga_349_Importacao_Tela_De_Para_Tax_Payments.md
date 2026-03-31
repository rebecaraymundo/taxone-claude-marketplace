# MTZ_Carga_349_ Importacao_Tela_De_Para_Tax_Payments

- **Fonte:** MTZ_Carga_349_ Importacao_Tela_De_Para_Tax_Payments.docx
- **Modificado:** 2026-03-18
- **Tamanho:** 71 KB

---

THOMSON REUTERS

 TAX PAYMENTS – IMPORTAÇÃO E EXPORTAÇÃO\- SAFX349 \(Tela de DE/PARA – Tax Payments\) 

TAXONE >> Básicos > Data Warehouse > Manutenção > Guias de Pagamento >>Tela De/Para – Tax Payments

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

ADO\- 1068055

Beatriz Tie Terada, Millys Lopes

Definição das regras de importação da SAFX349

# <a id="_Toc502934853"></a><a id="_Hlk210244861"></a>Introdução

A SAFX 349 irá importar os dados para tela __De/Para__ que permita ao usuário importação manualmente os códigos de __Empresa\.__  
Esses códigos serão utilizados para __sobrescrever__ \(reverter\) os códigos padrões atribuídos automaticamente pelo sistema, garantindo que a geração do DARF e do JSON utilize exatamente os códigos corretos em situações excepcionais ou personalizadas\.

__Localização:__

- __Agrupamentos: Básico >> Job Servidor__
- __   Menu: __Carga__ __> Programação > Execução 
- __                        __Importação > Programação > Execução      
-                                      Importação batch > Programação > Execução 

__\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX349 conforme o Manual de Layout, o que facilita a consulta\. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)\.__

Procedimentos para a Importação da SAFX349:

A importação da SAFX349 deve seguir as seguintes premissas de negócio e comportamentos:

- Caso COD\_EMPRESA\_ERP seja informado, o sistema deverá sobrescrever o código padrão da empresa pelo valor importado

__Resultado da Importação:__

Caso a importação seja realizada com sucesso, os dados serão preenchidos nas seguintes telas:

- __Tax One > Básico > Data Warehouse > Manutenção > Guias de Pagamentos > Tela De/Para – Tax Payments__
- __Menu: Acesso Principal >> Tela De/Para – Tax Payments__

__Resultado da Exportação:__

- O usuário poderá exportar os dados e visualizar as informações já exportadas

<a id="_Toc502934855"></a>Regra Geral para validação

1º \) Consistências Básicas:

- Campos Data inválidos
- Campos Obrigatórios
- Campos Numéricos inválidos
- Campo Estabelecimento – Vide regra RN01
- Campo Estabelecimento no ERP – Vide regra RN02

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__ADO__

RN00

__Índice__

__Nome do Campo__

__Descrição__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

1

COD\_EMPRESA

Campo destinado ao código da Empresa\. Vide regra RN00\.

A

003

SIM

\(\*\)

2

COD\_EMPRESA\_ERP

Campo destinado ao armazenamento do código da Empresa conforme registrado no ERP digitado pelo usuário\. 

A

008

SIM

NÃO

 

ADO\- 1068055

RN00\.1

__Campos Obrigatório não preenchido__

Se algum campo de preenchimento obrigatório não estiver preenchido, exibir a mensagem “Campo <<Nome do campo>> deve ser preenchido”

ADO\- 1068055

__RN01__

__Campo 01 \- Código da Empresa__

 

__Tabela: SAFX349__

__Item: __01

__Nome do Campo: __COD\_EMPRESA

__Descrição: __Campo destinado ao código da Empresa\. Vide regra RN00

__Tipo:__ A

__Tamanho: __003

__Campo Obrigatório__

__Chave Primária__

__Comentário:__

Informar o Código da Empresa atual existente no Tax One

Exibir a mensagem da TFIX 22 CÓDIGO 90001

ADO\- 1068055

__RN02__

__Campo 02 \- Código da Empresa no ERP__

__Tabela: SAFX349__

__Item: __02

__Nome do Campo: __COD\_EMPRESA\_ERP

__Descrição: __Campo destinado ao armazenamento do código da Empresa conforme registrado no ERP digitado pelo usuário\.

__Tipo:__ A

__Tamanho: __008

__Campo Obrigatório__

__Comentário:__

Armazena o código da Empresa conforme registrado no ERP digitado pelo usuário\. Utilizado como referência padrão de origem do dado\. RN02

Exibir a mensagem da TFIX 22 CÓDIGO 913360

ADO\- 1068055

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

