from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os

def capture_screenshot(subdomain, output_path=None):
    options = Options()
    options.add_argument('-headless')  # Run Firefox in headless mode
    driver = webdriver.Firefox(options=options)

    try:
        driver.get(subdomain)
        screenshot = driver.get_screenshot_as_png()

        domain_name = subdomain.replace('http://', '').replace('https://', '').replace('.', '_')
        screenshot_filename = f"{domain_name}.png"

        if output_path:
            screenshot_filename = os.path.join(output_path, screenshot_filename)

        with open(screenshot_filename, "wb") as f:
            f.write(screenshot)

        print(f"Screenshot saved for {subdomain} at {screenshot_filename}")
        return screenshot_filename

    except Exception as e:
        print(f"Error capturing screenshot for {subdomain}: {e}")

    finally:
        # Close the browser
        driver.quit()

def capture_screenshots(option, subdomain=None, subdomain_list=None, output_path=None):
    screenshot_filenames = []

    if option == 1:
        screenshot_filename = capture_screenshot(subdomain, output_path)
        if screenshot_filename:
            screenshot_filenames.append(screenshot_filename)

    elif option == 2:
        if subdomain_list:
            for sub in subdomain_list:
                sub = sub.strip()  # Remove leading/trailing spaces if any
                screenshot_filename = capture_screenshot(sub, output_path)
                if screenshot_filename:
                    screenshot_filenames.append(screenshot_filename)
        else:
            print("Empty subdomain list. No screenshots captured.")

    else:
        print("Wrong Input")

    return screenshot_filenames

if __name__ == "__main__":
    print("""
         Press 1 for a single domain
         Press 2 for a list of subdomains
    make sure you have entered the path correctly
    """)
    
    option = int(input("[+] Enter the option: "))
    
    if option == 1:
        subdomain = input("[+] Enter the subdomain: ")
        output_path = input("[+] Enter the path to save the screenshot: ")
        capture_screenshots(option, subdomain=subdomain, output_path=output_path)
    
    elif option == 2:
        subdomain_list_path = input("[+] Enter the file path: ")
        subdomains = open(subdomain_list_path, "r").read().splitlines()
        output_path = input("[+] Enter the path to save the screenshots: ")
        capture_screenshots(option, subdomain_list=subdomains, output_path=output_path)
    
    else:
        print("Wrong Input")

    print("Thank you for using it")
