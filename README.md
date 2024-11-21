# Marathi Stemmer

## Overview  
The Marathi Stemmer is a natural language processing (NLP) tool designed to extract the root or base form (stem) of words in the Marathi language. It helps reduce words to their base form, enabling efficient text analysis tasks like search, information retrieval, and text mining.  

This project is a step towards enhancing language processing capabilities for Marathi, a rich and morphologically complex language.

## Features  
- Efficient Stemming: Reduces inflected or derived words to their base form.  
- Support for Marathi Grammar Rules: Handles common suffixes and word forms in Marathi.  
- Customizable: Easily extendable for additional rules and exceptions.

## Applications  
- **Sentiment Analysis**: Improve accuracy by normalizing words.  
- **Search Engines**: Enhance search by matching stems instead of exact words.  
- **Text Analytics**: Facilitate clustering, classification, and other NLP tasks.

## Methodology  
The Marathi Stemmer employs rule-based algorithms to identify and remove common suffixes in Marathi. The rules are derived from linguistic research and tailored for Marathi grammar.  

### Steps:
1. Tokenize text into individual words.  
2. Apply predefined rules to identify and strip suffixes.  
3. Return the stemmed word.  

## Requirements  
- Python 3.8+  
- Required libraries are listed in `requirements.txt`. Install them using:  
  ```bash
  pip install -r requirements.txt
  ```

## Usage  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/marathi-stemmer.git
   ```
2. Navigate to the project directory:  
   ```bash
   cd marathi-stemmer
   ```
3. Run the stemmer:  
   ```python
   python stemmer.py
   ```

4. Input a Marathi word or sentence to get the stemmed output.  

### Example:
Input:  
```
पुस्तके वाचणारी मुले शाळेत जातात.  
```  
Output:  
```
पुस्तक वाच मुल शाळ जात  
```

## Project Structure  
```
Marathi-Stemmer/  
│  
├── stemmer.py          # Main script for stemming  
├── rules.json          # File containing suffix removal rules  
├── requirements.txt    # Dependencies  
├── data/               # Sample Marathi text files  
└── README.md           # Project documentation  
```

## Contributions  
Contributions are welcome!  
- Fork the repository  
- Create a feature branch  
- Submit a pull request  

## Acknowledgments  
This project was developed as part of a natural language processing initiative to enhance text analysis in regional languages. Special thanks to linguistic researchers and the Marathi-speaking community for their support.  
