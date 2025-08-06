# DataAnalysisX_API
Project: Data Analysis (University)

# 🐦 Twitter Themenanalyse: Region Frankfurt

Dieses Projekt untersucht mittels einer datengetriebenen Analyse die in Twitter-Nachrichten am häufigsten diskutierten Themen mit Bezug zur Region Frankfurt am Main. Grundlage dafür ist die Nutzung der offiziellen Twitter API v2 in Verbindung mit modernen Analyseverfahren aus dem Bereich Natural Language Processing (NLP).

---

## 🔍 Zielsetzung

Ziel des Projekts ist es, mithilfe öffentlich zugänglicher Twitter-Daten aktuelle Diskurs-Schwerpunkte zu identifizieren und inhaltlich einzuordnen. Dabei liegt der Fokus auf:

- der Identifikation der aktivsten Accounts (User ID)
- der Extraktion relevanter Hashtags
- der Bestimmung der fünf häufigsten Themen in den ausgewerteten Tweets

---

## 🔗 Vorgehensweise

### 1. **Datenerhebung via Twitter API v2**
Die Verbindung zur Twitter API v2 erfolgt über einen persönlichen Bearer Token. Mithilfe gezielter Suchanfragen nach Schlagworten wie "Frankfurt", "#Frankfurt" oder "Frankfurt am Main" werden Tweets gesammelt, die sich thematisch auf die Stadt oder Region beziehen.

Die abgerufenen Daten (max. 100 pro Anfrage) werden lokal im `.csv`-Format gespeichert und dienen als Grundlage für die anschließende Analyse.

---

### 2. **Erste Analyse mit Pandas**
Nach der Datenerhebung werden die Tweets mit der Python-Bibliothek `pandas` untersucht. Im Fokus stehen dabei:

- die Häufigkeit von Nutzeraktivität (ermittelt über die `author_id`)
- das Zählen der meistverwendeten Hashtags mittels regulärer Ausdrücke

Diese Analyseschritte ermöglichen eine erste Einschätzung darüber, wer kommuniziert und welche Begriffe dominieren.

---

### 3. **Thematische Clusterung mit NLP**
Für die Themenextraktion werden folgende NLP-Techniken eingesetzt:

- **Textbereinigung** (Entfernung von Stoppwörtern, URLs, Sonderzeichen)
- **Tokenisierung und Lemmatisierung** mit `spaCy` (deutsches Sprachmodell)
- **TF-IDF-Vektorisierung** zur Gewichtung wichtiger Begriffe
- **Non-negative Matrix Factorization (NMF)** zur Modellierung von Themenclustern

So lassen sich fünf zentrale Themenfelder identifizieren, die jeweils durch die charakteristischen Begriffe ihres Clusters beschrieben werden können.

---

## 📁 Daten und Code

Der Quellcode sowie Beispiel-Datensätze befinden sich in den jeweiligen `.py`-Dateien. Die Verarbeitungsschritte sind modular aufgebaut und dokumentiert.

---

## © Autor

Projektleitung, Konzeption und Umsetzung: *[Sebastian Seipp]*  
Dieses Projekt wurde zu Lern-, Analyse- und Forschungszwecken erstellt.
