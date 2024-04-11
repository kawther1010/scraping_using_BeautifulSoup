import requests
from bs4 import BeautifulSoup
import csv


import random

def get_article_infos(article):
    type_article = article.contents[3].find('h3').text.strip()
    topic_article = article.contents[9].find('h1').text.strip()
    arther_article = article.contents[9].find('a').text.strip()
    description_article = article.contents[3].find('h2').text.strip()
    date_article = article.contents[9].find('span').text.strip()
    # Déterminez si l'article est faux ou réel en fonction du type d'article
    fake_keywords = ["كذب", "تضليل", "غير مؤكد", "نظرية المؤامرة", "كذب باسم العلم", "خطأ", "انحياز", "تلاعب بالحقائق", "عبث", "سخرية", "خارج السياق", "عنوان مضلل", "ارباك"]
    classification = "fake" if any(keyword in type_article for keyword in fake_keywords) else "real"
    return [
        topic_article,
        type_article,
        arther_article,
        description_article,
        date_article,
        classification
    ]

def main():
    articles_info = []
    for _ in range(30):  # Générer une séquence de 30 numéros aléatoires
        number = random.randint(863, 893)
        page = requests.get(f"https://verify-sy.com/details/{number}")
        if page.status_code == 200:
            src = page.content
            soup = BeautifulSoup(src, 'lxml')
            articles = soup.find_all("div", {'class': 'blog_post_style2 blog_single_div'})
            if articles:
                article_info = get_article_infos(articles[0])
                articles_info.append(article_info)
        else:
            print(f"Erreur lors de la récupération de la page pour le numéro {number}")

    # Trier les articles par sujet (topic)
    sorted_articles_info = sorted(articles_info, key=lambda x: x[0])  # Trie par le premier élément de chaque liste (sujet)

    # Écrire les données triées dans un fichier CSV
    with open('articles_info_sorted.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Topic d\'article',' classification', 'Type d\'article', 'Arther d\'article', 'Description d\'article', 'Date de l\'article', 'Fake or Real'])
        writer.writerows(sorted_articles_info)
    print("Le fichier CSV a été créé avec succès : articles_info_sorted.csv")

if __name__ == "__main__":
    main()
