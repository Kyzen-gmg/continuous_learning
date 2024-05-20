Chapter 4 Network Security

# Learning Objectives
By the end of this chapter, you should be able to:
- Describe the threat environment, including types of attacks and types of attackers.
- Explain how to protect dialogues by cryptography, including encryption for confidentiality, electronic signatures, and host-to-host virtual private networks (VPNs).
- Evaluate alternative authentication mechanisms, including passwords, smart cards, biometrics, digital certificate authentication, and two-factor authentication.
- Describe firewall protection, including stateful packet inspection, next-generation firewalls, and related intrusion prevention systems.
- Describe the role of antivirus protection.


https://krebsonsecurity.com/2014/02/these-guys-battled-blackpos-at-a-retailer/
https://start.cybervista.net/hubfs/Resolve%20Assets/CyberVista%20Case%20Study_2013%20Target%20Breach.pdf
https://krebsonsecurity.com/2014/02/target-hackers-broke-in-via-hvac-company/

# The POS Attack
![](img/ch4_01.jpg)

![](img/ch4_02.jpg)

1. Spear Phishing on Fazio Mechanical Services employee to get creds on a vendor server that handled electronic billing and other matters.
2. BlacKPOS malware, $2k worth at the time in blackmarket.
3. Test Farm + modified payload to target Target's POS terminals
4. Malware was a RAM scraper, very selective and only data on the magnetic stipes of swiped cards.
5. Data collected went to legit Target servers but also to a compromised holding server
6. Data was exfild using another server that was specifically used for delivering data to the attackers outside Target's network
7. Extrusion server pulled batches of card data sets from the holding server and transmitted them to landing servers in Russa, Brazil, Miami, and other locations. The thieves could not conceal the IP addresses of the landing servers, so they probably moved the data quickly to other servers.
8. Attackers then monetized the stolen data. They wholesaled batches of data to online card shops that then sold the data to counterfeiters--these card shops held stripe information in a searchable database.
9. CCFers even use the card data to create fake credit cards that looked legit down to the graphics used by individual banks. They then copied data from a single legi card onto the magnetic stripe of each counterfeit card. This allowed them to purchase high-end merchandise and then sell the merchandise to traditional fences. However, the ccfers did not make the purchases themselves. Instead, they hired a small corps of "mules" to make the actual purchases or take cash out of ATMs.

*One thing is missing from the figure. The attacks needed to transmit control messages frequently into the Target network in order to compromise servers and take actions to direct actions on these servers during the attack. All of these messages had to go through Target's firewalls. It was critical for the attackers to maintain a hole in the victim's firewalls during the entire attack process.*

**CCFers normally only create a single card master from which all counterfeit cards in a batch are made. All ccc in the batch have the same printed name, cc number, exp date, and other information. The magnetic stripe data, however, will be specific to a single compromised credit card. This is why store clerks look at the last four digits of the card number on the physical credit card. If this is diff from information on the magnetic stripe, the card is fraudulent.**

# Perspective
**Network thinking focuses on software bugs and mechanical breakdowns. In contrast, security thinking must anticipate the actions of intelligent adversaries who will try many things to succeed and adapt to the defenses you put in place.**

**"Security is a process, not a product"**

![](img/ch4_03.jpg)

![](img/ch4_04.jpg)

