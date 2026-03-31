# MTZ_Tela_Manutenção_Bloco P_Ajustes_Contribuicao_Previdenciaria_Apurada_sobre_a_Receita_Bruta_P210

- **Fonte:** MTZ_Tela_Manutenção_Bloco P_Ajustes_Contribuicao_Previdenciaria_Apurada_sobre_a_Receita_Bruta_P210.docx
- **Modificado:** 2020-07-28
- **Tamanho:** 33 KB

---

    

# EFD \- Contribuições \- Tela \-Ajustes Contribuicao Previdenciaria Apurada sobre a Receita Bruta \- P210  

__Localização:__ 

Módulo: SPED >> EFD\-Escrituração Fiscal Digital das Contribuições

Menu: Manutenção >> Registro do Bloco P >> Ajuste da Contribuição Previdenciária Apurada Sobre a Receita Bruta \(P210\)

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3584\-DW1

Criação do documento

Tela –Ajustes Contribuicao Previdenciaria Apurada sobre a Receita Bruta \- P210 

27/04/2012

OS4569

Atualização do documento

Inclusão de novos domínios para o campo Código do Ajuste

19/07/2014

OS4316\-B

Marcos G\. de Paula

Criação do campo Código da SCP\.

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN01__

Criar no Módulo: SPED 🡪 EFD – Escrituração Fiscal Digital – PIS/PASEP/COFINS, Menu: Manutenção 🡪Registro Bloco P ,  a tela Ajustes da Contribuição Previdenciária Apurada Sobre a Receita Bruta \(P210\)

OS3584\-DW1

__RN02__

__Código da Receita:__

Valores Válidos:

298501 – Empresas Prestadoras de Serviço de Tecnologia da Informação – TI e Tecnologia da Informação e Comunicação – TCI

298502 	\- Contribuicao Previdenciaria Sobre Receita Bruta \- Empresas Prestadoras de Servicos TI e TIC  \- 13º Salario

299101 \- Contribuição Previdenciária sobre a Receita Bruta – Demais

299102	\-Contribuicao Previdenciaria Sobre Receita Bruta \- Demais  13º Salario 

Atenção: Este campo deve estar cadastrado na dwt\_cod\_receita

OS3584\-DW1

__RN03__

__Tipo do Ajuste:__

Valores válidos:

0 – Ajuste de Redução

1 – Ajuste de Acrescimo

OS3584\-DW1

__RN04__

__Código do Ajuste:__

Valores válidos:

01 – Ajuste Oriundo de Ação Judicial

02 – Ajuste Oriundo de Processo Administrativo

03 – Ajuste Oriundo da Legislação Tributária

04 – Ajuste Oriundo Especificamente do RTT

05 – Ajuste Oriundo de Outras Situações

06 – Estorno

07 – Ajuste da CPRB: Adoção Regime Caixa

08 – Ajuste da CPRB: Diferimento de Valores a Recolher no Período

09 – Ajuste da CPRB: Adição de Valores Diferidos em Período\(s\) Anterior\(es\)

OS3584\-DW1

OS4569

__RN05__

__Campos Chaves: Empresa, __Estabelecimento, Mês/Ano Apuração, Período Referencia, Código da Receita, Tipo do Ajuste, Código do Ajuste e Nº do Processo/Documento/Ato Concessório Vinculado\.

OS3584\-DW1

__RN06__

__Código da SCP:__

Incluir na tela o campo Código da SCP no formato padrão do Mastersaf DW com pasta de seleção e campo de texto para digitação do código\. Deverá acessar as informações da tabela SAFX2057\.

Este campo deverá ser chave, mas não obrigatório\.

OS4316\-B

