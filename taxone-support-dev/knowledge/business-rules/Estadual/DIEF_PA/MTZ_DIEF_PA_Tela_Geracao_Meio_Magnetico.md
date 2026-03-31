# MTZ_DIEF_PA_Tela_Geracao_Meio_Magnetico

- **Fonte:** MTZ_DIEF_PA_Tela_Geracao_Meio_Magnetico.docx
- **Modificado:** 2024-01-03
- **Tamanho:** 62 KB

---

THOMSON REUTERS

Declaração de Informações Econômico\-Fiscais \- Pará

DIEF\-PA

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4726

Julyana Perrucini

Inclusão de novo parâmetro “Não Existem Operações com Cartão de C/D”\.

CH2209\_2015

Julyana Perrucini

Atualização da versão para 2015\.1\.0\.

CH2474\_2016

Lara Aline

Atualização da versão para 2016\.1\.0\.

CH8626\_2016

Julyana Perrucini

Atualização da versão para 2016\.1\.1\.

MFS9619

Andréa Rocha

Atualização da versão para 2017\.1\.0\.

MFS16502

João Henrique de Araujo

Atualização da versão para 2018\.1\.0\.

MFS24380

Liliane Assaf

Atualização da versão para 2019\.1\.0\.

MFS27731

Andréa Rocha

Atualização da versão para 2019\.1\.1\.

MFS34062

Andréa Rocha

Atualização da versão para 2020\.1\.0\.

MFS60069

Aline Melo

Atualização da versão para 2021\.1\.0 e 2021\.2\.0

MFS64422

Andréa Rocha

Inclusão de um parâmetro para definir o município usado para a geração do Anexo I, para aas notas fiscais de transporte sem itens de frete\.

MFS80389

Liliane Assaf

Atualização da versão para 2022\.1\.0 e 2022\.2\.0

MFS435431

Graciela Soares

Atualização da versão para 2023\.1\.0 e 2023\.2\.0

MFS599053

Graciela Soares

Atualização da versão para 2024\.1\.0 e 2023\.2\.0

Sumário

[1\.	Regras dos Campos	3](#_Toc409613928)

[2\.	Sugestão de Layout	4](#_Toc409613929)

# <a id="_Toc350763252"></a><a id="_Toc409613928"></a>Regras dos Campos 

__Localização da tela:__ Estadual\\ DIEF\-PA\\ Obrigações\\ Geração do Meio Magnético

__Título da tela: __Declaração de Informações Econômico\-Fiscais \- Pará

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Não Existem Operações com Cartão de C/D

Texto

N

S

Formato: 

Check box

Default: Habilitado

Permitir ao usuário marcar a opção que servirá para não gerar o Registro Tipo 88 \- Subtipo 33 no período em casos em que não houver movimentações ou se não for obrigatório para o contribuinte\.

__Tratamento:__

- Esse campo deve ser habilitado a partir da versão 2011\.1\.1, ou seja, quando essa versão for selecionada no campo Versão da tela de geração do meio magnético, para as versões anteriores manter desabilitado\.

OS4726

Versão

Texto

S

S

Formato: 

Combo box

Default: Habilitado

Permitir o usuário selecionar a opção de versão da DIEF que está em vigor considerando as versões anteriores para retificação\.

__\[ALTERADA\-CH2209\_2015/ CH2474\_2016/CH8626\_2016/ MFS9619\]__

__Conteúdo:__

3\.01 \(2003\)

2005\.3\.0 \- 2006\.1\.0

2007\.1\.1

2008 1\.0

2009 1\.1

2010\.1\.2

2010 1\.3

2011\.1\.1

2012\.1\.1

2013\.1\.0

2014\.1\.0

2015\.1\.0

2016\.1\.0

2016\.1\.1

2017\.1\.0

2018\.1\.0

2019\.1\.0

2019\.1\.1

2020\.1\.0

2021\.1\.0

2021\.2\.0

2022\.1\.0

2022\.2\.0

2023\.1\.0

2023\.2\.0

2024\.1\.0

2024\.2\.0

CH2209\_2015

CH2474\_2016

CH8626\_2016

MFS9619

MFS16502

MFS24380

MFS27731

MFS34062

MFS60069

MFS80389

MFS435431

MFS599053

Considerar Município Origem – NF Transporte \(Anexo I\)

Texto

N

N

Formato: 

Check box

Default: Habilitado

Permitir ao usuário marcar a opção que servirá para selecionar qual o município que será usado para gerar o Anexo I\.

__Tratamento:__

Esse campo só deve ser habilitado para a seleção quando o campo “Gerar Anexo I \(Anual\) – Serviços e Outros” estiver marcado\. Neste caso, deve vir desmarcado por default\.

MFS64422

