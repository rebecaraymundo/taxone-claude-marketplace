# MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_Tabelas SAFX_C180_C181_C185_C186_C380_C480

- **Fonte:** MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_Tabelas SAFX_C180_C181_C185_C186_C380_C480.docx
- **Modificado:** 2021-05-17
- **Tamanho:** 87 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 087/2020\) 

Atualização das Tabelas SAFX \(C180, C181, C185, C186, C380, C480\) 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\),

 itens: Geração 🡪 IN\-RE 087/20 🡪 Transferência dos Movimentos para EFD Fiscal 

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS48753__

Liliane Videira Assaf

Criação da funcionalidade\.

Não estamos considerando Cupom Fiscal nesta entrega\.

22/12/2020 

__MFS65137__

Liliane Videira Assaf

Tratamento dos Cupom Fiscal \(Mod\. 02, 2D e 60\) para geração do registro C480 do Sped Fiscal\.

Os cupons devem ser lidos da tabela EST\_ST\_RS\_ECF e gravados na tabela X297\_INF\_COMP\_ST\_CUPOM\_ECF, de onde o registro C480 é gerado no Sped Fiscal\.

13/05/2021

Sumário

[1\.	Introdução	1](#_Toc62065758)

[2\.	Limpeza das tabelas definitivas relacionadas as SAFX	1](#_Toc62065759)

[3\.	Recuperação dos Dados e Processamento	1](#_Toc62065760)

[3\.1 – Recuperação dos Movimentos de Entrada e Gravação do C180	1](#_Toc62065761)

[3\.2 – Recuperação dos Movimentos de Saída e Gravação do C185	1](#_Toc62065762)

[3\.3 – Recuperação dos Movimentos de Saída e Gravação do C380	1](#_Toc62065763)

[3\.4 – Recuperação da Movimentação de Saída por Cupons Fiscais e Gravação do C480	1](#_Toc62065764)

[3\.5 – Recuperação dos Movimentos de Devolução de Saídas e Gravação do C181	1](#_Toc62065765)

[3\.6 – Recuperação dos Movimentos de Devolução de Entradas e Gravação do C186	1](#_Toc62065766)

# <a id="_Toc62065758"></a>Introdução 

O objetivo desse documento é definir a geração dos registros C180, C181, C185, C186, C380 e C480\.

Nessa rotina os registros gerados pelo processo de “Geração dos Movimentos” nas tabelas específicas do módulo são lidos e gravados nas tabelas definitivas relacionadas as “SAFX”, base para geração dos registros do Sped Fiscal\. 

__Tabelas Específicas da Geração do Movimento__

__Tabelas definitivas relacionadas as SAFX__

__Registro do SPED FISCAL__

EST\_ST\_RS\_NF\_ENT

x296\_info\_compl\_st\_itens\_merc

C180

EST\_ST\_RS\_NF\_DEV\_ENT

X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV

C186

EST\_ST\_RS\_NF\_DEV\_SAI

X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV

C181

EST\_ST\_RS\_NF\_SAI

x296\_info\_compl\_st\_itens\_merc

C185

EST\_ST\_RS\_NF\_SAI

x296\_info\_compl\_st\_itens\_merc

C380

EST\_ST\_RS\_ECF

X297\_INF\_COMP\_ST\_CUPOM\_ECF

C480 \[__MFS65137\]__

# <a id="_Toc62065759"></a>Limpeza das tabelas definitivas relacionadas as SAFX

No início do processamento é necessário excluir os registros das tabelas x296\_info\_compl\_st\_itens\_merc, X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV, \[__MFS65137\] __X297\_INF\_COMP\_ST\_CUPOM\_ECF com os seguintes critérios:

\- Empresa = de login do Manager

\- Estab = selecionado na tela de geração;

\- Data compreendida no período informado na tela de geração

\- Ind\_gravação = '0', '6','7','8'\.

__Sobre o campo IND\_GRAVAÇÃO__:

O ind\_gravação informa a origem do registro nas tabelas definitivas \(X\) que possuem importação por SAFX\. 

IND\_GRAVACAO:

Valores padrão do campo \(tabelas de importação \):

1\.  Incluído por Importação

2\.  Atualizado por Importação

3\.  Incluído por Importação / Atualizado por Digitação

4\.  Incluído por Digitação

5\.  Incluído por Digitação / Atualizado por Digitação

6\.  Gerado pelo Sistema

7\.  Gerado pelo Sistema  / Atualizado por Digitação

8\. Gerado pelo Sistema  / Atualizado por Importação

O valor 8 foi criado na OS2388\-AA, A4, e somente é considerado nas importações das SAFX112 e SAFX113\.

9\. Atualizado pelo Sistema

# <a id="_Toc350763252"></a><a id="_Toc62065760"></a>Recuperação dos Dados e Processamento

## <a id="_2.1_–_Recuperação"></a><a id="_Toc62065761"></a>3\.1 – Recuperação dos Movimentos de Entrada e Gravação do C180

Lê tabela EST\_ST\_RS\_NF\_ENT com os seguintes critérios:

\- Empresa = de login do Manager

\- Estab = selecionado na tela de geração;

\- Data compreendida no período informado na tela de geração

Gravar a tabela x296\_info\_compl\_st\_itens\_merc com IND\_GRAVACAO = ‘6’;

Caso registro já exista na tabela x296\_info\_compl\_st\_itens\_merc \(caso que foi incluído via digitação ou importação\) então:

Gravar a seguinte mensagem de aviso no log:

*“Registro C180: Registro de Movimento de Entrada, incluído via importação/manutenção da SAFX296, foi atualizado pelo processamento da geração\. Os dados originalmente inseridos foram desprezados\.”*

Exibir dados para identificação do registro \(dados da chave\);

Contabilizar o número de registros lidos, incluídos e atualizados para o C180 a ser demonstrado no relatório de “Resumo Registros Gerados”, especificado no “*MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_EFD Fiscal\.docx*”\.

## <a id="_Toc62065762"></a>3\.2 – Recuperação dos Movimentos de Saída e Gravação do C185

Lê tabela EST\_ST\_RS\_NF\_SAI com os seguintes critérios:

\- Empresa = de login do Manager

\- Estab = selecionado na tela de geração;

\- Data compreendida no período informado na tela de geração

\- Código do Modelo da nota = 01, 1B, 04, 55, 65

Gravar a tabela x296\_info\_compl\_st\_itens\_merc com IND\_GRAVACAO = ‘6’;

Caso registro já exista na tabela x296\_info\_compl\_st\_itens\_merc \(caso que foi incluído via digitação ou importação\) então:

Gravar a seguinte mensagem de aviso no log:

*“Registro C185: Registro de Movimento de Saída, incluído via importação/manutenção da SAFX296, foi atualizado pelo processamento da geração\. Os dados originalmente inseridos foram desprezados\.”*

Exibir dados para identificação do registro \(dados da chave\);

Contabilizar o número de registros lidos, incluídos e atualizados para o C185 a ser demonstrado no relatório de “Resumo Registros Gerados”, especificado no “*MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_EFD Fiscal\.docx*”\.

## <a id="_Toc62065763"></a>3\.3 – Recuperação dos Movimentos de Saída e Gravação do C380

Lê tabela EST\_ST\_RS\_NF\_SAI com os seguintes critérios:

\- Empresa = de login do Manager

\- Estab = selecionado na tela de geração;

\- Data compreendida no período informado na tela de geração

\- Código do Modelo da nota = 02

Gravar a tabela x296\_info\_compl\_st\_itens\_merc com IND\_GRAVACAO = ‘6’;

Caso registro já exista na tabela x296\_info\_compl\_st\_itens\_merc \(caso que foi incluído via digitação ou importação\) então:

Gravar a seguinte mensagem de aviso no log:

*“Registro C380: Registro de Movimento de Saída, incluído via importação/manutenção da SAFX296, foi atualizado pelo processamento da geração\. Os dados originalmente inseridos foram desprezados\.”*

Exibir dados para identificação do registro \(dados da chave\);

Contabilizar o número de registros lidos, incluídos e atualizados para o C380 a ser demonstrado no relatório de “Resumo Registros Gerados”, especificado no “*MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_EFD Fiscal\.docx*”\.

\[__MFS65137\]__

## <a id="_2.2_–_Recuperação"></a><a id="_Toc62065764"></a>3\.4 – Recuperação da Movimentação de Saída por Cupons Fiscais e Gravação do C480 

Lê tabela EST\_ST\_RS\_ECF com os seguintes critérios:

\- Empresa = de login do Manager

\- Estab = selecionado na tela de geração;

\- Data compreendida no período informado na tela de geração;

Gravar a tabela X297\_INF\_COMP\_ST\_CUPOM\_ECF com IND\_GRAVACAO = ‘6’;

Caso registro já exista na tabela X297\_INF\_COMP\_ST\_CUPOM\_ECF \(caso que foi incluído via digitação ou importação\) então:

Gravar a seguinte mensagem de aviso no log:

*“Registro C480: Registro de Movimento de Cupom Fiscal, incluído via importação/manutenção da SAFX297, foi atualizado pelo processamento da geração\. Os dados originalmente inseridos foram desprezados\.”*

Exibir dados para identificação do registro \(dados da chave\);

Contabilizar o número de registros lidos, incluídos e atualizados para o C480 a ser demonstrado no relatório de “Resumo Registros Gerados”, especificado no “*MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_EFD Fiscal\.docx*”\.

## <a id="_Toc62065765"></a>3\.5 – Recuperação dos Movimentos de Devolução de Saídas e Gravação do C181

Lê tabela EST\_ST\_RS\_NF\_DEV\_SAI com os seguintes critérios:

\- Empresa = de login do Manager

\- Estab = selecionado na tela de geração;

\- Data compreendida no período informado na tela de geração

Gravar a tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV com IND\_GRAVACAO = ‘6’;

Caso registro já exista na tabela x296\_info\_compl\_st\_itens\_merc \(caso que foi incluído via digitação ou importação\) então:

Gravar a seguinte mensagem de aviso no log:

*“Registro C181: Registro de Movimento de Devolução de Saída, incluído via importação/manutenção da SAFX308, foi atualizado pelo processamento da geração\. Os dados originalmente inseridos foram desprezados\.”*

Exibir dados para identificação do registro \(dados da chave\);

Contabilizar o número de registros lidos, incluídos e atualizados para o C181 a ser demonstrado no relatório de “Resumo Registros Gerados”, especificado no “*MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_EFD Fiscal\.docx*”\.\.

## <a id="_Toc62065766"></a>3\.6 – Recuperação dos Movimentos de Devolução de Entradas e Gravação do C186

Lê tabela EST\_ST\_RS\_NF\_DEV\_ENT com os seguintes critérios:

\- Empresa = de login do Manager

\- Estab = selecionado na tela de geração;

\- Data compreendida no período informado na tela de geração

Gravar a tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV com IND\_GRAVACAO = ‘6’;

Caso registro já exista na tabela x296\_info\_compl\_st\_itens\_merc \(caso que foi incluído via digitação ou importação\) então:

Gravar a seguinte mensagem de aviso no log:

*“Registro C186: Registro de Movimento de Devolução de Entrada, incluído via importação/manutenção da SAFX308, foi atualizado pelo processamento da geração\. Os dados originalmente inseridos foram desprezados\.”*

Exibir dados para identificação do registro \(dados da chave\);

Contabilizar o número de registros lidos, incluídos e atualizados para o C186 a ser demonstrado no relatório de “Resumo Registros Gerados”, especificado no “*MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_EFD Fiscal\.docx*”\.

= = = = = =

 

