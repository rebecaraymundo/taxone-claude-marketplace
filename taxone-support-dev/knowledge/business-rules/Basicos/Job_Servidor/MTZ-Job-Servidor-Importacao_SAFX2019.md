# MTZ-Job-Servidor-Importacao_SAFX2019

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX2019.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAF2019

Tabela de Códigos DARF

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS9754

Elenilson Coutinho

Alteração da tabela SAFX2019 para atendimento ao REINF Registro 2070\. 

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

Estrutura da tabela SAFX2019 🡪 vide manual de layout

A manutenção desta tabela é feita no Módulo Básicos, menu Manutenção 🡪 Códigos DARF

Sobre as mensagens de erro:

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS9754

__RN01__

__Campo REINF__

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>Quando for um indicador inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

O Indicador de incidencia no REINF deve ser <S> ou <N>

MFS9754

__RN02__

__Campo Classificação Rendimentos__

Quando for um indicador inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

O Indicador de classificacao do Codigo do Rendimento no REINF deve ser <1> ou <2>

MFS9754

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

