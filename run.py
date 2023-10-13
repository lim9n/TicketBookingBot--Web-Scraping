from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.first_try()
    bot.change_currency()
    bot.find_place_to_go(place='New York')
    bot.select_dates(check_in_dates="2023-10-27",
                    check_out_dates='2023-11-10')
    bot.select_adults(10)
    bot.select_rooms(5)
    
    bot.click_search()
    
