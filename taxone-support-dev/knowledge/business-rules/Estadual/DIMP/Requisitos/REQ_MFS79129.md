# REQ_MFS79129

- **Fonte:** REQ_MFS79129.docx
- **Modificado:** 2022-01-14
- **Tamanho:** 37 KB

---

__Orientações para correção do chamado__

                                                                                                      

Chave Ordenação:

1100

Resumo Mensal das Operações

2

V

<a id="_Hlk93051220"></a>cli\_cod\_fis\_jur \+ parc\_cod\_fis\_jur \+ ind\_comex

1110

Operações Diárias por Meio de Captura

3

1:N

cli\_cod\_fis\_jur \+ parc\_cod\_fis\_jur \+ ind\_comex \+ cod\_mcapt \+ dat\_oper \+ cnpj\_adqui

1115

Operações por Comprovante de transação

4

1:N

cli\_cod\_fis\_jur \+ parc\_cod\_fis\_jur \+ ind\_comex \+ cod\_mcapt \+ dat\_oper \+ cnpj\_adqui \+ hora \+ situacao

1120

Intermediador de Serviços e Negócios

5

1:1

cli\_cod\_fis\_jur \+ parc\_cod\_fis\_jur \+ ind\_comex \+ cod\_mcapt \+ dat\_oper \+ cnpj\_adqui \+ hora \+ situacao

- Registro 1100: Gera um registro no arquivo por cli\_cod\_fis\_jur \+ parc\_cod\_fis\_jur \+ ind\_comex
- <a id="_Hlk93051283"></a>Registro 1110: Gera um registro no arquivo por: cli\_cod\_fis\_jur \+ parc\_cod\_fis\_jur \+ ind\_comex \+ cod\_mcapt \+ dat\_oper \+ cnpj\_adqui
- Registro 1115: cada registro na tabela x313\_dimp\_mov é gravado no arquivo \(sem grupamento\)\.

__Correções no código da package:__

1\) Cursor: cur\_dimp

Ordenação será por: cli\_cod\_fis\_jur \+ parc\_cod\_fis\_jur \+ ind\_comex \+ cod\_mcapt \+ dat\_oper \+ cnpj\_adqui \+ hora \+ situacao

Corrigir os grupamentos de valores que vão para o 1100, 1110:

\- substituir o ident\_parceira por parc\_cod\_fis\_jur

\- substituir o ident\_cliente por cli\_cod\_fis\_jur

\- no tot\_vlr\_trans\_dia acrescentar cod\_mcapt \+ cnpj\_adqui

\- no tot\_qtd\_trans\_dia acrescentar cod\_mcapt \+ cnpj\_adqui

    

   sum\(dimp\.vlr\_oper\)  over \(partition by dimp\.cod\_empresa, dimp\.cod\_estab, dimp\.ident\_parceira, dimp\.ident\_cliente, dimp\.ind\_comex\) tot\_vlr\_oper,

   SUM\(dimp\.qtd\_total\) over \(partition by dimp\.cod\_empresa, dimp\.cod\_estab, dimp\.ident\_parceira, dimp\.ident\_cliente, dimp\.ind\_comex\) tot\_qtde,

   sum\(dimp\.vlr\_oper\)  over \(partition by dimp\.cod\_empresa, dimp\.cod\_estab, dimp\.ident\_parceira, dimp\.ident\_cliente, dimp\.ind\_comex, dimp\.id\_transac\_compl\) tot\_vlr\_tran\_compl,

   sum\(dimp\.qtd\_total\) over \(partition by dimp\.cod\_empresa, dimp\.cod\_estab, dimp\.ident\_parceira, dimp\.ident\_cliente, dimp\.ind\_comex, dimp\.id\_transac\_compl\) tot\_qtd\_tran\_compl,

   sum\(dimp\.vlr\_oper\) over \(partition by dimp\.cod\_empresa, dimp\.cod\_estab, dimp\.ident\_parceira, dimp\.ident\_cliente, dimp\.ind\_comex, dimp\.dat\_oper\) tot\_vlr\_trans\_dia,

   sum\(dimp\.qtd\_total\) over \(partition by dimp\.cod\_empresa, dimp\.cod\_estab, dimp\.ident\_parceira, dimp\.ident\_cliente, dimp\.ind\_comex, dimp\.dat\_oper\) <a id="_Hlk93051835"></a>tot\_qtd\_trans\_dia

2\) Na rotina Executar, corrigir as quebras dos registros 1100, 1110:

__Registro 1100:__

Alterar o IF marcado abaixo <a id="_Hlk93052179"></a>para que a comparação seja com os campos: cli\_cod\_fis\_jur \+ parc\_cod\_fis\_jur \+ ind\_comex 

Alterar a pChaveOrdenacao marcada abaixo para conter os campos: cli\_cod\_fis\_jur \+ parc\_cod\_fis\_jur \+ ind\_comex 

  if nvl\(vs\_cod\_chave\_ant,''\) <> \(nvl\(rdimp\(x\)\.ident\_parceira, ''\) || ';' || rdimp\(x\)\.ident\_cliente  || ';' ||  nvl\(rdimp\(x\)\.ind\_comex, ''\)\)  then

                  

                vs\_arquivo := '|1100|' ||

                              rdimp\(x\)\.parc\_cod\_fis\_jur || '|' ||

                              rdimp\(x\)\.cli\_cod\_fis\_jur || '|' ||

                              rdimp\(x\)\.ind\_comex || '|' ||

                              rdimp\(x\)\.ind\_extemp || '|' ||

                              to\_char\(pdataini, 'yyyymmdd'\) || '|' ||

                              to\_char\(pdatafim, 'yyyymmdd'\) || '|' ||

                              formata\_valor\(rdimp\(x\)\.tot\_vlr\_oper, 'V'\) || '|' ||

                              formata\_valor\(rdimp\(x\)\.tot\_qtde, 'Q'\) || '|';

                LIB\_PROC\.add\(vs\_arquivo, ptipo => vn\_arq, ppag => 1, plin=> 1, pChaveOrdenacao => '1100|' ||rdimp\(x\)\.ident\_parceira || '|' ||rdimp\(x\)\.ident\_cliente || '|' \);

                vn\_lin\_1   := vn\_lin\_1 \+ 1;

                insere\_qtd \('1100', 1\);

                  

          *\-\-    end if;*

  END IF;

__Registro 1110:__

Alterar o IF marcado abaixo para que a comparação seja com os campos: cli\_cod\_fis\_jur \+ parc\_cod\_fis\_jur \+ ind\_comex \+ cod\_mcapt \+ dat\_oper \+ cnpj\_adqui

Alterar a pChaveOrdenacao marcada abaixo para conter os campos: cli\_cod\_fis\_jur \+ parc\_cod\_fis\_jur \+ ind\_comex \+ cod\_mcapt \+ dat\_oper \+ cnpj\_adqui

IF rdimp\(x\)\.id\_transac\_compl is not null THEN 

                if nvl\(count\_oper\_1110\_w,0\) = 1 then

                  vs\_arquivo := '|1110|' ||

                                rdimp\(x\)\.cod\_mcapt || '|' ||

                                to\_char\(rdimp\(x\)\.dat\_oper, 'yyyymmdd'\) || '|' ||

                                formata\_valor\(rdimp\(x\)\.tot\_vlr\_tran\_compl, 'V'\) || '|' ||

                                formata\_valor\(rdimp\(x\)\.tot\_qtd\_tran\_compl, 'Q'\) || '|' ||

                                rdimp\(x\)\.cnpj\_adqui || '|';

                  LIB\_PROC\.add\(vs\_arquivo, ptipo => vn\_arq, ppag => 1, plin=> 1, pChaveOrdenacao => '1100|' ||rdimp\(x\)\.ident\_parceira || '|' ||rdimp\(x\)\.ident\_cliente || '|'|| nvl\(rdimp\(x\)\.id\_transac\_compl,''\) || '|'|| rdimp\(x\)\.hora */\*|| '|'|| rdimp\(x\)\.cod\_mcapt\*/* \);

                  vn\_lin\_1   := vn\_lin\_1 \+ 1;

                  insere\_qtd \('1110', 1\);

                  count\_oper\_1110\_w := 0;

                END IF;     

                count\_oper\_1110\_w := 1;

ELSE 

    if nvl\(to\_char\(dat\_oper\_ant\_w, 'yyyymmdd'\),0\) <> to\_char\(rdimp\(x\)\.dat\_oper, 'yyyymmdd'\)   then    

                  vs\_arquivo := '|1110|' ||

                                rdimp\(x\)\.cod\_mcapt || '|' ||

                                to\_char\(rdimp\(x\)\.dat\_oper, 'yyyymmdd'\) || '|' ||

                                formata\_valor\(rdimp\(x\)\.tot\_vlr\_trans\_dia, 'V'\) || '|' ||

                                formata\_valor\(rdimp\(x\)\.tot\_qtd\_trans\_dia, 'Q'\) || '|' ||

                                rdimp\(x\)\.cnpj\_adqui || '|';

                  LIB\_PROC\.add\(vs\_arquivo, ptipo => vn\_arq, ppag => 1, plin=> 1, pChaveOrdenacao => '1100|' ||rdimp\(x\)\.ident\_parceira || '|' ||rdimp\(x\)\.ident\_cliente || '|'|| rdimp\(x\)\.hora || '|'*/\*|| rdimp\(x\)\.cod\_mcapt\*/* \);

                  vn\_lin\_1   := vn\_lin\_1 \+ 1;

                  insere\_qtd \('1110', 1\);

                  count\_oper\_1110\_w := 0;

end if;             

END IF;

__Registro 1115:__

Alterar a pChaveOrdenacao marcada abaixo para conter os campos: cli\_cod\_fis\_jur \+ parc\_cod\_fis\_jur \+ ind\_comex \+ cod\_mcapt \+ dat\_oper \+ cnpj\_adqui \+ hora \+ situacao

             vs\_arquivo := '|1115|' ||

                          rdimp\(x\)\.seq\_nsu || '|' ||

                          rdimp\(x\)\.cod\_autorizacao || '|' ||

                          rdimp\(x\)\.id\_transacao || '|' ||

                          rdimp\(x\)\.ind\_split || '|' ||

                          rdimp\(x\)\.bandeira || '|' ||

                          lpad\(replace\(rdimp\(x\)\.hora, ':', ''\), 6, '0'\) || '|' ||

                          formata\_valor\(rdimp\(x\)\.vlr\_oper, 'V'\) || '|' ||

                          rdimp\(x\)\.IND\_OPER\_NAT\_PAG || '|' ||

                          rdimp\(x\)\.cod\_geo || '|';

             LIB\_PROC\.add\(vs\_arquivo, ptipo => vn\_arq, ppag => 1, plin=> 1, pChaveOrdenacao => '1100|' ||rdimp\(x\)\.ident\_parceira || '|' ||rdimp\(x\)\.ident\_cliente || '|'|| rdimp\(x\)\.hora || '|'||rdimp\(x\)\.cod\_mcapt  \) ;             

             vn\_lin\_1   := vn\_lin\_1 \+ 1;

__Registro 1120__

Alterar a pChaveOrdenacao marcada abaixo para conter os campos: cli\_cod\_fis\_jur \+ parc\_cod\_fis\_jur \+ ind\_comex \+ cod\_mcapt \+ dat\_oper \+ cnpj\_adqui \+ hora \+ situacao \+ rdimp\(x\)\.cli\_uf \+ rdimp\(x\)\.num\_autentic\_nfe

IF rdimp\(x\)\.cnpj\_destino is not null OR rdimp\(x\)\.cpf\_destino is not null OR rdimp\(x\)\.COD\_DEST is not null then

               *\-\- colocar um if para verificar se vai montar este registro com layout 6 ou 7 que adiciona mais dois campos NFSE DCE*

               vs\_arquivo := '|1120|' ||

                            rdimp\(x\)\.cli\_uf || '|' ||

                            rdimp\(x\)\.num\_autentic\_nfe || '|' ||

                            rdimp\(x\)\.cnpj\_destino || '|' ||

                            rdimp\(x\)\.cpf\_destino || '|' ||

                            rdimp\(x\)\.COD\_DEST || '|' ||

                            rdimp\(x\)\.cod\_chave\_nfse || '|' ||

                            rdimp\(x\)\.cod\_chave\_dce  || '|' ||

                            rdimp\(x\)\.uf\_origem || '|' ||

                            rdimp\(x\)\.cnpj\_origem || '|';

               LIB\_PROC\.add\(vs\_arquivo, ptipo => vn\_arq, ppag => 1, plin=> 1, pChaveOrdenacao => '1100|' ||rdimp\(x\)\.ident\_parceira || '|' ||rdimp\(x\)\.ident\_cliente || '|'|| rdimp\(x\)\.hora || '|'||rdimp\(x\)\.cod\_mcapt || '|'|| <a id="_Hlk93053007"></a>rdimp\(x\)\.cli\_uf || '|' ||rdimp\(x\)\.num\_autentic\_nfe\);

               vn\_lin\_1   := vn\_lin\_1 \+ 1;

               insere\_qtd \('1120', 1\);

END IF;

Obsevação:

- Acho que os campos que compões a chave \(pChaveOrdenacao\) devem ser formatados com o tamanho do campo \(to\_char\(campo, tamanho\)\), para que a ordenação do arquivo funcione\.

