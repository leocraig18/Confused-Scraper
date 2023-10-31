import selenium
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

def wait_for_element(driver, by, value, time_to_wait=10):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))


def click_element(driver, by, value):
    element = wait_for_element(driver, by, value)
    element.click()


def click_element_js(driver, by, value):
    element = driver.find_element(by, value)
    driver.execute_script('arguments[0].click();', element)

def send_keys_to_element(driver, by, value, keys):
    element = wait_for_element(driver, by, value)
    element.send_keys(keys)


def select_from_dropdown_by_index(driver, element_id, index):
    dropdown = Select(wait_for_element(driver, By.ID, element_id))
    dropdown.select_by_index(index)

def setup_webdriver():

    # Initialize the WebDriver session
    # Make sure to pass the options
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    return driver

def close_webdriver(driver):
    driver.quit()


def scrape(person, driver):
    driver.get('https://motor.confused.com/CarDetails')
    wait = WebDriverWait(driver, 10)
    time.sleep(0.3)
    
    # First Page
    send_keys_to_element(driver, By.ID, 'registration-number-input', f'{person.car.reg_number}')
    click_element(driver, By.ID, 'find-vehicle-btn')
    click_element_js(driver, By.ID, 'HasDashcam_2')
    click_element(driver, By.CSS_SELECTOR,
                  '.btn--primary.btn--arrow.btn--large.btn-form-submit.btn--submit')

    # Second Page
    select_from_dropdown_by_index(driver, 'CoverStartDate', 8)
    click_element_js(driver, By.ID, 'PaymentFrequency_42719')
    click_element(driver, By.CSS_SELECTOR,
                  '.btn--primary.btn--arrow.btn--large.btn-form-submit.btn--submit')

    # Third Page
    if person.title == 'Mr':
        click_element_js(driver, By.ID, 'Driver_Title_2449')
    else:
        click_element_js(driver, By.ID, 'Driver_Title_2450')
    
    send_keys_to_element(driver, By.ID, 'Driver_FirstName',
                         f'{person.first_name}')
    send_keys_to_element(driver, By.ID, 'Driver_LastName', f'{person.last_name}')
    send_keys_to_element(driver, By.ID, 'Driver_DateOfBirth_Day', f'{person.dob.day}')
    send_keys_to_element(driver, By.ID, 'Driver_DateOfBirth_Month', f'{person.dob.month}')
    send_keys_to_element(driver, By.ID, 'Driver_DateOfBirth_Year', f'{person.dob.year}')
    click_element_js(driver, By.ID, 'Driver_MaritalStatus_2455') # Single
    click_element_js(
        driver, By.ID, 'Driver_UkResidentSinceBirth_1')  # Uk resident from birth
    click_element_js(
        driver, By.ID, 'Driver_OwnOrUseAnotherVehicle_2')  # Does not own another vehicle
    click_element_js(
        driver, By.ID, 'Driver_Employment_EmploymentStatus_2435_radio')  # 2435 2436 2437 Employed, Self-employed, Retired respectively

    click_element(
        driver, By.ID, 'select2-Driver_Employment_OccupationDetails-container')
    send_keys_to_element(driver, By.CLASS_NAME,
                         'select2-search__field', 'Accountant')
    
    # Step 3: Wait for results to appear and load
    wait_for_element(driver, By.ID,
                     'select2-Driver_Employment_OccupationDetails-results')
    # Step 4: Select the now-visible desired option (this assumes you want the first result)
    results = driver.find_element(
        By.ID, 'select2-Driver_Employment_OccupationDetails-results')
    results = results.find_elements(By.TAG_NAME, 'li')
    # replace '0' with the index of the desired result if needed
    results[0].click()

    click_element(
        driver, By.ID, 'select2-Driver_Employment_Industry-container')
    send_keys_to_element(driver, By.CLASS_NAME,
                         'select2-search__field', 'Accountancy')

    # Step 4: Select the now-visible desired option (this assumes you want the first result)
    results = driver.find_element(
        By.ID, 'select2-Driver_Employment_Industry-results')
    results = results.find_elements(By.TAG_NAME, 'li')
    # replace '0' with the index of the desired result if needed
    results[0].click()

    # Licence Type - Manual for now
    click_element_js(driver, By.ID, 'Driver_LicenceType_27777_radio')

    select_from_dropdown_by_index(driver, 'Driver_LicenceHeldYears', 1)
    select_from_dropdown_by_index(driver, 'Driver_LicenceHeldAdditionalMonths', 3)

    click_element_js(driver, By.ID, 'Driver_EnterDrivingLicenceNumber_2')
    click_element(driver, By.CSS_SELECTOR,
                  '.btn.btn--secondary.btn--medium.item-save-btn')


    # Fourth Page
    time.sleep(1)
    click_element_js(driver, By.ID, 'DriverInfo_AddAnotherDriver_2')
    send_keys_to_element(driver, By.ID, 'Phonenumber', f'{person.phone_number}')
    send_keys_to_element(driver, By.ID, 'Email_EmailAddress', f'{person.email_address}')
    send_keys_to_element(driver, By.ID, 'postcodeInput', f'{person.postcode}')

    click_element_js(driver, By.ID, 'HomeOwner_1')
    click_element_js(driver, By.ID, 'IsCarKeptHomeDuringDay_2')
    click_element_js(driver, By.ID, 'WhereWillCarBeKeptDuringDay_38588')
    click_element_js(driver, By.ID, 'IsCarKeptHomeDuringNight_1')
    click_element_js(driver, By.ID, 'WhereWillCarBeKeptDuringNight_27787')
    click_element_js(driver, By.ID, 'NumberOfCarsKeptAtHome_1')
    click_element_js(driver, By.ID, 'AnyChildrenUnderSixteen_2')
    select_from_dropdown_by_index(driver, 'NoClaimsBonus', 2)

    click_element(driver, By.CSS_SELECTOR,
                  '.btn--primary.btn--arrow.btn--large.btn-form-submit.btn--submit')
    click_element_js(driver, By.ID, 'findAddressBtn')
    select_from_dropdown_by_index(driver, 'addressResultsList', 2)
    click_element(driver, By.CSS_SELECTOR,
                  '.btn--primary.btn--arrow.btn--large.btn-form-submit.btn--submit')
    

    # Final Form Page
    time.sleep(1)
    click_element_js(driver, By.ID, 'HasTheCarBeenBought_2')
    click_element_js(driver, By.ID, 'WillOwnTheCarByThePolicyStartDate_1')
    click_element_js(driver, By.ID, 'CarUsageGeneral_27684') # Social and commuting
    select_from_dropdown_by_index(driver, 'AnnualMileage', 2)
    click_element(driver, By.ID, 'TermsAndConditions_AgreeTermsAndConditions')
    click_element(driver, By.CSS_SELECTOR,
                  '.btn--primary.btn--arrow.btn--large.btn-form-submit.btn--submit')


    # Create Account
    send_keys_to_element(driver, By.ID, 'confirmemail',
                         f'{person.email_address}')
    password = 'ConfusedGotScraper360'
    send_keys_to_element(driver, By.ID, 'create-password', f'{password}')
    send_keys_to_element(driver, By.ID, 'confirm-password', f'{password}')

    click_element(driver, By.ID, 'setup-account')

    wait_for_element(driver, By.ID, 'ViewAllPricesButton', 45).click()
    html = driver.page_source
    return html
