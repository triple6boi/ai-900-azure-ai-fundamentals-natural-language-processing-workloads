from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os

class colors:
    green = '\033[92m'
    blue = '\033[94m'
    red = '\033[31m'
    yellow = '\033[33m'
    reset = '\033[0m'


cog_endpoint = "https://ai-letsgo.cognitiveservices.azure.com/"
cog_key = "1900553b76394f80af2a5ed7d1c200e0"
text_analytics_client = TextAnalyticsClient(endpoint=cog_endpoint, credential=AzureKeyCredential(cog_key))


# Change the lines below in quotes to try your own reviews! 
review1 =["This place is awesome. I highly recommend."]
review2 = ["This place sucks.  Not coming back. "]




def text_analytics(review):
    sentiment_analysis = text_analytics_client.analyze_sentiment(documents=review)
    print("\n-----Sentiment Analysis-----")
    print(f"{colors.blue}The sentence to analyze: {colors.reset}" + str(review))
    for result in sentiment_analysis:
        print(f"{colors.green}Sentiment: {colors.reset}" + result.sentiment)
        print(f"{colors.green}Confidence: {colors.reset}" + str(result.confidence_scores))
    print("----------\n")

    input("Press Enter to continue to key phrases...\n")

    print("\n-----Key Phrases-----")
    print(f"{colors.blue}The sentence to analyze:  {colors.reset}" + str(review))
    key_phrase_analysis = text_analytics_client.extract_key_phrases(documents=review)
    for result in key_phrase_analysis:
        print(f"{colors.green}Key Phrases: {colors.reset}" + str(result.key_phrases))
    print("----------\n")

    input("Press Enter to continue to entities...\n")

    print("\n-----Entities-----")
    print(f"{colors.blue}The sentence to analyze:  {colors.reset}" + str(review))
    entity_analysis = text_analytics_client.recognize_entities(documents=review)
    for result in entity_analysis:
        for entity in result.entities:
            print(f"{colors.green}Entity:{colors.reset} {entity.text:<30}", 
            f" {colors.yellow}Category:{colors.reset} {entity.category:<15}", 
            f" {colors.red}Confidence:{colors.reset} {entity.confidence_score:<4}")
    print("----------\n")

    input("Press Enter to continue...\n")
    print('\033c')


text_analytics(review1)

text_analytics(review2)

input("Press Enter to exit...\n")
