Um **port scanner** é uma ferramenta usada para identificar portas abertas em um computador ou dispositivo em uma rede. As portas abertas indicam que o serviço ou a aplicação correspondente está disponível e escutando por conexões. Port scanners são usados principalmente para fins de segurança, administração de rede e diagnóstico.

### Como Funciona um Port Scanner

1. **Varredura de Portas**: O port scanner envia pacotes para um range específico de portas em um alvo (endereço IP ou hostname).
2. **Resposta do Alvo**: Dependendo da resposta recebida (ou ausência de resposta), o scanner determina se a porta está aberta, fechada ou filtrada.
   - **Porta Aberta**: Indica que a porta está aceitando conexões.
   - **Porta Fechada**: Indica que a porta não está aceitando conexões.
   - **Porta Filtrada**: Não há resposta, possivelmente indicando que um firewall ou sistema de segurança está bloqueando o acesso.

### Tipos de Varredura de Portas

1. **TCP Connect Scan**: Estabelece uma conexão completa com a porta (conexão TCP de três vias).
2. **TCP SYN Scan (Half-open Scan)**: Envia apenas o pacote SYN e espera pelo SYN-ACK. Não completa a conexão, sendo menos detectável.
3. **UDP Scan**: Envia pacotes UDP para as portas e espera por respostas ICMP de destino inalcançável para determinar portas fechadas.
4. **Xmas Scan**: Envia pacotes com os flags FIN, URG, e PSH ativos, podendo revelar portas abertas em alguns sistemas.
5. **ACK Scan**: Envia pacotes ACK, útil para mapear regras de firewall.

### Usos de um Port Scanner

1. **Auditoria de Segurança**: Identificar serviços vulneráveis e portas desnecessariamente abertas.
2. **Administração de Rede**: Monitorar e gerenciar os serviços ativos na rede.
3. **Diagnóstico de Problemas**: Identificar problemas de conectividade e configuração de rede.

### Ferramentas Comuns de Port Scanning

1. **Nmap (Network Mapper)**: Ferramenta de varredura de portas muito popular e poderosa, usada para detecção de rede e auditoria de segurança.
2. **Netcat (nc)**: Ferramenta simples e versátil para leitura e gravação em conexões de rede.
3. **Masscan**: Um scanner de portas extremamente rápido, capaz de escanear toda a Internet em minutos.

### Exemplo de Uso do Nmap

Para escanear portas comuns de um host específico:

```sh
nmap -p 1-1000 192.168.1.1
```

Para realizar um TCP SYN scan:

```sh
nmap -sS 192.168.1.1
```

Para identificar serviços em execução e suas versões:

```sh
nmap -sV 192.168.1.1
```

### Considerações Legais e Éticas

Embora os port scanners sejam ferramentas úteis, o uso não autorizado em redes de terceiros pode ser ilegal e considerado uma tentativa de invasão. É crucial obter permissão antes de realizar varreduras em sistemas que você não possui ou administra.

### Resumo

Um port scanner é uma ferramenta essencial para segurança de rede e administração, permitindo identificar portas abertas e os serviços associados. Usado corretamente, pode ajudar a proteger e gerenciar uma rede, mas deve ser usado com responsabilidade e dentro dos limites legais.