# -*- coding: utf-8 -*-
from jinja2.utils import generate_lorem_ipsum

ARTICLES = []

for id, article in enumerate(range(100), start=1):
    title = generate_lorem_ipsum(
        n=1,         # Одно предложение
        html=False,  # В виде обычного текста
        min=2,       # Минимум 2 слова
        max=5        # Максимум 5
    )
    content = generate_lorem_ipsum()
    ARTICLES.append(
        {'id': id, 'title': title, 'content': content}
    )
