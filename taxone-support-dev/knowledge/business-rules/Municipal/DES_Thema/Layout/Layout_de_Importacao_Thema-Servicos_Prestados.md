# Layout_de_Importacao_Thema-Servicos_Prestados

- **Fonte:** Layout_de_Importacao_Thema-Servicos_Prestados.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 34 KB

---

[Arquivos de escrituração \(serviços prestados\)](https://wiki.thema.inf.br/wiki/help/32220" \t "_blank)\.

## Layout padrão do XML

### <a id="Exemplo_para_Prestadores_de_Servi%C3%A7o"></a>Exemplo para Prestadores de Serviço em geral

<declaracao retificadora="123456">

  <empresa nome="Nome da empresa 2" inscricao="3"

  cpfcnpj="00000000000000">

    <informacao exercicio="2009" mes="04"

    atividade\_desenvolvida="3872" aliquota="2000" basecalculo=""

    observacao="OPCIONAL" numero\_funcionarios="6" valor\_folha\_pagamento="500000" valor\_faturamento="200000">

      <nota data\_emissao="20/04/2009" numero="3" serie="A"

      valor\_tributavel="10000" situacao="A" valor\_bruto="0"

      valor\_deducao="0" modelo="01" cpfcnpj\_tomador="00000000000"

      numero\_servico="52" codigo\_obra="47" numero\_projeto= "20151" />

      <nota data\_emissao="30/04/2009" numero="4" serie="A"

      valor\_tributavel="20000" situacao="N" valor\_bruto="0"

      valor\_deducao="0" modelo="01" cpfcnpj\_tomador="00000000000"

      numero\_servico="52" />

    </informacao>

    <informacao exercicio="2009" mes="04" aliquota="0500"

    basecalculo="" quantidade\_issfixo="200" observacao="OPCIONAL">

      <nota data\_emissao="20/04/2009" numero="3" serie=""

      valor\_tributavel="15000" situacao="N" valor\_bruto="0"

      valor\_deducao="0" modelo="01" cpfcnpj\_tomador="00000000000"

      numero\_servico="52" />

      <nota data\_emissao="30/04/2009" numero="4" serie=""

      valor\_tributavel="12000" situacao="R" valor\_bruto="0"

      valor\_deducao="0" modelo="01" cpfcnpj\_tomador="00000000000"

      numero\_servico="51" codigo\_obra="47" numero\_projeto= "20151" />

    </informacao>

  </empresa>

</declaracao>

### Exemplo para declaração sem movimento \(SMOV\)

<?xml version="1\.0" encoding="iso\-8859\-1"?>

<declaracao>

<empresa nome="TESTE" inscricao="100" cpfcnpj="12345678000123">

<informacao exercicio="2014" mes="02" atividade\_desenvolvida="416" aliquota="200" basecalculo="0" observacao=""></informacao>

</empresa>

</declaracao>

### Exemplo para Instituições Financeiras

<declaracao>

  <empresa inscricao="441" cpfcnpj="00000000000000"

  nome="BANCO XXXXXX">

    <informacao atividade\_desenvolvida="1238" mes="07"

    aliquota="500" exercicio="2014"

    observacao="Declaracao com Plano de Contas">

      <nota serie="" valor\_tributavel="500" subserie=""

      valor\_deducao="0" valor\_bruto="500" situacao="P" modelo="01"

      observacao="" data\_emissao="01/07/2014" numero="1001"

      numero\_servico="52" />

    </informacao>

  </empresa>

</declaracao>

## Explicação sobre os tags:

### <a id="Conven%C3%A7%C3%B5es"></a>Convenções

- Todos os campos devem estar entre aspas, conforme o exemplo acima
- Os campos de valores NÃO devem conter pontos ou vírgulas e considera as últimas 2\(duas\) casas como decimais, por exemplo 1000 representa o número 10,00
- Deverá ser respeitado o tamanho máximo dos campos
- Campos de data DEVEM conter o separador "/"\. Ex: 15/02/1998
- O CPF/CNPJ não deve conter separadores, como pontos, traços, etc
- O Número da Nota não deve conter separadores, como pontos, traços, etc

### <a id="Tags"></a>Tags

- __<declaracao>:__ Indica o início da Declaração
- __retificadora:__ Numero de entrega da declaração que será retificada\.
- __<empresa:__ Abertura da guia por empresa
- __nome:__ Nome da Empresa \(100 caracteres\)
- __inscricao:__ Número da Empresa na Prefeitura \(10 caracteres\)
- __cpfcnpj:__ CPF ou CNPJ da Empresa \(14 caracteres\)
- __<informacao:__ Abertura do Movimento Informado
- __exercicio:__ Exercício da competência declaração\(4 caracteres\)
- __mes:__ Mês de competência da declaração \(2 caracteres\)
- __aliquota:__ Alíquota deverá ser informada para ambas as declarações, seja normal ou plano de contas\. \(4 caracteres\)
- __quantidade\_issfixo:__ Informação define a quantidade de ISS FIXO 1\(Um\); Deve haver uma coerência com a tabela de cálculo da Prefeitura; \(Ex: Número de Sócios, etc\)Informação OPCIONAL
- __quantidade\_2\_issfixo:__ Informação define a quantidade de ISS FIXO 2\(dois\); Deve haver uma coerência com a tabela de cálculo da Prefeitura; \(Ex: Número de Empregados, etc\) Informação OPCIONAL
- __observacao:__ Informação OPCIONAL \(120 caracteres\)
- __basecalculo:__ Informação necessária somente para quem faz declaração por ESTIMATIVA \(15 caracteres\)
- __atividade\_desenvolvida:__ Código auxiliar disponível na Tabela Estrutural da lista de atividades disponibilizada pela Prefeitura\. Para plano de contas, deve\-se verificar o CNAE cadastrado para a empresa e então acessar seu respectivo plano de contas para obter o código\. \(6 caracteres\)
- __numero\_funcionarios:__ Numero de funcionários
- __valor\_folha\_pagamento:__ Valor da folha de pagamento
- __valor\_faturamento:__ Valor do faturamento
- __<nota:__ Todas as notas fiscais OU Movimentação do Plano de Contas
- __codigo\_obra:__ Código da Obra em caso de serviços vinculados a uma Obra;
- __numero\_projeto:__ Número do Projeto em caso de serviços vinculados a uma Obra;
- __data\_emissao:__ Data de emissão da Nota OU Data da Declaração no caso de Plano de Contas \(10 caracteres\)
- __numero:__ Número da Nota \(10 caracteres\) OU Número do Plano de Contas, visível na coluna Conta Movimento \(50 caracteres\)
- __serie:__ Série da Nota Fiscal\. Informação OPCIONAL \(2 caracteres\)
- __subserie:__ SubSérie da Nota Fiscal\. Informação OPCIONAL\(2 caracteres\)
- __observacao:__ Informação OPCIONAL \(200 caracteres\)
- __valor\_tributavel:__ Valor da Nota para efeito de cálculo do Imposto \(15 caracteres\)
- __situacao:__ Relativo a situação da nota, poderá receber: A = Ativa, N = Nula ou cancelada, E = Extraviada, R = Retida, P = Plano de Contas \(1 caractere\)
- __valor\_bruto:__ Valor Bruto de Faturamento \(15 caracteres\)
- __valor\_deducao:__ Se aconteceu alguma dedução do bruto \(15 caracteres\)
- __modelo/especie:__ Código do modelo da nota emitida \(Cupom fiscal, Nota Fiscal de Serviços e etc\), consulte a Prefeitura e verifique a tabela dos modelos\. A informação será desnecessária caso não haja regulamentação \(2 caracteres\)
- __numero\_servico:__ Operação que foi efetuada de acordo com o código do serviço na Tabela de Serviços\. Dê especial atenção para este enquadramento, pois ele indicará se haverá incidência de tributação\. Consulte tabela na Prefeitura\(2 Caracteres\)
- __cpfcnpj\_tomador__ ou cpfcgc\_tomador: CPF ou CNPJ do Tomador do serviço, responsável tributário\(14 caracteres\)
- __</nota>:__ Indica o fechamento da Nota OU Plano de Contas
- __</informacao>:__ Indica o fechamento do Movimento Informado
- __</empresa>:__ Indica o fechamento da declaração da Empresa
- __</declaracao>:__ Indica o fechamento da Declaração

__Importante:__ Quando houver necessidade de declaração de SEM MOVIMENTO, não preencher o tag <nota>

