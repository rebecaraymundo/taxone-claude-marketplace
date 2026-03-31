# MTZ_Tela_Doc_Fiscal_de_Servico_TAXONE

- **Fonte:** MTZ_Tela_Doc_Fiscal_de_Servico_TAXONE.docx
- **Modificado:** 2026-02-24
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Tela Doc\. Fiscal de Mercadoria e Serviço

__Localização:__ Módulo: TAXONE > Básicos > Data Warehouse > Menu: Manutenção > Documento Fiscal > Doc\. Fiscal de Mercadoria e Serviço

__Atenção:__ Para o Produto DW temos outro documento para ser ajustado devido ao layout de tela\.  Considerar o arquivo “MTZ\-Basicos\-Documento\_de\_Item\_de\_Servico\-SAFX09”, no caminho \\Thomson Reuters Incorporated\\Requisitos \- Mastersaf DW TaxOne\\Documento\_Matriz\\Basicos\\MasterSAF\_DW\\

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

Alessandra Cristina Navatta e Roseval Lima

Alteração de Layout da Tela de Documento Fiscal de Serviço \(ajuste apenas no TAXONE\), com o objetivo de deixá\-la mais performática\. 

Atenção: Neste momento, não foram consideradas as regras dos campos de documento de mercadoria, pois o ajuste foi realizado apenas pela squad técnica, sem o acompanhamento funcional \(pela consultoria e ou requisito\)\. Quando planejado, será realizado a engenharia reversa da parte de mercadoria\.

Sumário

[1\.	Introdução	3](#_Toc89188058)

[2\.	Layout e Campos da Tela	3](#_Toc89188059)

[3\.	Regra dos Campos da Tela	3](#_Toc89188060)

# <a id="regras_campos"></a><a id="_Toc89188058"></a><a id="_Toc350763252"></a>Introdução

O objetivo é ajustar o layout da tela de documentos fiscais \(Mercadoria e Serviço\), no produto TAXONE, a fim de torná\-la mais performática\.

Vale ressaltar que não houve nenhuma criação ou alteração de campo por esta nesta demanda\. 

Não houve ajuste nas interfaces das SAFX07, SAFX08 e SAFX09\.

Ressaltamos que as regras referentes aos campos de mercadoria, não foi escopo tratado pela demanda\.

# <a id="_Toc89188059"></a>Layout e Campos da Tela

__Localização da tela:__ Módulo: TAXONE > Básicos > Data Warehouse, Menu: Manutenção > Documento Fiscal > Novo Documento Fiscal > Doc\. Fiscal de Mercadoria e Serviço

# <a id="_Toc89188060"></a>Regra dos Campos da Tela

Considerar as informações da planilha ‘Aderência de Campos V2\.LSX’\.

__Tabela SAFX07__

A planilha SAFX07\_CAPA NOTA FISCAL \(existente no arquivo ‘Aderência de Campos V2\.LSX’\), contém todos os campos da SAFX07\. Seu respectivo campo na X07 está definido na coluna H\. Esses campos estão disponíveis em tela na aba indicada na coluna M ‘Menu ajustar para mantermos o padrão da 09’, considerando a respectiva ordenação conforme coluna \(L\)\. As regras dos campos estão localizadas na coluna I ’Regra/Descrição’\. A coluna Q ‘Mercadoria/Serviço’, indica que o campo será apresentado quando se tratar de nota de mercadoria e ou de serviço\. Caso a informação seja igual a ‘Mercadoria/Serviço’, o campo será apresentado nas notas, independente de sua classificação \(seja ela mercadoria ou serviço\)\.

__Tabela SAFX09__

A planilha SAFX09\_ITENS\_SERVIÇO \(existente no arquivo ‘Aderência de Campos V2\.LSX’\), contém todos os campos da SAFX09\. Seu respectivo campo na X09 está definido na coluna H\. Esses campos estão disponíveis em tela conforme colunas J ‘Menu’ e N ‘ABA’, considerando a respectiva ordenação conforme coluna L ‘Sequência de campos no mockup’\. As regras dos campos estão localizadas na coluna I ’Regra/Descrição’\. 

