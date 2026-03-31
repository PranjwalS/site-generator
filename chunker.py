from bs4 import BeautifulSoup

def chunk_html(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "noscript", "nav", "head"]):
        tag.decompose()

    chunks = []

    landmarks = soup.find_all(["header", "main", "footer", "section", "article"])
    
    if not landmarks:
        landmarks = [soup.body]

    for landmark in landmarks:
        region = landmark.name  # "section", "header", etc.

        current_heading = None
        current_text = []

        for el in landmark.descendants:
            if el.name in ["h1", "h2", "h3"]:
                if current_text:
                    text = " ".join(current_text).strip()
                    if len(text.split()) > 15:  # filter short noise
                        chunks.append({
                            "region": region,
                            "heading": current_heading,
                            "text": text
                        })
                current_heading = el.get_text(strip=True)
                current_text = []

            elif el.string and el.string.strip():
                current_text.append(el.string.strip())

        # flush last chunk
        if current_text:
            text = " ".join(current_text).strip()
            if len(text.split()) > 15:
                chunks.append({
                    "region": region,
                    "heading": current_heading,
                    "text": text
                })

    return chunks