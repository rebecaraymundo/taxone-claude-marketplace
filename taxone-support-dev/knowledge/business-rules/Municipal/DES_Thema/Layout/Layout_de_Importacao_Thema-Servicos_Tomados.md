# Layout_de_Importacao_Thema-Servicos_Tomados

- **Fonte:** Layout_de_Importacao_Thema-Servicos_Tomados.docx
- **Modificado:** 2025-12-07
- **Tamanho:** 35 KB

---

[Arquivos de retenções \(serviços tomados\)](https://wiki.thema.inf.br/wiki/help/32220" \t "_blank)\.

Exemplo 1: Escrituração Tomador \(Convencional\)

<declaracao retificadora="123456">

  <retencao cpfcnpj="88148945000104">

    <info\_retencao data\_informacao="29/06/2005" exercicio="2005"

    mes="06" observacao="observacao da entrega" aplicacao="N">

      <nota\_retencao data\_emissao="08/06/2005" modelo="01"

      numero="1" serie="A" cpfcnpf\_prestador="40726258091"

      atividade\_desenvolvida="1516"

      descricao\_atividade="Armazenamento" numero\_servico="11"

      valor\_bruto="0500000" valor\_deducao="0200000"

      valor\_tributavel="000000300000" aliquota="300"

      valor\_retido="0009000" codigo\_obra="47" numero\_projeto= "20151"

      ></nota\_retencao>

      <nota\_retencao data\_emissao="07/06/2005" modelo="02"

      numero="2" serie="A" cpfcnpf\_prestador="00125392000115"

      descricao\_atividade="Armazenamento" numero\_servico="11"

      atividade\_desenvolvida="1516" valor\_bruto="0500000"

      valor\_deducao="0200000" valor\_tributavel="000000300000"

      aliquota="200" valor\_retido="0006000"></nota\_retencao>

    </info\_retencao>

    <info\_retencao data\_informacao="29/03/2005" exercicio="2005"

    mes="02" observacao="observacao da entrega" aplicacao="N">

      <nota\_retencao data\_emissao="07/03/2005" modelo="01"

      numero="1" serie="A" cpfcnpf\_prestador="00125392000115"

      descricao\_atividade="Armazenamento" numero\_servico="11"

      atividade\_desenvolvida="1516" valor\_bruto="0800000"

      valor\_deducao="0200000" valor\_tributavel="000000600000"

      aliquota="3" valor\_retido="000180" codigo\_obra="47" 

      numero\_projeto= "20151"></nota\_retencao>

    </info\_retencao>

  </retencao>

</declaracao>

__Explicação sobre os tags:__

- __<declaracao>__ Indica o início da Declaração
- __retificadora:__ Numero de entrega da declaração que será retificada\.
- __<retencao__ Inicio da declaração para determinado contribuinte
- __cpfcnpj__ Informe o CPF ou CNPJ da empresa TOMADORA do serviço \(14 caracteres\)
- __<info\_retencao__ Inicio das informações da retenção, indica a competencia, pode\-se ter mais de uma por declaração;
- __data\_informacao__ Data do cadastro da informação, padrão DD/MM/YYYY\(8 caracteres\)
- __exercicio__ Exercicio de competência da declaração \(4 caracteres\)
- __mes__ Mês de competência da declaração \(2 caracteres\)
- __observacao__ Informação OPCIONAL, campo livre para digitação\(300 caracteres\)
- __aplicacao__ Para identificar este tipo de retenção, convencinou\-se o uso de aplicação "N" \(1 caractere\)
- __numero\_servico__ Operação que foi efetuada de acordo com o código do serviço na Tabela de Serviços, corresponde ao campo "OPERAÇÃO" da Escrituração Tomador\(2 Caracteres\)
- __<nota\_retencao__ Inicio de informações sobre as notas fiscais retidas nas competências
- __codigo\_obra:__ Código da Obra em caso de serviços vinculados a uma Obra;
- __numero\_projeto:__ Número do Projeto em caso de serviços vinculados a uma obra;
- __data\_emissao__ Data de emissão da nota, no padrão dd/mm/yyyy \(8 caracteres\)
- __modelo/espécie:__ código do modelo da nota emitida \(Cupom fiscal, Nota Fiscal de Serviços e etc\), consulte a Prefeitura e verifique a tabela dos \*__modelos__ \(exemplo em Anexo I\)\. A informação será desnecessária caso não haja regulamentação \(2 caracteres\)
- __numero__ Número da nota fiscal \(10 caracteres\)
- __serie__ Série da nota fiscal \(2 caracteres\)
- __cpfcnpf\_prestador__ CPF ou CNPJ do Prestador do serviço \(14 caracteres\)
- __descricao\_atividade__ Descrição da atividade desenvolvida pelo prestador \(200 caracteres\)
- __atividade\_desenvolvida__ Código auxiliar disponível na Tabela Estrutural da lista de atividades disponibilizada pela Prefeitura \(6 caracteres\)
- __valor\_bruto__ Valor total da nota \(15 caracteres\)
- __valor\_deducao__ Valor a ser deduzido da nota \(15 caracteres\)
- __valor\_tributavel__ Valor tributável da nota fiscal \(15 caracteres\)
- __aliquota__ Percentual aplicado para essa atividade \(10 caracteres\)
- __valor\_retido>__ Percentual da alíquota aplicada sobre o valor bruto\. Este será o valor retido \(10 caracteres\)
- __</nota\_retencao>__ Indica o fechamento das informações da nota
- __</info\_retencao>__ Indica o fechamento das informações da Retenção
- __</retencao>__ Indica o fechamento da declaração da Retenção

Exemplo 2: Escrituração Obra

<obra cpfcnpj="88148945000104">

        

<info\_obra data\_informacao="29/03/2005" exercicio="2005" mes="03"

observacao="observacao da entrega" aplicacao="B"

numero\_obra="00003">

            

<nota\_obra data\_emissao="07/03/2005" modelo="01" numero="1"

serie="A" cpfcnpf\_prestador="00125392000115"

descricao\_atividade="Armazenamento" valor\_bruto="1800000"

valor\_deducao="0200000" valor\_tributavel="000001600000"

aliquota="233" valor\_retido="00037280">

            </nota\_obra>

            

<nota\_obra data\_emissao="07/03/2005" modelo="02" numero="2"

serie="A" cpfcnpf\_prestador="00125392000115"

descricao\_atividade="Armazenamento" valor\_bruto="1800000"

valor\_deducao="0200000" valor\_tributavel="000001600000"

aliquota="300" valor\_retido="00048000">

            </nota\_obra>

        </info\_obra>

    </obra>

__Explicação sobre os tags:__

- __<declaracao>__ Indica o início da Declaração;
- __<obra cpfcnpj>__ CPF ou CNPJ da Empresa \(14 caracteres\)
- __<info\_obra data\_informacao__ Data do cadastro da informação, padrão dd/mm/yyyy \(8 caracteres\)
- __exercicio__ Exercicio de competência da declaração \(4 caracteres\)
- __mes__ Mês de competência da declaração \(2 caracteres\)
- __aplicacao__ Tipo da Aplicação, A,B ou C \(1 caracter\)
- __numero\_obra__ Codigo de Inscrição da Obra \(10 caracteres\)
- __<nota\_obra__ Declara as notas fiscais para esta obra
- __codigo\_obra: Código da Obra em caso de serviços vinculados a uma Obra;__
- numero\_projeto: Número do Projeto em caso de serviços vinculados a uma Obra;
- __data\_emissao__ Data da emissão da nota dd/mm/yyyy \(8 caracteres\)
- __modelo__ Código do modelo de nota emitida, sua obrigatoriedade é definida pela Prefeitura\(2 caracteres\)
- __numero__ Numero da Nota Fiscal \(15 caracteres\)
- __serie__ Série da nota \(2 caracteres\)
- __cpfcnpf\_prestador__ CPF ou CNPJ do prestador do serviço \(14 caracteres\)
- __descricao\_atividade__ Atividade desenvolvida pelo prestador \(200 caracteres\)
- __valor\_bruto__ Valor total da nota \(15 caracteres\)
- __valor\_deducao__ Valor a ser deduzido da nota \(15 caracteres\)
- __valor\_tributavel__ Valor tributável da nota fiscal \(15 caracteres\)
- __aliquota__ Percentual aplicado para essa atividade \(10 caracteres\)
- __valor\_retido>__ Percentual da alíquota aplicada sobre o valor bruto\. Este será o valor retido \(10 caracteres\)
- __</nota\_obra>__ Indica o fechamento das informações sobre a nota da obra
- __</ínfo\_obra>__ Indica o fechamento das informações da obra
- __</obra>__ Indica fechamento da da obra

Exemplo 3: Escrituração Arrendamento Mercantil

<retencao cpfcnpj="22222222222">

        

<info\_retencao data\_informacao="29/03/2005" exercicio="2005"

mes="03" observacao="observacao da entrega" aplicacao="L">

            

<nota\_retencao data\_emissao="07/03/2005"

cpfcnpf\_arrendadora="00125392000115" descricao\_atividade="Leasing"

valor\_tributavel="000001000000" aliquota="10"

valor\_retido="00100000" cpfcnpf\_vendedor="00125392000115"

numero\_renavam="12132" placa\_veiculo="ILN8371"

cpfcnpf\_arrendatario="93080257000181" nome\_arrendatario=""

numero\_contrato="">

            </nota\_retencao>

        </info\_retencao>

    </retencao>

__Explicação sobre os tags:__

- __<retencao cpfcnpj__ CPF ou CNPJ do responsável \(14 caracteres\)
- __<info\_retencao data\_informacao__ Data do cadastro da informação, no padrão dd/mm/yyyy \(8 caracteres\)
- __exercicio__ Exercício de competência da declaração \(4 caracteres\)
- __mes__ Mês de competência da declaração \(2 caracteres\)
- __observacao__ Campo opcional para peculiaridades a respeito da declaração \(300 caracteres\)
- __aplicacao>__ Para identificar este tipo de retenção, convencinou\-se o uso de aplicação "L"
- __<nota\_retencao data\_emissao__ Data da emissão da nota, no padrão dd/mm/yyyy \(8 caracteres\)
- __cpfcnpj\_arrendadora__ CPF ou CNPJ da arrendadora \(14 caracteres\)
- __descricao\_atividade__ Descrição da atividade da transação \(200 caracteres\)
- __valor\_tributavel__ Valor tributável da nota fiscal \(15 caracteres\)
- __aliquota__ Percentual aplicado para essa atividade \(10 caracteres\)
- __valor\_retido__ Percentual da alíquota aplicada sobre o valor bruto\. Este será o valor retido \(10 caracteres\)
- __cpfcnpj\_vendedor__ CPF ou CNPJ do vendedor do veículo \(14 caracteres\)
- __numero\_renavam__ Número do registro do veículo envolvido na transação \(30 caracteres\)
- __placa\_veiculo__ Placa do veículo envolvido na transação \(15 caracteres\)
- __cpfcnpj\_arrendatario__ CPF ou CNPJ do arrendatario \(14 caracteres\)
- __nome\_arrendatario__ Nome do arrendatario \(60 caracteres\)
- __numero\_contrato__ Número do contrato de compra e venda \(20 caracteres\)
- __</nota\_retencao>__ Indica o fechamento das informações da nota
- __</info\_retencao>__ Indica o fechamento das informações da Retenção
- __</retencao>__ Indica o fechamento da declaração da Retenção

Exemplo 4: Escrituração CRVA

<declaracao\_CRVA cpfcnpj="22222222222">

        

<info\_declaracao data\_informacao="01/08/2005" exercicio="2005"

mes="08" observacao="teste de declaração" aplicacao="N">

            

<mov\_declaracao data\_movimento="07/03/2005" numero\_renavam="123456"

placa\_veiculo="ILN 8371" cpfcnpf\_arrendatario="93080257000181"

nome\_arrendatario="cerebrum informática ltda"

cpfcnpf\_arrendadora="00125392000115">

            </mov\_declaracao>

        </info\_declaracao>

    </declaracao\_CRVA>

__Explicação sobre os tags:__

- __<declaracao\_CRVA cpfcnpj__ CPF ou CNPJ do responsável pela declaração \(14 caracteres\)
- __<info\_declaracao data\_informacao__ Data do cadastro da informação, no padrão dd/mm/yyyy \(8 caracteres\)
- __exercicio__ Exercício de competência da declaração \(4 caracteres\)
- __mes__ Mês de competência da declaração \(2 caracteres\)
- __observacao__ Campo destinado a peculiaridades sobre a declaração \(300 caracteres\)
- __aplicacao>__ Para identificar este tipo de retenção, convencinou\-se o uso de aplicação "N"
- __<mov\_declaracao data\_movimento__ Data do transação, no padrão dd/mm/yyyy \(8 caracteres\)
- __numero\_renavam__ Número do registro do veículo envolvido na transação \(30 caracteres\)
- __placa\_veiculo__ Placa do veículo envolvido na transação \(15 caracteres\)
- __cpfcnpj\_arrendatario__ CPF ou CNPJ do arrendatario \(14 caracteres\)
- __nome\_arrendatario__ Nome do arrendatario \(60 caracteres\)
- __cpfcnpj\_arrendadora__ CPF ou CNPJ da arrendadora \(14 caracteres\)
- __</mov\_declaracao>__ Fechamento das informações do movimento da declaração
- __</info\_declaracao>__ Fechamento dos informações da Declaração
- __</declaracao\_CRVA>__ Fechamento da Declaração do CRVA
- __</declaracao>__ Fechamento do relatório de declarações

### <a id="Conven%C3%A7%C3%A3o"></a>Convenção

- Todos os campos devem estar entre aspas, conforme o exemplo acima;
- Os campos de valores NÃO devem conter pontos ou virgulas e tem as últimas 2\(duas\) casas para decimais; Ex: 1000\(representa o número 10,00\);
- Deverá ser respeitado o tamanho máximo dos campos;
- Campos de data DEVEM conter o separador "/"\. Ex: 15/02/1998
- O CPF/CNPJ não deve conter separadores, como pontos, traços, etc\.
- O Número da Nota não deve conter separadores, como pontos, traços, etc\.

__Importante\!__  
Este help contém um único exemplo de cada tipo de retenção, porém o arquivo poderá conter quantas retenções forem necessárias, desde que sigam este padrão descrito\.

