# MTZ_GIAs_Geracao_dos_Valores_por_Classe

- **Fonte:** MTZ_GIAs_Geracao_dos_Valores_por_Classe.docx
- **Modificado:** 2025-02-06
- **Tamanho:** 67 KB

---

THOMSON REUTERS

Geração dos Valores da Apuração p/ Classe de Lançamento

 Módulo: Diversos

Localização por módulo:

\- Módulo __GIA\-MG__, menu Obrigações à DAPI à Geração à Valores da Apuração p/ Classe de Lançamento

Esta geração apura totais a partir dos lançamentos complementares da Apuração do ICMS e ICMS ST\. Estes valores são totalizados por Classe de Lançamentos, e os resultados são utilizados por diversos módulos das obrigações estaduais \(GIA’s, etc \.\.\.\)\.

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS7299

Atualização da DAPI\-MG para versão 8\.02

Criação de uma nova classe de lançamento \(980\) para atendimento à versão 8\.02 da DAPI\-MG\.

31/10/2016 \(criação do documento\)

MFS10024

Alteração na Totalização das Classes da DAPI\-MG 

Alteração para desconsiderar os lançamentos referentes à transferência dos valores da Apuração do DIFAL EC 87/15 para a Apuração do ICMS 

12/05/2017

Sumário

[1\.	Parâmetros da Tela	2](#_Toc465691638)

[2\.	Recuperação dos Dados e Processamento	3](#_Toc465691639)

[3\.	Gravação dos Dados	3](#_Toc465691640)

# <a id="_Toc465691638"></a>Parâmetros da Tela 

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

# <a id="_Toc350763252"></a><a id="_Toc465691639"></a>Recuperação dos Dados e Processamento

Classe__ __“__980\-DAPI – Outros Débitos de ST – Anexo VII – Item 77\.1__”:

MFS7299: A classe 980 foi criada na MFS7299 \(Nov/2016\) para atendimento ao campo 77\.1 da DAPI\-MG, versão 8\.02\.

Para apurar esta classe serão totalizados os lançamentos complementares da *Apuração do ICMS ST*, que tenham as seguintes características:

\- Empresa = empresa do login;

\- Estabelecimento = estabelecimento da geração;

\- Data da Apuração = Data final do período informado na tela da geração;

\- Código do Livro = “108” ou “165”\(ver Obs\);

\- Código de Operação = “002” ou “003” \(lançamentos de débitos\);

\- UF = MG;

\- Classe Lançamento = “980”;

Valor s ser totalizado: valor do lançamento \(*campo “Valor” da tela de manutenção dos lançamentos\) *

Obs: As empresas que geram a apuração centralizada por inscrição estadual única, têm que solicitar a *Geração dos Valores por Classe de Lançamento* para o estabelecimento centralizador\. Ou seja, na tela da geração, devem selecionar apenas o centralizador\. 

\- \- \- \- \- \- \- \- \- \-

MFS10024: Alteração feita para a DAPI\-MG, para desconsiderar os lançamentos referentes à transferência dos valores da Apuração do DIFAL EC 87/15 para a Apuração do ICMS, procedimento solicitado pela Sefaz MG\.

Na recuperação dos lançamentos da Apuração do ICMS \(seja do livro “108” ou do livro “165”\), serão *desconsiderados* os lançamentos que tenham os seguintes códigos de ajuste:

__MG000001__

Apuração do ICMS; Outros débitos; Débitos transferidos do Difal Origem \(E300=MG\) para apuração do ICMS OP \(E110\)

__MG020008__

Créditos transferidos do Difal Origem \(E300=MG\) para apuração do ICMS \(E110\) 

  

Observar que esta alteração se refere apenas à obrigação DAPI – MG, uma vez que os códigos de ajuste citados acima são de MG\. 

O objetivo da alteração é que os lançamentos de transferência dos valores da Apuração do DIFAL EC 87/15 p/a Apuração do ICMS não sejam demonstrados nos campos “71\-Outros Créditos” e “74\-Outros Débitos” da DAPI\. *Não* existem classes especificas para estes lançamentos, justamente pelo fato deles não aparecerem na DAPI\. No entanto, o objetivo da alteração é evitar erros, caso o usuário informe alguma classe genérica, equivocadamente, como por exemplo, a classe 578 ou 580\. 

# <a id="_Toc465691640"></a>Gravação dos Dados

__Classe “980\-DAPI – Outros Débitos de ST – Anexo VII – Item 77\.1”__

MFS7299: A classe 980 foi criada na MFS7299 \(Nov/2016\) para atendimento ao campo 77\.1 da DAPI\-MG, versão 8\.02\.

Caso o total apurado seja > zeros, serão gravdas as seguintes informações na tabela auxiliar utilizada nesta geração:

\(tabela EST\_GIA\_INFO\)

\- Código da Empresa – código da empresa

\- Código do Etabelecimento – código do estabelecimento

\- Data da Apuração – data final do período informado na tela da geração

\- Código da Classe – “980”

\- Valor \(VLR\_OUTROS\) – Total apurado 

\- Indicador Digitado/Calculado – “2” \(indicador de registros calculados\)

\- Identificador do estado – IDENT da UF de MG

\- Código do Amparo Legal – será gravado um caracter branco \(‘ ‘\)

\- Código do Sub\-Item do Amparo Legal – será gravado um caracter branco \(‘ ‘\)

Obs: Os campos do amparo legal e subitem do amparo fazem parte da chave, mas são gravados com um caracter branco dependendo do caso\.

= = = = = =

 

