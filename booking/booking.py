import booking.constants as const
import os
from selenium import webdriver
from booking.booking_filtration import BookingFiltration
from selenium.webdriver.common.by import By
class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r"F:\WEB SCRAPING\chromedriver.exe", teardown=False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ['PATH']+= self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        
        
    def first_try(self):
        button=self.find_element(By.XPATH,'/html/body/div[17]/div/div/div/div[1]/div[1]/div/button')
        button.click()
    def change_currency(self,):
        currency_element = self.find_element(By.XPATH, '/html/body/div[2]/div/header/nav[1]/div[2]/span[1]/button')
        currency_element.click()

        selected_country_element=self.find_element(By.CSS_SELECTOR, '#b2indexPage > div.b9720ed41e.cdf0a9297c > div > div > div > div > div.f7c2c6294c > div > div.aca0ade214.aaf30230d9.cd2e7d62b0 > div > div > ul:nth-child(1) > li:nth-child(1) > button')
        selected_country_element.click()
    
    
    def find_place_to_go(self,place ):
            
        select_place=self.find_element(By.NAME, 'ss')
        select_place.clear()
        select_place.send_keys(place)
        
        first_result=self.find_element(
            By.CSS_SELECTOR, '#indexsearch > div.hero-banner-searchbox > div > form > div.ffb9c3d6a3.c9a7790c31.e691439f9a > div:nth-child(1) > div > div > div.acf75b5882 > div > ul > li:nth-child(1) > div > div > div > div.a3332d346a'
        )
        
        first_result.click()
        

    
    def select_dates(self,check_in_dates,check_out_dates):
        check_in_elements=self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_in_dates}"]'
        )
        
        
        check_in_elements.click()
        
        check_out_elements=self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_out_dates}"]'
        )
        check_out_elements.click()
        
    def select_adults(self, count=1):
        selection_element = self.find_element(By.CLASS_NAME, 'd777d2b248')
        selection_element.click()

        increase_button_selector = '/html/body/div[3]/div[2]/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[2]'
    
        for _ in range(count-2):
            increase_button_element = self.find_element(By.XPATH, increase_button_selector)
            increase_button_element.click()
            
            
            
    def select_rooms(self, count=1):

        increase_button_selector = '/html/body/div[3]/div[2]/div/form/div[1]/div[3]/div/div/div/div/div[3]/div[2]/button[2]'
    
        for _ in range(count-1):
            increase_button_element = self.find_element(By.XPATH, increase_button_selector)
            increase_button_element.click()    

            
    def click_search(self):
        search_button=self.find_element(
            By.XPATH,f'/html/body/div[3]/div[2]/div/form/div[1]/div[4]/button'
        )
        
        search_button.click()
    
    def apply_filtrartion(self):
        filtration=BookingFiltration(driver=self)