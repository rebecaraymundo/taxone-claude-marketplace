# MTZ-OTF-Geracao_da_SEFIP

- **Fonte:** MTZ-OTF-Geracao_da_SEFIP.docx
- **Modificado:** 2020-08-31
- **Tamanho:** 27 KB

---

# Obrigações de Tributos Federais \- Geração do Meio Magnético SEFIP

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

CH113756\-A

Obrigações de Tributos Federais \- Geração do Meio Magnético SEFIP

Este chamado de alteração de regra de negócio tem por objetivo determinar quais Códigos de Pagamento de INSS podem fazer parte da SEFIP\.

OS4658

Geração do Meio Magnético SEFIP

Centralização das informações por estabelecimento Matriz

CH24869\_2014

Ajustar geração do SEFIP

Este documento tem como objetivo ajustar a geração do SEFIP para considerar os registros de acordo com o Período de Competência preenchido\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Ao gerar o meio magnético da SEFIP, o sistema deverá verificar o Código de Pagamento de INSS na tabela IRT\_COD\_PG\_INSS\. Essa tabela é alimentada pela TFIX34\.

Caso o Código de Pagamento de INSS esteja com o campo IND\_AUTONOMO = “N”, essa informação não deverá ser gerada na SEFIP \(arquivo\) e nem no relatorio contendo as informações do arquivo gerado\.

Somente os Códigos de Pagamento de INSS cujo campo IND\_AUTONOMO = “S” é que devem ser gerados no arquivo\.

__CH113756\-A__

__RN02__

Campo Centralização por estabelecimento Matriz

Tipo Checkbox

Não Obrigatório

Default não selecionado

Quando selecionado, a centralização das informações será por estabelecimento matriz, ou seja, deverá gerar um único registro “10”, correspondente a matriz, com as informações dos estabelecimentos centralizados\.

Obs: Este campo será habilitado somente quando o Radio Button “empresa” do campo “Processar dados Por” estiver selecionado, na tela de “Geração Meio Magnético”\.

__OS4658__

__RN02__

Após a geração dos registros, a geração do MM SEFIP deve considerar a recuperação desses registros, considerando os Documentos Fiscais que estejam dentro do Período de Competência preenchido na tela de geração \(verifica pela data fiscal da NF\) e ainda compreendendo a parametrização da Data de Vigência em Federal >> OTF >> Outras Obrigações >> SEFIP >> Parâmetros, ou seja, se estiver parametrizado dentro do Período de Competência considerar o parâmetro, caso contrário não gerar e emitir a mensagem no log: “Status: Alerta \- Req 10 \- Inf\. Empresa: Não há informações de parâmetros da Sefip p/ o estabelecimento <<levar código do estabelecimento selecionado>>”\.

__CH24869\_2014__

