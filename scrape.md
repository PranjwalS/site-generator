Playwright renders page
       ↓
Semantic chunker
  → { region: "hero", text: "..." }
  → { region: "services", text: "..." }
  → { region: "contact", text: "..." }
       ↓
     Split into two paths
    ↙              ↘
MongoDB/Postgres   Embed each chunk
(raw + structured  (Sentence Transformers)
JSON documents)         ↓
                   Store in ChromaDB
                   with metadata:
                   { url, region, chunk_id }