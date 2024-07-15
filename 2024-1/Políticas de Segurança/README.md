# Políticas de Segurança

## O que é Backup

Backup é o processo de fazer uma cópia dos dados ou das configurações do seu sistema para protegê-los. O backup é uma cópia de segurança que é armazenada separadamente da original, com o fim de evitar perdas ocasionadas por imprevistos, como erros humanos, falhas computacionais e de segurança, ou desastres naturais.

Os imprevistos podem impactar no tempo de inatividade não planejada de um negócio, o que pode resultar rapidamente em perda de receita em muitos setores. Qualquer tempo de inatividade pode inviabilizar interações com o cliente, prejudicar a produtividade de funcionários SAP, destruir dados e interromper processos de negócios.

## O que é recuperação de desastres? 

Recuperação de desastres refere-se ao plano e aos processos para restabelecer rapidamente o acesso a aplicativos, dados e recursos de TI após uma indisponibilidade ocasionada por um imprevisto.

Esse plano pode envolver migrar para um conjunto redundante de servidores e sistemas de armazenamento até que seu data center principal esteja funcional novamente.

## Backup e recuperação de desastres 

Backup e recuperação de desastres servem para criar uma cópia de segurança de dados e criar procedimentos para acessar esses dados em caso de imprevistos.

Em caso de que ocorra uma grande indisponibilidade, é essencial ter uma **cópia dos dados (backup)**. Porém, ter apenas o backup não significa que você pode manter sua empresa em funcionamento.

Para assegurar a continuidade dos negócios, também é necessário ter um **plano de recuperação de desastres** robusto e comprovado. Isso ajudará a acessar e utilizar os dados para reestabelecer o funcionamento dos sistemas da empresa.

## A importância do planejamento 

Sua organização não pode se dar ao luxo de negligenciar backups ou a recuperação de desastres. Caso a recuperação de dados perdidos após uma exclusão acidental demore horas, seus funcionários ou parceiros ficarão ociosos, incapazes de concluir processos críticos que dependem de sua tecnologia.

Caso o processo de recuperação de seu negócios demore dias após um desastre, é possível que você perca clientes permanentemente. Dada a quantia de tempo e capital que você pode perder em ambos os casos, os investimentos em backup e recuperação de desastres são totalmente justificados.

----

# Tipos de armazenamento de backup 

A melhor maneira de realizar um plano de backup e recuperação de desastres na sua empresa pode variar de acordo com cada carga de trabalho presente nos negócios.

Para um grande banco, por exemplo, o sistema bancário on-line pode ser uma carga de trabalho crítica, pois o banco precisa minimizar o tempo de inatividade e a perda de dados. No entanto, o aplicativo de monitoramento de tempo dos funcionários do banco é menos importante. No caso de um desastre, o banco pode permitir que o aplicativo fique indisponível por várias horas, ou até mesmo um dia, sem impacto negativos nos negócios. Definir as cargas de trabalho como Nível 1, Nível 2 ou Nível 3 pode ajudar a fornecer um framework para seu plano de recuperação de desastres.

## Opções de implementação

A próxima etapa na elaboração de um plano de recuperação de desastres é avaliar as opções de implementação. É necessário manter alguma função de recuperação de desastres ou dados de backup no local? Haveria algum benefício de uma abordagem usando uma cloud pública ou cloud pública?

- [cloud pública](https://www.ibm.com/br-pt/cloud)
- [cloud pública](https://www.ibm.com/br-pt/hybrid-cloud)

### Cloud

As soluções de backup e recuperação de desastres baseadas na cloud estão se tornando cada vez mais conhecidas entre organizações de todos os portes. Muitas soluções na cloud oferecem a infraestrutura para armazenar dados e, em certos casos, as ferramentas para gerenciar processos de backup e recuperação de desastres.

Ao selecionar uma solução de backup ou recuperação de desastres baseada na cloud, você estará economizando um investimento inicial de capital em infraestrutura, além dos custos de gerenciamento do ambiente. Além disso, você ganha escalabilidade rápida, juntamente com a distância geográfica necessária para manter os dados seguros no caso de um desastre regional.

As soluções de backup e recuperação de desastres baseadas na cloud oferecem suporte a ambientes de produção tanto no local quanto baseados na cloud. Você pode, por exemplo, optar por armazenar na cloud apenas os dados de backup ou replicados, enquanto mantém seu ambiente de produção em seu próprio data center. Com esta abordagem híbrida, você ainda terá as vantagens de escalabilidade e distância geográfica, sem ter que migrar seu ambiente de produção. No modelo cloud-to-cloud, tanto a produção quanto a recuperação de desastres estão localizadas na cloud, porém em locais diferentes, para assegurar suficiente separação física.

### No local

Em alguns casos, manter alguns processos de backup ou recuperação de desastres no local pode ajudar a recuperar dados e serviços de TI mais rapidamente. Manter uma certa quantidade de dados sensíveis no local também pode ser recomendado caso seja necessário cumprir regulamentações rígidas de privacidade ou soberania de dados.

Para a recuperação de desastres, ter um plano que dependa totalmente de um ambiente no local é algo arriscado. Caso ocorra um desastre natural ou indisponibilidade de energia, todo o seu data center, com os sistemas primários e secundários, seria afetado. É por essa razão que a maioria das estratégias de recuperação de desastres utilizam um site secundário geograficamente afastado do data center principal. Você pode localizar esse outro site na outra ponta da cidade, do país ou do outro lado do mundo, dependendo de como decidir equilibrar fatores como desempenho, conformidade regulamentar e acessibilidade física ao site secundário.

### Tecnologias

Dependendo das opções de implementação escolhidas, você terá diversas alternativas para os tipos de tecnologias e processos empregados para backup e recuperação de desastres.

### Fitas LTO tradicionais

Embora exista há décadas, o armazenamento em fitas magnéticas tradicionais ainda tem espaço em seu plano de backup. Com uma solução de fita, é possível armazenar uma grande quantidade de dados de forma confiável e com custo reduzido.

Embora a fita possa ser eficiente para backups, ela não é usada geralmente para recuperação de desastres, que requer um tempo de acesso mais rápido da área de armazenamento baseada em disco. Além disso, caso precise recuperar uma fita fisicamente de um local externo, você poderia perder diversas horas ou até mesmo dias de disponibilidade.

- [armazenamento em fitas](https://www.ibm.com/br-pt/tape-storage)

### Replicação baseada em captura instantânea
 
Um backup baseado em captura instantânea captura o estado de um aplicativo ou disco em certo momento. Ao gravar apenas os dados alterados desde a última captura instantânea, este método pode ajudar a proteger os dados enquanto conserva espaço de armazenamento.

A replicação baseada em captura instantânea pode ser usada para backup ou recuperação de desastres. Logicamente, a quantidade recuperável de dados depende da sua última captura instantânea. Caso faça capturas instantâneas a cada hora, você deve estar disposto a perder uma hora de dados.
 
### Replicação contínua
 
Muitas organizações estão adotando a replicação contínua para a recuperação de desastres e backup. Com esse método, a cópia mais recente de um disco ou aplicativo é replicada de maneira contínua para outro local ou para a cloud, minimizando o tempo de inatividade e proporcionando pontos de recuperação mais granulares.

----

# Termos-Chave

Entender alguns termos essenciais pode ajudar a dar forma às suas decisões estratégicas e permitir uma melhor avaliação das soluções de backup e recuperação de desastres.

- **Objetivo do tempo de recuperação (RTO)** é a quantidade de tempo necessária para recuperar operações de negócios normais após uma indisponibilidade. Ao definir seu RTO, será necessário considerar quanto tempo você está disposto a perder, assim como o impacto que esse tempo terá em seus resultados. O RTO pode variar muito de um tipo de negócio para outro. Por exemplo, se uma biblioteca pública perder seu sistema de catálogo, é provável que ela continue funcionando manualmente por alguns dias enquanto os sistemas são restaurados. Mas se um grande varejista on-line perder seu sistema de inventário, até mesmo dez minutos de tempo de inatividade, e a perda de receita associada, seriam inaceitáveis.

- **Objetivo do ponto de recuperação (RPO)** refere-se à quantidade de dados que você está disposto a perder em um desastre. Pode ser necessário copiar dados para um data center remoto de forma contínua  para que uma indisponibilidade não resulte em nenhuma perda de dados. Ou você pode decidir que perder cinco minutos ou uma hora de dados seria aceitável.

- **Failover** é o processo da recuperação de desastres que transfere tarefas automaticamente para sistemas de backup de maneira ininterrupta para os usuários. Você pode fazer failover de seu data center primário para um site secundário, com sistemas redundantes que estejam prontos para assumir o controle imediatamente.

- **Failback** é o processo de recuperação de desastres de voltar aos sistemas originais. Assim que o desastre tiver passado e seu data center principal voltar a funcionar, você também deve ser capaz de fazer o failback sem dificuldades.

- **Restauração** é o processo de transferir os dados de backup para seu sistema ou data center principal. O processo de restauração é geralmente considerado parte do backup e não da recuperação de desastres.

Um último termo pode ser útil ao considerar alternativas para gerenciar seus processos de recuperação de desastres e seu ambiente de recuperação de desastres:

- **Recuperação de desastres como serviço (DRaaS)** é uma abordagem gerenciada para a recuperação de desastres. Um fornecedor terceiro hospeda e gerencia a infraestrutura utilizada para a recuperação de desastres. Algumas soluções DRaaS podem oferecer ferramentas para gerenciar os processos de recuperação de desastres ou permitir que organizações terceirizem o gerenciamento.
