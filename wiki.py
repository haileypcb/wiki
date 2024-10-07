import wikipediaapi
import time 

user_agent = "wiki (haileycb101@gmail.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

def fetch_links(page):
    links_list = []
    links = page.links 

    for tittle in links.keys():
        links_list.append(tittle)

    return links_list

#creating start and target pages
start_page = wiki.page("Pasadena High School (California)")
target_page = wiki.page("Rose Parade")

print(fetch_links(start_page))