# XPath Extractor pour RobotFramework

✨ **Un outil simple et efficace pour récupérer les XPaths lors de l'utilisation de RobotFramework.** ✨

---

## 🚀 Objectif du Projet

Ce projet en Python permet d'extraire facilement des XPaths destinés à être utilisés avec RobotFramework. Malgré l'existence d'autres outils capables de réaliser cette tâche, ce script est né principalement de deux besoins :

- 🎯 **Apprentissage personnel** : Comprendre et maîtriser davantage Python, ainsi que la manipulation des XPaths.
- 🔐 **Contraintes professionnelles** : Contournement des restrictions d'installation logicielle imposées par des droits utilisateurs limités en entreprise.

---

## ⚙️ Fonctionnalités

- Extraction automatique des XPaths depuis des éléments HTML.
- Intégration facilitée avec RobotFramework.
- Légèreté et simplicité d'utilisation sans installation de logiciels tiers.

---

## 📦 Installation

Clonez ce dépôt :

```bash
git clone https://github.com/votre-utilisateur/xpath-robotframework.git
cd xpath-robotframework
```

Installez les dépendances :

```bash
pip install -r requirements.txt
```

---

## 💡 Utilisation

Exécutez simplement le script principal en spécifiant votre fichier HTML :

```bash
python xpath_extractor.py votre_fichier.html
```

---

## 🌟 Exemples

```python
from xpath_extractor import extract_xpath

xpath = extract_xpath('votre_fichier.html', 'élément recherché')
print(xpath)
```

---

## 🛠️ Dépendances

- Python 3.x
- BeautifulSoup
- lxml

---

## 📖 Contribution

Les contributions sont toujours les bienvenues ! N'hésitez pas à soumettre des pull requests ou à ouvrir des issues pour proposer des améliorations ou signaler des bugs.

---

## 📜 Licence

Ce projet est sous licence Beerware.

---

