from selenium import webdriver
from selenium.webdriver.firefox.options import Options

print("""
*****Press 1 for a single domain*****
*****Press 2 for list of subdomains*****
make sure you have entered a the path correctly
""")
def capture_screenshots(option, subdomain=None, subdomain_list=None, output_path=None):
    screenshot_filenames = []
    
    if option == 1:
        options = Options()
        options.add_argument('-headless')  # Run Firefox in headless mode
        driver = webdriver.Firefox(options=options)

        try:
            driver.get(subdomain)
            
            screenshot = driver.get_screenshot_as_png()
            domain_name = subdomain.replace('http://', '').replace('https://', '').replace('.', '_')
            screenshot_filename = f"{domain_name}.png"
            
            if output_path:
                screenshot_filename = f"{output_path}/{screenshot_filename}"
            
            with open(screenshot_filename, "wb") as f:
                f.write(screenshot)
            
            screenshot_filenames.append(screenshot_filename)
            print(f"Screenshot saved for {subdomain} at {screenshot_filename}")
        except Exception as e:
            print(f"Error capturing screenshot for {subdomain}: {e}")
        
        # Close the browser
        driver.quit()

    elif option == 2:
        options = Options()
        options.add_argument('-headless')  # Run Firefox in headless mode
        driver = webdriver.Firefox(options=options)

        for sub in subdomain_list:
            sub = sub.strip()  # Remove leading/trailing spaces if any
            
            try:
                driver.get(sub)
                
                screenshot = driver.get_screenshot_as_png()
                domain_name = sub.replace('http://', '').replace('https://', '').replace('.', '_')
                screenshot_filename = f"{domain_name}.png"
                
                if output_path:
                    screenshot_filename = f"{output_path}/{screenshot_filename}"
                
                with open(screenshot_filename, "wb") as f:
                    f.write(screenshot)
                
                screenshot_filenames.append(screenshot_filename)
                print(f"Screenshot saved for {sub} at {screenshot_filename}")
            except Exception as e:
                print(f"Error capturing screenshot for {sub}: {e}")
            
        # Close the browser
        driver.quit()

    else:
        print("Wrong Input")

    return screenshot_filenames

# Example usage:
option = int(input("[+] Enter the option: "))
if option == 1:
    subdomain = input("[+] Enter the subdomain: ")
    output_path = input("[+] Enter the path to save the screenshots: ")
    capture_screenshots(option, subdomain=subdomain, output_path=output_path)
elif option == 2:
    subdomain_list_path = input("[+] Enter the file path: ")
    subdomains = open(subdomain_list_path, "r").read().splitlines()
    output_path = input("[+] Enter the path to save the screenshots: ")
    capture_screenshots(option, subdomain_list=subdomains, output_path=output_path)
else:
    print("Wrong Input")

print("Thank you for using it")
