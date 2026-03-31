# MTZ-Job-Servidor-Importacao_SAFX250

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX250.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 70 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX250

Tabela do Demonstrativo de Pagamento dos Autônomos – Outros Vínculos do Trabalhador

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS14409

Criação da SAFX250 

Criação da SAFX250 para a importação dos dados sobre os outros vínculos trabalhistas dos autônomos, para a geração do eSocial\.

01/12/2017

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX250__ 🡪 vide manual de layout

A SAFX250 foi criada na __MFS14409__, para a importação dos dados sobre outros vínculos trabalhistas dos autônomos, durante o período em questão\.  Estas informações são utilizadas na geração do evento S\-1200 do eSocial\.

Esta é uma tabela “filha” da SAFX247 \(Demonstrativo de Pagamento dos Autônomos\), onde serão informados outros vínculos ou atividades trabalhistas que o trabalhador autônomo possa ter durante o período referente ao demonstrativo informado na tabela “mãe”\.

__Campos que compõe a chave da tabela \(PK\):__

Desta forma, os campos que compõe a chave de identificação da tabela serão os campos chave da tabela “mãe” \+ campos que identificam o vínculo/atividade na tabela “filha”:

\- Código da Empresa 

\- Código do Estabelecimento 

\- Indicador Pessoa Fis/Jur 

\- Código Pessoa Fis/Jur 

\- Ano Competência

\- Mês Competência 

\- Identificador do Demonstrativo de Pagamento

   

    Campos chave da tabela mãe \(SAFX247\)

\- CNPJ/CPF do Empregador 

        Campo de identificação do vínculo

__RN01__

__RN02__

__RN03__

__RN04__

__RN05__

__RN06__

__RN07__

__Campo Código da Empresa__

__Campo Código do Estabelecimento__

__Campo Ano Competência __

__Campo Mês Competência__

__Campo Indicador Pessoa Fis/Jur __

__Campo Código Pessoa Fis/Jur __

__Campo Identificador do Demonstrativo de Pagamento __

Estes são os campos chave da tabela “mãe” \(SAFX247\), e assim, a validação é a mesma feita na importação da SAFX247\.

Crítica da existência do demonstrativo na tabela mãe \(SAFX247\):

A partir dos dados informados nestes campos, será verificada a existência do registro na SAFX247\. Caso não exista, será gravada a seguinte mensagem de erro no log da importação:

*       “O Demonstrativo de Pagamento não existe na Tabela de Demonstrativo de Pagamento dos Autônomos \(SAFX247\)”*

Crítica sobre o campo “Indicador de Desconto da Contribuição Previdenciária” do demonstrativo \(SAFX247\):

Quando o demonstrativo existir, será verificada a informação do campo “*08\-Indicador de Desconto da Contribuição Previdenciária”*, pois os outros vínculos do trabalhador da SAFX250 só devem ser informados quando este campo estiver preenchido\. 

Se campo “*08\-Indicador de Desconto da Contribuição Previdenciária*” da SAFX247 *não preenchido*:

     Neste caso, será gravada a seguinte mensagem de erro no log da importação, e o registro não será importado:

*                 “Os Outros Vínculos do Trabalhador \(SAFX250\) só devem ser informados quando o Indicador de Desconto *

*                                    da Contribuição Previdenciária do demonstrativo \(SAFX247\) estiver preenchido”*

__RN08__

__Campo CNPJ/CPF do Empregador __

Campo de preenchimento obrigatório\.

Validações:

Se for um CNPJ \(14 dígitos\), deve ser um CNPJ válido;

Se for um CPF \(11 dígitos\), deve ser um CPF válido;

Se for um CNPJ, deve ser diferente do CNPJ do estabelecimento \(a comparação será feita pela raiz, ou seja, as 8 primeiras posições\);

Se for um CPF, deve ser diferente do CPF do trabalhador em questão \(pessoa fis/jur do demonstrativo de pagamento\);

Quando o campo não for preenchido, ou não atender as regras descritas acima, será gravada uma das mensagens de erro abaixo e o registro não será importado:

No caso de CNPJ/CPF não preenchido, ou com informação inválida:

*                                              “CNPJ/CPF do empregador não preenchido ou inválido”*

No caso do CNPJ \(quando for o caso\) ser igual ao CNPJ do estabelecimento, ou do CPF \(quando for o caso\) ser igual ao CPF do trabalhador:

*           “O CNPJ/CPF do empregador não pode ser o mesmo CNPJ de empresa, nem o mesmo CPF do trabalhador”*

__RN09__

__Campo Código da Categoria do Trabalhador__

Campo de preenchimento obrigatório\.

O conteúdo informado deve ser um código existente na “*Tabela de Categoria de Trabalhador – eSocial*”  __\(TACES66\)__\.

Quando não preenchido, ou o código informado não existir na TACES66, será gravada mensagem de erro padrão e o registro não será importado\.

__RN10__

__Campo Valor Remuneração __

Campo de preenchimento obrigatório\.

Quando não preenchido, será gravada mensagem de erro padrão e o registro não será importado\.

__RN11__

__Campo Valor Retenção Previdência__

Campo de preenchimento *não* obrigatório\.

\(valor apenas informativo, pois não consta no layout do eSocial\)

