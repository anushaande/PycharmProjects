from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.text)
story_links = soup.select(selector=".titleline a")
# for link in story_links:
#     print(link.text)
#     print(link.get("href"))
upvotes = soup.select(selector="span .score")
# for vote in upvotes:
#     print(int(vote.text.split()[0]))
text_list = [link.text for link in soup.select(selector=".titleline a")]
# print(text_list)
href_list = [link.get("href") for link in soup.select(selector=".titleline a")]
# print(href_list)
votes = [int(vote.text.split()[0]) for vote in soup.select(selector="span .score")]
# print(votes)
print(f"{text_list[votes.index(max(votes))]},{href_list[votes.index(max(votes))]}")
