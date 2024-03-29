import requests
from lxml import html
from PageObject.Pages.Locators import LocatorAuctionPage as Locator
from PageObject.TestBase.logger_setup import LoggingConfig

logging = LoggingConfig()
logging = logging.get_logging()


class AuctionPage:
    def __init__(self, url: str):
        logging.info("[def] __init__")
        logging.info("url = " + url)
        self.url = url
        logging.info(self.url)

        # Parse main Auction Page
        page = requests.get(self.url)
        self.tree = html.fromstring(page.content)

    def get_lot_href_list(self) -> list:
        auction_href_list = []

        btn_details_list = self.tree.xpath(Locator.BTNS_AUCTION_DETAILS_XPATH)

        for btn_detail in btn_details_list:
            btn_detail = btn_detail.attrib
            href = btn_detail['href']

            if 'leilao' in href:
                try:
                    href = self.get_lot_href(href)
                except:
                    pass

            logging.info(href)
            auction_href_list.append(href)

        return auction_href_list

    def get_next_page_href(self):
        btn_next = self.tree.xpath(Locator.BTN_NEXT_PAGE_XPATH)
        if not btn_next:
            return False

        btn_next = btn_next[0].attrib
        logging.info(btn_next['href'])
        return btn_next['href']

    def get_lot_href(self, href):
        page = requests.get('https://www.lut.com.br' + href)
        tree = html.fromstring(page.content)
        btn_lot = tree.xpath('//*[@id="details0"]/a')[0]
        href = btn_lot.attrib['href']
        return href
