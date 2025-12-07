def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose browser language')

@pytest.fixture
def browser(request):
    user_language = request.config.getoption('--language')
    options = Options()
    options.add_experimental_option("prefs", {'intl.accept_languages' : user_language})
    driver = webdriver.Chrome(options=options)
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    driver.get(link)

    yield driver
    driver.quit()
