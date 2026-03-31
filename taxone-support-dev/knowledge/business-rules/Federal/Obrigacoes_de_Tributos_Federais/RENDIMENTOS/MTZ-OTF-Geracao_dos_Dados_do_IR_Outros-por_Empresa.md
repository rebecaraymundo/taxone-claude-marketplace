# MTZ-OTF-Geracao_dos_Dados_do_IR_Outros-por_Empresa

- **Fonte:** MTZ-OTF-Geracao_dos_Dados_do_IR_Outros-por_Empresa.docx
- **Modificado:** 2022-05-06
- **Tamanho:** 38 KB

---

# Módulo – Obrigações de Tributos Federais

# Geração dos Dados do Informe de Rendimentos Outros – por Empresa 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3753\-C

Obrigações de Tributos Federais – Desconsiderar Retenções com Estorno dos Informes de Rendimento

O cliente Caixa Seguradora possui um processo interno de estorno de retenções\. O conceito de estorno de retenções é quando o cliente deseja reaver o valor de uma retenção indevida\. Isso pode ocorrer em três momentos distintos no produto:

- __Retenção sem DARF Gerado:__ esse é o caso mais simples, o cliente importou uma retenção no produto, porém antes mesmo de gerar o DARF referente a essa retenção, o cliente percebeu o erro\. 
- __Retenção com DARF Gerado e Não Pago:__ esse caso é o cenário principal do cliente, pois ele envia o DARF para pagamento e por motivos de erro no sistema bancário – exemplo: conta inválida ou encerrada, CPF inválido, entre outros – o pagamento não é processado\. Nesse caso o cliente tem que estornar o valor no ERP \(SAP\) para que essa retenção não seja considerada em nenhuma obrigação acessória\.
- __Retenção com DARF Gerado e Pago: __esse cenário já está resolvido dentro do sistema, pois se o cliente pagou um DARF indevidamente – a maior ou a menor – o cliente pode resolver essa situação através da funcionalidade de Tributos Ajustados já disponibilizada no produto\.

A solução proposta foi a criação de dois campos de identificação na tabela de Controle de Tributos: “Estorno” e “Data do Estorno”\. Esses campos identificam a retenção estornada e não permitem que a mesma seja considerada nas obrigações acessórias federais e relatórios de conferência do sistema\. Vale salientar que esses campos citados anteriormente foram criados na OS3753\. As rotinas do sistema que deverão ser alteradas são:

- Obrigações Acessórias
	- DARF
	- DCTF
	- DIRF
	- __Informe de Rendimentos – OS3753\-C__
- Relatórios Gerenciais
	- Relatório de Tributos Federais
	- Relatório de Rastreabilidade

Hoje a rotina de importação do produto não permite a importação de uma retenção que tenha um DARF vinculado à mesma e que esteja Gerado/Não Pago ou Pago\. Isso é um controle do sistema para garantir que um DARF fique diferente da retenção, ocasionando erros críticos para o cliente\. Esse controle funciona assim de longa data e no passado já foram dados NO GO para que isso fosse permitido\.

Com esse cenário do cliente, o sistema deverá permitir que na rotina de importação da tabela de Controle de Tributos – SAFX53 – o sistema ao identificar os campos “Estorno” e “Data do Estorno” preenchidos, o sistema deverá fazer a seguinte identificação:

- __Retenção sem DARF Gerado:__ nesse caso a retenção será atualizada sem maiores ônus\. 
- __Retenção com DARF Gerado e Não Pago:__ nesse caso, o sistema irá identificar o DARF dessa retenção e irá à tabela X75\_DCTF apagar esse DARF\. Essa retenção e as outras associadas ao DARF que foi deletado, terão seu status alterado para “Não Gerado”\. Essas retenções terão o campo “Estorno” e “Data do Estorno” informados\.
- __Retenção com DARF Pago:__ nesse caso o cliente deverá utilizar o sistema de acordo com a funcionalidade de Tributos Ajustados já existente no sistema\. 

É importante que no segundo ponto o DARF seja deletado, porque as retenções com Estorno não serão consideradas nas obrigações federais\. Se isso não for desenvolvido ao gerar a DCTF o cliente irá ter uma Ficha de Pagamento \(R11\) sem uma Ficha de Débito vinculada\.

O escopo da OS3753\-C é permitir que os Informes de Rendimento desconsidere as retenções da tabela de Controle de Tributos que estejam estornadas\.

OS3832\-A

Alteração do Documento

Considerar no campo ‘07 \.Outros’ do quadro ‘4\. Rendimentos Isentos e Não tributáveis’, os valores referente a Benefícios Indiretos e Reembolso de Despesa Voluntário da Copa, além do valor de Bolsa de Estudo Recebida por Médico Residente oriundos da SAFX53\.

CH4854\_2013

OTF – Ajustes na geração do registro RTRT para considerar apenas o Valor Bruto

O objetivo deste documento de requisito é permitir duas importantes alterações no que se refere à DIRF e ao Informe de Rendimentos:

- Informe de Rendimentos
	- Foi observado que ao gerar o Comprovante de Rendimentos através do Validador da DIRF 2013, quando o Código de Receita é 0916 – Prêmios Obtidos em concursos e sorteios, o valor informado na linha 2 – Outros do Quadro 5 – Rendimentos sujeitos à Tributação Exclusiva \(rendimento líquido\) deverá ser o resultado da Linha 01 – Linha 02 do Quadro 3 – Rendimentos Tributáveis\. Ocorre que essa informação – já calculada – já é carregada através do campo 43 da SAFX53 \(Valor Outros de Tributação Exclusiva\)\. Nesse caso quando for gerado o Informe de Rendimentos desse Código de Receita é 0916, o sistema só deve exibir a linha 2 do Quadro 5 e não deve exibir as informações do Quadro 3\.
- DIRF
	- Ao realizar os testes do Informe de Rendimentos, foi verificado que não existe registro específico para os Rendimentos de Tributação Exclusiva\. Ocorre que existe uma regra no produto MasterSAF DW que ao gerar os registro RTRT – Rendimento Tributável, o sistema realiza uma soma entre os campos de Valor Bruto e Valor Outros de Tributação Exclusiva \(campos 14 e 43 da SAFX53\)\. Ocorre que após entendimento do CAN, essa informação já é composta como Rendimento Tributável, uma vez que a única informação que não deve ser considerada no Rendimento Tributável são as informações de Exigibilidade Suspensa\. Nesse caso o sistema só deve considerar para a geração do registro RTRT a informação do Valor Bruto\.

CH6108\_2013

Obrigações de Tributos Federais – Não considerar Retenções canceladas na geração do Informe de Rendimentos Outros

O objetivo deste documento de requisito é alterar o Informe de Rendimentos do tipo Outros para que as retenções que estejam com o flag “Cancelado” selecionado e com “Data de Cancelamento” informada, não sejam considerados no IR\.

CH21610\-A\_2013

Obrigações de Tributos Federais – Considerar Tributo COSIRF na geração do Informe de Rendimentos Outros

O objetivo deste documento de requisito é permitir que as retenções que sejam do tributo COSIRF sejam geradas nos Informes de Rendimento Outros do produto\.

MFS\-9872

Incluir beneficiários do exterior

Este documento tem como objetivo corrigir a geração dos Informes de Rendimento Outros para considerar beneficiários do exterior\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Ao gerar o Informe de Rendimentos Outros por Empresa, o sistema ao recuperar os registros de retenção do Controle de Tributos \(tabela: X53\_RETENCAO\_IRRF\), deve ignorar os registros estornados, ou seja, os registros cujo campo “Estorno” e “Data do Estorno” estejam preenchidos\.

__OS3753\-C__

__RN02__

Considerar no campo ‘07\.Outros’ do quadro ‘4\. Rendimentos Isentos e Não tributáveis’, também os valores dos campos: Valor – Voluntário da Copa, Valor 13º – Voluntário da Copa, Valor – Bolsa de Estudo Recebida por Médico Residente e Valor 13º– Bolsa de Estudo Recebida por Médico Residente da X53\.

Atenção: Atualmente a rotina de geração da DIRF, já está considerando outros valores para compor o campo 07\.Outros, estes valores devem ser mantidos, incluindo os campos citados acima\. 

__OS3832\-A__

__RN03__

Ao gerar o Informe de Rendimentos Outros, caso o Código de Retenção seja 0916 \(campo 11 da SAFX53\), o sistema deverá gerar normalmente a linha 02 do Quadro 5 recuperando a informação do campo 43 da SAFX53 \(Valor Outros de Tributação Exclusiva\), porém embora exista informação para ser gerada nas linhas 01 e 05 do Quadro 3 – Rendimentos Tributáveis, o sistema não irá exibir essa informação ao emitir o Informe\.

Nos casos dos outros Códigos de Retenção, a informação será exibida normalmente no Quadro 3\.

Vale salientar que essa regra é válida somente para o beneficiário que seja Pessoa Física\. No caso do beneficiário Pessoa Jurídica, o informe será gerado normalmente com as informações de Rendimento Bruto e Imposto de Renda Retido na Fonte\.

__CH4854\_2013__

__RN04__

Caso ao gerar o Informe de Rendimentos, exista algum Controle de Tributos com Código de Retenção = 0916 para o mesmo Beneficiário e com o campo 43 – Valor Outros Tributação Exclusiva não preenchido na tela de Controle de Tributos, o sistema irá gerar o Informe de Rendimentos conforme regra RN03, porém será exibida a seguinte mensagem de aviso no Log de Processos:

“Existem Controle de Tributos com Código 0916 sem Valor Outros de Tributação Exclusiva preenchido e o mesmo não foi gerado no Informe de Rendimentos”\. No caso dessa mensagem será exibida a chave do Controle de Tributos para correção por parte do usuário\.

O registro que não possuir o campo 43 – Valor Outros Tributação Exclusiva preenchido, não será considerado na geração do Informe de Rendimentos\.

__CH4854\_2013__

__RN05__

Ao gerar o Informe de Rendimentos Outros, caso existam retenções na tabela de Controle de Tributos \(X53\_RETENCAO\_IRRF\) cujo campo “Cancelado” esteja selecionado e cujo campo “Data Cancelamento” esteja informado, esse registro não deve ser considerado na geração do Informe de Rendimentos\.

Só deverão ser considerados no Informe de Rendimentos, os registros cujo campo “Cancelado” não esteja selecionado e cujo campo “Data Cancelamento” não esteja informado\.

__CH6108\_2013__

__RN06__

O Informe de Rendimentos Outros deverá considerar as retenções cujo tributo seja COSIRF \(campo Tributo da tela: Manutenção >> Controle de Tributos\) = 32 do módulo DW\.

Atualmente a COSIRF não é considerada nos Informes de Rendimento\. A mesma será gerada conforme as regras atuais do sistema\.

__CH21610\-A\_2013__

__RN07__

Será necessário alterar a rotina de geração dos dados dos rendimentos de outros beneficiários para contemplar pessoa física/ jurídica localizada no exterior\.

Na SAFX04, se tratando de pessoa física/ jurídica do exterior não é obrigatória à informação do campo “06\-CPF\-CGC”, então como se trata de um campo chave na tabela o campo “04\-Indicador do Conteúdo do Código” deve ser preenchido como “4\-Especial”, com isso, para geração desses beneficiários será necessário considerar o campo “53\-Número de Identificação Fiscal“ da SAFX04, ou seja:

- Considerar a seleção do beneficiário através do campo “06\-CPF\-CGC” da SAFX04, se não estiver preenchido considerar a seleção do beneficiário através do campo “53\-Número de Identificação Fiscal“ da SAFX04, se não estiver preenchido o registro será desconsiderado da geração\.

__*Atenção:*__ As outras condições para seleção dos registros não sofrem alteração, somente do beneficiário cadastrado na SAFX53 quando se tratar de estabelecido no exterior, solução adotada anteriormente na DIRF\.

__MFS\-9872__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

