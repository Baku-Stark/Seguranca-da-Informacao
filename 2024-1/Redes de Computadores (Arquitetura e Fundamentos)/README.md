# Redes de Computadores (Arquitetura e Fundamentos)

### O que é uma Rede de Computadores?

Uma rede de computadores é um conjunto de computadores e dispositivos conectados entre si para compartilhar recursos e informações. Esses dispositivos podem incluir computadores, servidores, roteadores, switches, e outros equipamentos de rede. A conexão pode ser feita por meio de cabos (rede cabeada) ou sem fio (rede sem fio).

### Arquitetura de Redes de Computadores

A arquitetura de rede refere-se ao design e layout de uma rede, incluindo a topologia física e lógica, os protocolos usados e as camadas de comunicação. As arquiteturas de rede mais comuns são baseadas no modelo OSI (Open Systems Interconnection) e no modelo TCP/IP (Transmission Control Protocol/Internet Protocol).

#### 1. **Modelo OSI (Open Systems Interconnection)**
O modelo OSI é um modelo de referência com sete camadas que define como os dados devem ser transmitidos em uma rede.

- **Camada 1: Física**
  - Define as características físicas do meio de transmissão, como cabos e conectores.
  - Protocolos e tecnologias: Ethernet, Wi-Fi, USB.

- **Camada 2: Enlace de Dados**
  - Responsável pela transferência de dados entre dispositivos na mesma rede.
  - Protocolos: Ethernet, Wi-Fi (IEEE 802.11), PPP (Point-to-Point Protocol).

- **Camada 3: Rede**
  - Responsável pelo roteamento de pacotes de dados entre redes diferentes.
  - Protocolos: IP (Internet Protocol), ICMP (Internet Control Message Protocol).

- **Camada 4: Transporte**
  - Garante a entrega confiável dos dados entre hosts.
  - Protocolos: TCP (Transmission Control Protocol), UDP (User Datagram Protocol).

- **Camada 5: Sessão**
  - Gerencia e controla as conexões entre computadores.
  - Protocolos: NetBIOS, RPC (Remote Procedure Call).

- **Camada 6: Apresentação**
  - Converte dados entre formatos de aplicação e de rede.
  - Protocolos: SSL/TLS (Secure Sockets Layer/Transport Layer Security).

- **Camada 7: Aplicação**
  - Interface direta para os serviços de rede que os usuários finais acessam.
  - Protocolos: HTTP, FTP, SMTP (Simple Mail Transfer Protocol).

#### 2. **Modelo TCP/IP**
O modelo TCP/IP é mais simples e tem quatro camadas:

- **Camada 1: Acesso à Rede (Link)**
  - Combina as camadas Física e de Enlace de Dados do modelo OSI.
  - Protocolos: Ethernet, Wi-Fi.

- **Camada 2: Internet**
  - Equivalente à camada de Rede do modelo OSI.
  - Protocolos: IP, ICMP.

- **Camada 3: Transporte**
  - Equivalente à camada de Transporte do modelo OSI.
  - Protocolos: TCP, UDP.

- **Camada 4: Aplicação**
  - Combina as camadas Sessão, Apresentação e Aplicação do modelo OSI.
  - Protocolos: HTTP, FTP, SMTP, DNS (Domain Name System).

### Fundamentos de Redes de Computadores

#### 1. **Protocolo**
Um conjunto de regras que define como os dados devem ser transmitidos e recebidos na rede. Exemplos incluem TCP/IP, HTTP, FTP e SMTP.

#### 2. **Topologia de Rede**
A disposição física ou lógica dos dispositivos na rede. As topologias mais comuns incluem:

- **Barramento (Bus)**
  - Todos os dispositivos estão conectados a um único cabo de comunicação.
  
- **Estrela (Star)**
  - Todos os dispositivos estão conectados a um switch ou hub central.

- **Anel (Ring)**
  - Cada dispositivo está conectado a dois outros dispositivos, formando um anel.

- **Malha (Mesh)**
  - Todos os dispositivos estão interconectados.

#### 3. **Endereçamento**
Métodos para identificar dispositivos na rede:

- **Endereço IP**
  - Identifica dispositivos de forma única em uma rede IP.
  - IPv4: 32 bits, formato decimal (ex: 192.168.1.1).
  - IPv6: 128 bits, formato hexadecimal (ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334).

- **Endereço MAC**
  - Identifica de forma única a interface de rede de um dispositivo.
  - Formato hexadecimal (ex: 00:1A:2B:3C:4D:5E).

#### 4. **Roteamento e Comutação**
- **Roteamento**
  - Processo de encaminhamento de pacotes de dados entre redes diferentes.
  - Dispositivos: Roteadores.

- **Comutação**
  - Processo de encaminhamento de quadros de dados dentro da mesma rede.
  - Dispositivos: Switches.

#### 5. **Segurança de Rede**
- **Firewalls**
  - Monitoram e controlam o tráfego de rede baseado em regras de segurança.

- **VPNs (Virtual Private Networks)**
  - Criam conexões seguras sobre redes públicas.

- **IDS/IPS (Intrusion Detection/Prevention Systems)**
  - Detectam e/ou previnem atividades maliciosas na rede.

#### 6. **Qualidade de Serviço (QoS)**
Mecanismos para garantir a entrega eficiente e oportuna de diferentes tipos de tráfego de rede, priorizando dados críticos.

### Resumo

Redes de computadores são essenciais para a comunicação e troca de dados entre dispositivos. A arquitetura de rede, baseada em modelos como o OSI e o TCP/IP, define como os dados são transmitidos. Fundamentos como protocolos, topologias, endereçamento, roteamento, comutação, segurança e QoS são cruciais para o funcionamento eficaz e seguro das redes.
