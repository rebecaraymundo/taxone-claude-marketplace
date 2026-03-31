# MTZ-LAIPI-Calculo-Materia-Prima-Devolucoes

- **Fonte:** MTZ-LAIPI-Calculo-Materia-Prima-Devolucoes.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Módulo Lançamentos Automáticos do IPI

Cálculo do Lançamento “Matérias Primas referente às Devoluções”

__Localização__: Menu Federal, módulo Lançamentos Automáticos do IPI”, menu Lançamentos 🡪 Cálculo dos Lançamentos 

Nesse item de menu são calculados todos os lançamentos automáticos gerados neste módulo\. Este documento é específico do lançamento “__Matérias Primas referente às Devoluções__”\.

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS17499__

<a id="OLE_LINK12"></a><a id="OLE_LINK13"></a><a id="OLE_LINK14"></a>Alteração do lançamento para gerar as informações dos documentos fiscais vinculados\.

<a id="OLE_LINK15"></a><a id="OLE_LINK19"></a>Alteração no cálculo do lançamento para passar a gerar as informações dos documentos fiscais vinculados\. Estas informações serão utilizadas na geração do Sped Fiscal, registro E531\. 

25/04/2018 

\(criação do documento\)

Sumário

[1\.	Parâmetros da Tela	2](#_Toc501011070)

[2\.	Recuperação dos Dados e Processamento	2](#_Toc501011071)

[3\.	Gravação dos Dados	3](#_Toc501011072)

# <a id="_Toc501011070"></a>Parâmetros da Tela 

# <a id="_Toc350763252"></a><a id="_Toc501011071"></a>Recuperação dos Dados e Processamento

Origem dos dados: \- Documentos Fiscais \(SAFX07/SAFX08\);

                               \- Tabela dos Códigos Fiscais \(SAFX2012\);

                               \- Parametrização “Lançamentos de Estornos” \(menu Parâmetros > Lançamentos de Estornos\);

Para cada estabelecimento selecionado em tela é gerado um lançamento\.

O valor do lançamento é calculado a partir da totalização do campo “VLR\_OUTROS\_IPI” de todos os itens das notas fiscais que atendam às condições abaixo\.

\- Itens de notas fiscais do estabelecimento em questão;

\- Itens de notas fiscais com data fiscal no período solicitado em tela;

\- Itens de notas fiscais de saída;

\- Itens de notas fiscais não canceladas;

\- Itens cujo CFOP tenha o campo IND\_IPI\_EST\_CRED da X2012 = “S” 

Valor do item totalizado: campo VLR\_OUTROS\_IPI

<a id="OLE_LINK26"></a>Alteração __MFS17499__: O cálculo deste lançamento foi alterado para passar a gerar as informações de identificação de todos os itens de nota fiscal considerados na totalização de cada lançamento\. 

Estas informações dos itens que compõem cada lançamento, ficarão armazenadas numa tabela “filha” da FDT\_LANCTO\_P8, e darão origem a janela “*Documentos Fiscais Vinculados*” da tela de manutenção dos lançamentos complementares da Apuração do IPI, e serão utilizadas posteriormente na geração do Sped Fiscal, registro E531\.

# <a id="_Toc501011072"></a>Gravação dos Dados

O valor do lançamento calculado para cada estabelecimento é gravado na tabela FDT\_LANCTO\_P8\.

Alteração __MFS17499__: As informações de identificação de todos os itens que originaram cada lançamento, serão armazenadas numa tabela “filha” da FDT\_LANCTO\_P8\.

As informações de cada item gravadas na tabela são as seguintes:

	

     \- Dados da chave de identificação da tabela “mãe” \(FDT\_LANCTO\_P8\);

     \- Dados da chave de identificação do item do documento fiscal;

     \- Número do item do documento fiscal;

     \- Valor do ajuste corresponde ao item __\(\*\)__;

__\(\*\)__ O valor do ajuste correspondente a cada item será exatamente o valor do campo VLR\_OUTROS\_IPI, já que este é o valor utilizado na totalização dos itens para compor o lançamento\. 

= = = = = =

 

