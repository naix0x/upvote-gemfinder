from vote_management.selenium_config import configure_selenium
from vote_management.recaptcha_solver import solve_recaptcha
from vote_management.web_driver_setup import setup_webdriver
from vote_management.vote_process import perform_vote
from target import get_target_url

def main():
    try:
        test_driver = setup_webdriver()
        configure_selenium(test_driver)

        target_url = get_target_url()
        test_driver.get(target_url)

        recaptcha_iframe = solve_recaptcha(test_driver)
        
        print("Success: reCAPTCHA solved")

        perform_vote(test_driver)
        print("Success: Vote button clicked")

    except Exception as e:
        print(f"Failed: {str(e)}")

    finally:
        if 'test_driver' in locals():
            test_driver.quit()

if __name__ == "__main__":
    main()
