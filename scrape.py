import selenium
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time


def setup_webdriver():
    # Initialize the WebDriver session
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    return driver

def close_webdriver(driver):
    driver.quit()



def scrape(person, driver):
    driver.get('https://motor.confused.com/CarDetails')
    wait = WebDriverWait(driver, 10)



    # First Page
    driver.find_element(by=By.ID, value='registration-number-input').send_keys(f'{person.car.reg_number}')
    driver.find_element(by=By.ID, value='find-vehicle-btn').click()
    element = driver.find_element(by=By.ID, value='HasDashcam_2') # No dash cam
    driver.execute_script('arguments[0].click();', element)
    button = driver.find_element(by=By.CSS_SELECTOR, value='.btn--primary.btn--arrow.btn--large.btn-form-submit.btn--submit')
    button.click()




    # Second Page
    # Select dropdown by index:
    dropdown = Select(driver.find_element(By.ID, 'CoverStartDate'))
    dropdown.select_by_index(8) # A week from now

    # Annual Payment frequency
    element = driver.find_element(by=By.ID, value='PaymentFrequency_42719')
    driver.execute_script('arguments[0].click();', element)

    button = driver.find_element(by=By.CSS_SELECTOR, value='.btn--primary.btn--arrow.btn--large.btn-form-submit.btn--submit')
    button.click()



    # Third Page
    # MR buttom
    if person.title == 'Mr':
        element = driver.find_element(by=By.ID, value='Driver_Title_2449') # Need to change for each input option (2449, 2451, 2450, 2452) for (Mr, Mrs, Miss, Ms) respectively
        driver.execute_script('arguments[0].click();', element)
    else:
        element = driver.find_element(by=By.ID, value='Driver_Title_2450') # Need to change for each input option (2449, 2451, 2450, 2452) for (Mr, Mrs, Miss, Ms) respectively
        driver.execute_script('arguments[0].click();', element)

    # First name
    driver.find_element(by=By.ID, value='Driver_FirstName').send_keys(f'{person.first_name}') # Change to form loop

    # Last name
    driver.find_element(by=By.ID, value='Driver_LastName').send_keys(f'{person.last_name}') # Change to form loop

    # Date of birth
    driver.find_element(by=By.ID, value='Driver_DateOfBirth_Day').send_keys(f'{person.dob.day}')
    driver.find_element(by=By.ID, value='Driver_DateOfBirth_Month').send_keys(f'{person.dob.month}')
    driver.find_element(by=By.ID, value='Driver_DateOfBirth_Year').send_keys(f'{person.dob.year}')

    # Marital status
    element = driver.find_element(by=By.ID, value='Driver_MaritalStatus_2455') # Need to change for each input option (2457, 2455) for (Married, Single) respectively
    driver.execute_script('arguments[0].click();', element)

    # Lived in uk since birth?
    element = driver.find_element(by=By.ID, value='Driver_UkResidentSinceBirth_1') # or _2 for no
    driver.execute_script('arguments[0].click();', element)

    # Does the user own or use another car?
    element = driver.find_element(by=By.ID, value='Driver_OwnOrUseAnotherVehicle_2') # _1 or _2 for yes or no respectively
    driver.execute_script('arguments[0].click();', element)

    # Driver occupation
    element = driver.find_element(by=By.ID, value='Driver_Employment_EmploymentStatus_2435_radio')  # 2435 2436 2437 Employed, Self-employed, Retired respectively -- Additional implementation required for other options
    driver.execute_script('arguments[0].click();', element)


    # Dropdown is using Select2 jquery so requires a different method to select
    # Step 1: Click the Select2 box to open it
    select_box = wait.until(EC.element_to_be_clickable((By.ID, "select2-Driver_Employment_OccupationDetails-container")))
    select_box.click()
    # Step 2: Type into the search field that appears (it might have a different ID or selector)
    search_field = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'select2-search__field')))
    search_field.send_keys('Accountant') # change this accordingly

    # Step 3: Wait for results to appear and load
    wait.until(EC.presence_of_element_located((By.ID, 'select2-Driver_Employment_OccupationDetails-results')))

    # Step 4: Select the now-visible desired option (this assumes you want the first result)
    results = driver.find_element(By.ID,'select2-Driver_Employment_OccupationDetails-results')
    results = results.find_elements(By.TAG_NAME, 'li')
    results[0].click()  # replace '0' with the index of the desired result if needed

    # And again for the industry.
    select_box = wait.until(EC.element_to_be_clickable((By.ID, "select2-Driver_Employment_Industry-container")))
    select_box.click()
    # Step 2: Type into the search field that appears (it might have a different ID)
    search_field = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'select2-search__field')))
    search_field.send_keys('Accountancy') # change this accordingly
    # Step 3: Wait for results to appear and load
    wait.until(EC.presence_of_element_located((By.ID, 'select2-Driver_Employment_Industry-results')))
    # Step 4: Select the now-visible desired option (this assumes you want the first result)
    results = driver.find_element(By.ID,'select2-Driver_Employment_Industry-results')
    results = results.find_elements(By.TAG_NAME, 'li')
    results[0].click()  # replace '0' with the index of the desired result if needed

    # Licence Type - Manual for now
    element = driver.find_element(by=By.ID, value='Driver_LicenceType_27777_radio')  
    driver.execute_script('arguments[0].click();', element)



    # Licence held for how long?
    dropdown_element = wait.until(EC.visibility_of_element_located((By.ID, 'Driver_LicenceHeldYears'))) # So always from the age of 18.
    select_dropdown = Select(dropdown_element)
    select_dropdown.select_by_index(1) # change this accordingly

    dropdown_element = wait.until(EC.visibility_of_element_located((By.ID, 'Driver_LicenceHeldAdditionalMonths')))
    select_dropdown = Select(dropdown_element)
    select_dropdown.select_by_index(3)  # Replace '3' with the index of the option you want to select

    # Enter driving licence number?
    element = driver.find_element(by=By.ID, value='Driver_EnterDrivingLicenceNumber_2')  # No
    driver.execute_script('arguments[0].click();', element)

    # Page button
    button = driver.find_element(by=By.CSS_SELECTOR, value='.btn.btn--secondary.btn--medium.item-save-btn')
    button.click()




    # Fourth Page
    time.sleep(1)
    element = driver.find_element(by=By.ID, value='DriverInfo_AddAnotherDriver_2')
    driver.execute_script('arguments[0].click();', element)

    # Phone number
    driver.find_element(by=By.ID, value='Phonenumber').send_keys(f'{person.phone_number}')
    driver.find_element(by=By.ID, value='Email_EmailAddress').send_keys(f'{person.email_address}')
    driver.find_element(by=By.ID, value='postcodeInput').send_keys(f'{person.postcode}')


    element = driver.find_element(by=By.ID, value='HomeOwner_1')  # Yes or _2 for No
    driver.execute_script('arguments[0].click();', element)

    element = driver.find_element(by=By.ID, value='IsCarKeptHomeDuringDay_2')  # No
    driver.execute_script('arguments[0].click();', element)

    # If no then pick an office location
    element = driver.find_element(by=By.ID, value='WhereWillCarBeKeptDuringDay_38588')
    driver.execute_script('arguments[0].click();', element)

    element = driver.find_element(by=By.ID, value='IsCarKeptHomeDuringNight_1')  # Yes
    driver.execute_script('arguments[0].click();', element)

    element = driver.find_element(by=By.ID, value='WhereWillCarBeKeptDuringNight_27787')  # Driveway
    driver.execute_script('arguments[0].click();', element)

    element = driver.find_element(by=By.ID, value='NumberOfCarsKeptAtHome_1')  # 1
    driver.execute_script('arguments[0].click();', element)

    element = driver.find_element(by=By.ID, value='AnyChildrenUnderSixteen_2')  # No
    driver.execute_script('arguments[0].click();', element)

    dropdown_element = wait.until(EC.visibility_of_element_located((By.ID, 'NoClaimsBonus')))
    select_dropdown = Select(dropdown_element)
    select_dropdown.select_by_index(2) # change this accordingly 1 year

    # button = driver.find_element(by=By.CSS_SELECTOR, value='.btn--primary.btn--arrow.btn--large.btn-form-submit.btn--submit')
    # button.click()

    button_find_addy = driver.find_element(By.ID, 'findAddressBtn')

    # Execute a JavaScript click event
    driver.execute_script("arguments[0].click();", button_find_addy)


    dropdown_element = wait.until(EC.visibility_of_element_located((By.ID, 'addressResultsList')))
    select_dropdown = Select(dropdown_element)
    select_dropdown.select_by_index(2) # change this accordingly


    # Page button
    button = driver.find_element(by=By.CSS_SELECTOR, value='.btn--primary.btn--arrow.btn--large.btn-form-submit.btn--submit')
    button.click()




    # Final Page

    element = driver.find_element(by=By.ID, value='CarUsageGeneral_27684') # social and commuting
    driver.execute_script('arguments[0].click();', element)

    time.sleep(0.3)


    # time.wait(10)
    element = driver.find_element(by=By.ID, value='CarUsageGeneral_27684')  #social and commuting
    driver.execute_script('arguments[0].click();', element)


    # Locate the dropdown element
    dropdown_element = wait.until(EC.visibility_of_element_located((By.ID, 'AnnualMileage')))
    select_dropdown = Select(dropdown_element)
    select_dropdown.select_by_index(2) # change this accordingly

    # Accept terms and conditions
    element = driver.find_element(by=By.ID, value='TermsAndConditions_AgreeTermsAndConditions')
    element.click()


    # Back to top to finish form:
    element = driver.find_element(by=By.ID, value='HasTheCarBeenBought_2')
    driver.execute_script('arguments[0].click();', element)

    element = driver.find_element(by=By.ID, value='WillOwnTheCarByThePolicyStartDate_1')
    driver.execute_script('arguments[0].click();', element)

    # dropdown_element = wait.until(EC.visibility_of_element_located((By.ID, 'WhenWasTheCarBought_Month')))
    # select_dropdown = Select(dropdown_element)
    # select_dropdown.select_by_index(1) # change this accordingly


    # # Find the dropdown for the year
    # dropdown_year = driver.find_element(By.ID, 'WhenWasTheCarBought_Year')

    # # Create a Select object for the year
    # select_year = Select(dropdown_year)

    # # Select the first actual year (index 1 because index 0 is the placeholder)
    # select_year.select_by_index(1)

    time.sleep(0.2)

    continue_button = driver.find_element(By.CSS_SELECTOR, '.btn--primary.btn--arrow.btn--large.btn-form-submit.btn--submit')
    continue_button.click()





    # Sign Up page
    # confirm email
    confirm_email = driver.find_element(By.ID, 'confirmemail')
    confirm_email.send_keys(f'{person.email_address}')

    # Create Password:
    password = 'Confusedgotbeat332'
    password_input = driver.find_element(By.ID, 'create-password').send_keys(f'{password}')
    password_confirm = driver.find_element(By.ID, 'confirm-password').send_keys(f'{password}')


    # # Keep me logged in:
    # element = driver.find_element(by=By.ID, value='keeploggedin')
    # element.click()


    # Final Button
    element = driver.find_element(by=By.ID, value='setup-account')
    element.click()



    # View Prices Button
    element = WebDriverWait(driver, 45).until(EC.visibility_of_element_located((By.ID, 'ViewAllPricesButton')))
    element.click()
    html = driver.page_source
    print('Success')
    return html
