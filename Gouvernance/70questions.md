# 70 questions pour auditeur un SI

### Formations
1. Organisez-vous des formations solides et fréquentes de sensibilisation à la cybersécurité pour les utilisateurs finaux ?
2. Avez-vous appris à tout le monde comment stocker en toute sécurité les mots de passe ou les phrases secrètes ?
3. Menez-vous des campagnes trimestrielles anti-phishing, smishing et vishing ?
4. Tous les membres de votre organisation comprennent-ils le risque associé à la cybersécurité, les stratagèmes courants utilisés par les acteurs malveillants et la manière de signaler toute activité suspecte pour une enquête plus approfondie ?

### Contrôle d'accès
5. Tous les comptes par défaut des fournisseurs ont-ils été modifiés ou désactivés ?
6. Seuls les services, protocoles, démons3 et fonctions nécessaires sont-ils activés ?
7. Toutes les fonctionnalités inutiles sont-elles supprimées ou désactivées ?
8. Tous les comptes sont-ils immédiatement désactivés ou supprimés à la fin de l'emploi ?
9. Tous les temps d'inactivité de l'écran sont-ils définis sur 15 minutes et nécessitent-ils une nouvelle authentification pour être déverrouillés ?

### Utilisateur final
10. Fournissez-vous aux utilisateurs finaux un outil pour enregistrer tous les mots de passe (de préférence basé sur le cloud pour une utilisation à domicile et au travail) ?
11. Avez-vous développé une politique de mot de passe ou de phrase secrète d'administrateur (admin) et d'utilisateur qui élimine l'utilisation de mots de passe courants ou faciles à deviner ?

### Points de fin
12. Tous les journaux des points finaux sont-ils ingérés par une technologie intelligente qui utilise les renseignements sur les menaces et l'intelligence artificielle (IA) en fonction des activités et des heuristiques des acteurs menaçants ?
13. Renforcez-vous tous les points de terminaison et supprimez-vous tout ce qui n'est pas nécessaire à la fonctionnalité du travail ?
14. Disposez-vous d'une protection anti-malware de nouvelle génération (par exemple, détection et réponse gérées [MDR], détection et réponse étendues [XDR], détection et réponse des points de terminaison [EDR])4 sur tous les points de terminaison qui utilisent une sécurité basée sur les renseignements sur les menaces. une plateforme d'analyse avec un contexte de sécurité intégré ?
15. Empêchez-vous les appareils sécurisés et non contrôlés par l'entreprise de se connecter à n'importe quelle partie de votre réseau ?
16. Tous les points finaux disposent-ils de pare-feu personnels pour accéder à Internet lorsqu'ils ne sont pas connectés au réseau de l'entreprise ?
17. Tous les points finaux sont-ils équipés d'un logiciel antivirus qui ne peut pas être désactivé et qui est automatiquement mis à jour lorsque de nouvelles mises à jour sont disponibles ?
18. Une application anti-malware de nouvelle génération est-elle installée sur tous les points finaux ?

### Gestion d'événements
19. Tous les journaux sont-ils conservés pendant au moins 2 ans ?
20. Tous les appareils génèrent-ils des journaux ?
21. Tous les journaux sont-ils examinés quotidiennement par des sources internes et/ou externes ?
22. Disposez-vous d'une réponse aux incidents de cybersécurité mature et bien organisée (en interne ou en collaboration avec des tiers) qui enquête de manière approfondie sur tous les incidents ?

### Architecture de sécurité
23. Donnez-vous uniquement aux employés les outils et l'accès nécessaires à l'exercice de leurs fonctions, et rien d'autre ?
24. Utilisez-vous le principe du moindre privilège ?
25. Déployez-vous un modèle zéro confiance ?
26. Exigez-vous une authentification multifacteur (MFA) pour toutes les connexions en dehors du réseau ?
27. Exigez-vous l'authentification multifacteur pour que les utilisateurs internes du réseau authentifiés puissent accéder à l'infrastructure et aux données clés à l'intérieur du réseau (c'est-à-dire les joyaux de la couronne) ?
28. Gérez-vous toutes les informations d'identification dans un ordre qui vous permet d'effectuer rapidement une réinitialisation du mot de passe pour chaque compte de votre réseau ? (Cela inclut les comptes de service.)
29. Avez-vous récemment évalué votre Active Directory pour vous assurer qu'il est correctement configuré et sécurisé ?
30. Surveillez-vous activement la sécurité de votre Active Directory ?
31. Vos pare-feux périmétriques ont-ils une règle de refus total, sauf autorisation contraire ?
32. Votre zone démilitarisée (DMZ) est-elle sécurisée ?
33. A-t-on été assuré qu'il n'y a pas de données, de bases de données ou de comptes stockés dans la DMZ ?
34. Déployez-vous une technologie anti-usurpation d'identité pour empêcher les fausses adresses IP d'entrer dans le réseau ?
35. Empêchez-vous la divulgation de l'adresse IP interne et des informations de routage sur Internet ?
36. Segmentez-vous l'infrastructure clé des autres parties du réseau avec des pare-feu restrictifs (par exemple, en segmentant le WiFi, les données confidentielles, les machines virtuelles et les imprimantes loin des joyaux de la couronne) ?

### Cryptographie
37. Des procédures sont-elles définies et mises en œuvre pour protéger les clés cryptographiques utilisées pour protéger les données stockées contre la divulgation et l'utilisation abusive ?
38. Les clés cryptographiques sont-elles stockées dans le moins d'endroits possibles avec au moins deux dépositaires ?
39. Utilisez-vous le chiffrement complet du disque sur tous les lecteurs appropriés ?
40. Utilisez-vous un chiffrement sécurisé en transit, au moins Transport Layer Security (TLS) 1.1 ou supérieur ?
41. Tous les accès administratifs hors console sont-ils chiffrés à l’aide d’une cryptographie forte ?

### Des menaces
42. Effectuez-vous périodiquement des chasses ciblées aux menaces ?
43. Bénéficiez-vous d'informations actuelles sur les menaces (de préférence provenant de plusieurs sources) et disposez-vous d'une procédure pour mettre en œuvre des contre-mesures rapides basées sur de bonnes informations sur les menaces ?
44. Cela implique-t-il d'effectuer une reconnaissance de routine du Dark Web pour découvrir ce qui existe sur le Dark Web concernant votre marque et les structures de votre entreprise ?
45. Surveillez-vous de près toutes les connexions de la chaîne d'approvisionnement des fournisseurs et des tiers pour vérifier leur conformité et les problèmes indésirables ?

### Tests
46. Effectuez-vous au moins 1 test d'intrusion par an, réalisé par un tiers ?
47. Effectuez-vous des analyses de vulnérabilité de routine et corrigez-vous toutes les vulnérabilités avec un score CVSS (Common Vulnerability Scoring System) de 4 ou plus dans les 30 jours, et toutes les autres vulnérabilités dans les 90 jours ?
48. Analysez-vous régulièrement votre infrastructure Internet à la recherche de pénétrations et de vulnérabilités ?
49. Effectuez-vous un rapport annuel d’analyse de l’impact sur les activités/d’analyse des risques avec des auditeurs internes et externes ?

### Politique
50. Disposez-vous d'une politique de sécurité d'entreprise mise à jour au moins une fois par an et comprise par toutes les parties auxquelles elle s'applique ?
51. Avez-vous une politique formelle de contrôle des changements ?

### Physique
52. Des processus et mécanismes permettant de restreindre l'accès physique aux serveurs, aux consoles, aux équipements de sauvegarde et de réseau sont-ils en place et correctement protégés ?
53. Des contrôles physiques et/ou logiques sont-ils mis en œuvre pour restreindre l'utilisation de prises réseau accessibles au public dans les installations ?

Des plans
54. Disposez-vous d'un bon plan de réponse aux cyberincidents (CIRP) qui est révisé et mis en pratique chaque année ? Le CIRP doit être régulièrement mis à jour, et les équipes de réponse aux incidents principales et élargies doivent s'entraîner à réagir au moins une fois par an à l'aide d'exercices de cybersécurité sur table ou fonctionnels.
55. Disposez-vous de manuels contenant des instructions techniques pour gérer les incidents de cybersécurité courants ?

### Inventaire
56. Disposez-vous de schémas détaillés de l'ensemble du réseau, y compris le WiFi ?
57. Disposez-vous d'un inventaire complet de tous les actifs comprenant les niveaux de criticité de l'entreprise, les propriétaires, les copropriétaires et la restauration ? Cet inventaire comprend-il des instructions avec des délais de récupération ?
58. Disposez-vous d'un ensemble complet de diagrammes de flux de données ?

### Gestion de données
59. Utilisez-vous la surveillance de l'intégrité des fichiers (FIM) pour les joyaux de la couronne de l'organisation ?
60. Le stockage des données confidentielles est-il réduit au minimum et supprimé en toute sécurité une fois qu’elles ne sont plus nécessaires ?
61. Avez-vous besoin d'une classification des données sur l'ensemble du réseau ?
62. Déployez-vous un programme de prévention des pertes de données (DLP) réseau et cloud partout où résident des données confidentielles ?
63. Empêchez-vous que les données confidentielles soient copiées sur des appareils externes et que les appareils externes soient connectés aux points finaux ?

### Développement de logiciels
64. Les processus et mécanismes de développement et de maintenance de systèmes et de logiciels sécurisés sont-ils définis et compris ?
65. Des techniques d'ingénierie logicielle ou d'autres méthodes sont-elles définies et utilisées par le personnel de développement de logiciels pour prévenir ou atténuer les attaques logicielles courantes et les vulnérabilités associées dans tous les logiciels ?
66. En ce qui concerne les applications Web destinées au public, les nouvelles menaces et vulnérabilités sont-elles régulièrement traitées ?
67. Ces applications sont-elles protégées contre les attaques ?
68. Les environnements de préproduction sont-ils séparés des environnements de production, et la séparation est-elle renforcée par des contrôles d'accès ?

### Appareils mobiles
69. Tous les appareils mobiles sont-ils régis par des politiques efficaces de gestion des appareils mobiles (MDM) ?
70. Interdisez-vous toute connectivité des appareils mobiles non contrôlés par les mécanismes de sécurité de l'entreprise ?