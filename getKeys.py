from google.cloud import language_v1
from google.cloud.language_v1 import enums
<<<<<<< HEAD
<<<<<<< HEAD
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('/home/lucerax/mysite/project.json')
=======
>>>>>>> 2f970d59632bf745bdc09045c6a9a60f1c472544
=======
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('.\project.json')
>>>>>>> 2cb4eb6d5138d3eb52aa04887a76af236f7fb505



def sample_analyze_entities(text_content):
    """
    Analyzing Entities in a String

    Args:
      text_content The text content to analyze
    """

<<<<<<< HEAD
<<<<<<< HEAD
    client = language_v1.LanguageServiceClient(credentials = credentials)
=======
    client = language_v1.LanguageServiceClient()
>>>>>>> 2f970d59632bf745bdc09045c6a9a60f1c472544
=======
    client = language_v1.LanguageServiceClient(credentials = credentials)
>>>>>>> 2cb4eb6d5138d3eb52aa04887a76af236f7fb505

    # text_content = 'California is a state.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_entities(document, encoding_type=encoding_type)

    Rep = []
    Entity = []
    Salience= []
    MentionText= []
    MentionType = []

    # Loop through entitites returned from the API
    for entity in response.entities:
        #print(u"Representative name for the entity: {}".format(entity.name))
        Rep.append(entity.name)
        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        #print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))
        Entity.append(enums.Entity.Type(entity.type).name)
        # Get the salience score associated with the entity in the [0, 1.0] range
        #print(u"Salience score: {}".format(entity.salience))
        Salience.append(entity.salience)
        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
        #for metadata_name, metadata_value in entity.metadata.items():
            #   print(u"{}: {}".format(metadata_name, metadata_value))

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
        for mention in entity.mentions:
            #print(u"Mention text: {}".format(mention.text.content))
            MentionText.append(mention.text.content)
            # Get the mention type, e.g. PROPER for proper noun
            #print(u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name))
            MentionType.append(enums.EntityMention.Type(mention.type).name)

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.

    #print(u"Language of the text: {}".format(response.language))
    return(Rep[:5])

def keyResult(article):
    list = sample_analyze_entities(article)
    print("list: ", list)
    return list
