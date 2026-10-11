import json

with open("movies_enriched.json", "r", encoding="utf-8") as f:
    movies = json.load(f)

for m in movies:
    if m["id"] == 15:
        m["title"] = "Joker: Folie a Deux"

movies_js = json.dumps(movies, ensure_ascii=False)

with open("app.js", "w", encoding="utf-8") as f:
    f.write(f"const MOVIES = {movies_js};\n")

print("app.js created successfully with", len(movies), "movies")
