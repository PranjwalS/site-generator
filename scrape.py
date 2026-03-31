import json

from playwright.async_api import async_playwright
import asyncio
from chunker import chunk_html

async def scrape(url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url, wait_until="networkidle") 
        html = await page.content() 
        await browser.close()
        return html 

async def main():
    html_content = await scrape("https://whiterabbitwaterloo.com/bar-bible/")
    chunks = chunk_html(html_content)
    
    with open("chunks.json", "w") as f:
        json.dump(chunks, f, indent=2)
        
asyncio.run(main())