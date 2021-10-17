from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Lanuching the brawser 
    browser = p.chromium.launch()

    # Open a new page with in the brawser
    page = browser.new_page()

    # From language
    From = input('Translate From: ')

    # To language
    To = input('Translate To: ')

    while True:
        # The text that the user want to translate
        content = input('enter word to transelate: ')

        # Go to translate.google.com with a modified url
        page.goto(f'https://translate.google.com/?sl={From}&tl={To}&text={content}&op=translate')

        # Print the translated text from with in the page
        print(page.inner_text('//*[@class="eyKpYb"]/div[1]/span[1]/span/span'))

        # Finding if the user want to continue or exit
        condation = input('Continue or Exit(E)')
        if condation in ['E','e']:
            break

    # Close the browser
    browser.close()