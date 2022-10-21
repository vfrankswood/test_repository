from database import articles

def get_genres():
    genres = [g for g in articles.keys()]

    return genres

def get_article(genre):
    article = articles[genre]

    return article