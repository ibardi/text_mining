from imdbpie import Imdb
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

imdb = Imdb()

def search():
    """
    This function allows the user to search for a movie and then either verify or search again using a different phrase. There is no advanced search features beyond what imdb's search offers.
    """
    selectedmovie = input('Please Enter a Title')
    selectedmovie = str(selectedmovie)
    print(imdb.search_for_title(selectedmovie)[0])
    response = input("Does the above match your selection? If not, you will asked to enter the title again. PLEASE MAKE SURE TO ONLY TYPE EITHER 'yes' or 'no'")
    if response == 'yes':
        print("Your selection has been confirmed!")
        global title
        global identi
        title = imdb.search_for_title(selectedmovie)[0].get('title')
        identi = imdb.search_for_title(selectedmovie)[0].get('imdb_id')
    elif response == 'no':
        search()
    else:
        print('Invalid response. You will be asked to re-enter the films name and verify the selection again:')
        search()

def againfun():
    """
    This function just asks the user wether he/she wants to check another movie's review or not.
    """
    again = input("Would you like to check another movie? 'yes' or 'no' only")
    if again == "yes":
        analyze()
    elif again == "no":
        quit()
    else:
        print("Invalid input!")
        againfun()

def analyze():
    """
    This function will analyze the top 5 best reviews for sentiment. The imdb library already lists the reviews according to their filter::"Best". So we do not have to write a function for that. Also, instead of treating these as individual strings, we combine them into one large string. This allows for us to use a single natural language processing to determine the overall sentiment of the reviews.
    """
    search()
    value = 0
    analyizetext = ""
    for element in range(0,5):
        analyizetext = analyizetext + imdb._get_reviews_data(identi)[value]['text']
        value += 1
    score = SentimentIntensityAnalyzer().polarity_scores(analyizetext)
    if score.get("pos") > score.get("neg"):
        print("The top 5 reviews for the movie:",title,". Has been generally positive.")
    elif score.get("pos") < score.get("neg"):
        print("The top 5 reviews for the movie:",title,". Has been generally negative.")
    elif score.get("pos") == score.get("neg"):
        print("The top 5 reviews for the movie:",title,". Has been basically neutral.")
    againfun()

analyze()


    