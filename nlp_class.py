import stanza

class NLP:
    def __init__(self, lang):
        self.nlp = stanza.Pipeline(lang=lang, processors='tokenize, ner, sentiment,pos')

    def analyze(self, text):
        doc = self.nlp(text)
        return doc

    def extract_entities(self, doc):
        entities = []
        for sentence in doc.sentences:
            for entity in sentence.ents:
                entities.append(entity.text)
        return entities

    def extract_entities_v2(self, doc):
   	    print(*[f'token: {token.text}\tner: {token.ner}' for sent in doc.sentences for token in sent.tokens], sep='\n')

    def count_entities(self, entities):
        entity_count = len(entities)
        return entity_count

    def classify_entities(self, doc):
        entity_classification = {}
        for sentence in doc.sentences:
            for entity in sentence.ents:
                if entity.type not in entity_classification:
                    entity_classification[entity.type] = 1
                else:
                    entity_classification[entity.type] += 1
        return entity_classification

    def extract_adjectives(self, doc):
        adjectives = []
        for sentence in doc.sentences:
            for word in sentence.words:
                #print(word,word.upos)
                if word.upos == 'ADJ':
                    adjectives.append(word.text)
        return adjectives

    def count_adjectives(self, adjectives):
        adjective_count = len(adjectives)
        return adjective_count

    def extract_entity_sentiments(self, doc):
        entity_sentiments = {}
        for sentence in doc.sentences:
            for entity in sentence.ents:
                if entity.text not in entity_sentiments:
                    entity_sentiments[entity.text] = sentence.sentiment
        return entity_sentiments

    def extract_place(self, doc):
        
        places = []
        entity_sentiments = {}
        for sentence in doc.sentences:
            for entity in sentence.ents:
                if entity.text not in entity_sentiments:
                    entity_sentiments[entity.text] = sentence.sentiment
        return places

    def extract_date(self, doc):
        date = doc.sentences[0].tokens[0].misc['Date']
        return date

    def extract_sources(self, doc):
        sources = []
        for sentence in doc.sentences:
            for token in sentence.tokens:
                if token.misc is not None and 'Source' in token.misc:
                    sources.append(token.misc['Source'])
        return sources

    def extract_links(self, doc):
        links = []
        for sentence in doc.sentences:
            for token in sentence.tokens:
                if token.misc is not None and 'Link' in token.misc:
                    links.append(token.misc['Link'])
        return links


