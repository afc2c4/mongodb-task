from datetime import datetime
from models.db import posts_collection

posts_collection.delete_many({})

posts_collection.insert_many([
    {
        "title": "Introdução ao MongoDB",
        "content": "Conceitos iniciais sobre MongoDB.",
        "comments": [
            {"user": "ana", "text": "Muito bom!", "likes": 4, "created_at": datetime.now()},
            {"user": "joao", "text": "Gostei bastante", "likes": 2, "created_at": datetime.now()},
            {"user": "ana", "text": "Esperando continuação", "likes": 7, "created_at": datetime.now()}
        ]
    },
    {
        "title": "Aggregation Pipeline na prática",
        "content": "Aprendendo aggregation.",
        "comments": [
            {"user": "carlos", "text": "Conteúdo denso", "likes": 3, "created_at": datetime.now()},
            {"user": "ana", "text": "Excelente!", "likes": 10, "created_at": datetime.now()}
        ]
    }
])

print("Seed executado com sucesso.")
