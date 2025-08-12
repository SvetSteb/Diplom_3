from selenium.webdriver.common.by import By

class QueueLocators:

    FIRST_ORDER_IN_QUEUE = (By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"]')

    ORDER_INFO_WINDOW = (By.XPATH, './/div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]')

    TOTAL_OF_ALL_TIME_COUNTER = (By.XPATH, './/div[@class="undefined mb-15"]/p[2]')
    TOTAL_OF_TODAY_COUNTER = (By.XPATH, './/div[@class="OrderFeed_ordersData__1L6Iv"]/div[3]/p[2]')

    IN_PROGRESS_LIST = (By.XPATH, './/ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li[@class="text text_type_digits-default mb-2"]')
    
