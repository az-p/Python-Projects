import urllib as ul
import urllib.robotparser
import requests
from bs4 import BeautifulSoup, SoupStrainer


class MyCrawler:
    def __init__(self):
        self.start_url = r'http://quotes.toscrape.com/'
        self.crawl_depth = 1
        self.no_robots = []
        self.visit_tree = {}

    def get_child_links(self, url):
        robo_url = ul.parse.urljoin(url, r'/robots.txt')
        print('URL is {}'.format(url))
        print('Robo URL is {}'.format(robo_url))  # Debug

        rp = ul.robotparser.RobotFileParser()
        rp.set_url(robo_url)
        rp.read()
        can_fetch = rp.can_fetch("*", url)
        # print('Can we fetch this URL? ', can_fetch)  # Debug

        if can_fetch:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'lxml', parse_only=SoupStrainer('a'))
            return [link.get('href') for link in soup.find_all('a') if link.get('href')[0] != r'/']
        else:
            self.no_robots.append(url)

    def get_links(self, url, visit_depth):
        link_queue = [url]
        visit_history = []
        for i in range(0, visit_depth):
            next_queue = []
            for link in link_queue:
                if link not in visit_history:
                    print("Visiting {}".format(link))
                    child_links = self.get_child_links(link)
                    next_queue += child_links
                    self.visit_tree[link] = child_links  # Add to graph
                    visit_history.append(link)
                else:
                    print("Already visited {}".format(link))
            link_queue = next_queue.copy()
        return {'visit_history': visit_history + link_queue,
                'disallowed_urls': self.no_robots}

    def prepare_graph(self):
        # Strip path from URLs, then retain only unique
        for k, v in self.visit_tree.items():
            v = [ul.parse.urlparse(url).netloc for url in v]
            v = list(set(v))

    def draw_graph(self):
        import networkx as nx
        from matplotlib import pyplot

        self.prepare_graph()
        print(self.visit_tree)
        G = nx.DiGraph(self.visit_tree)
        gpos = nx.drawing.nx_pydot.graphviz_layout(G, prog='dot')
        g = nx.draw(G, pos=gpos, with_labels=True, font_weight='bold')
        pyplot.show(block=True)

if __name__ == "__main__":
    crawler = MyCrawler()
    print(crawler.get_links(r'http://quotes.toscrape.com/', 2))
    crawler.draw_graph()
