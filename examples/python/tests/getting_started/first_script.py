# Setup browser
driver = webdriver.Chrome()

# Step 1: Go to the product page
driver.get("https://www.target.com/p/pok-233-mon-trading-card-game-scarlet-38-violet-8212-destined-rivals-booster-bundle/-/A-94300067")

# Step 2: Click "Add to Cart"
add_to_cart_button = driver.find_element(By.ID, "add-to-cart")
add_to_cart_button.click(2)
time.sleep(2)

# Step 3: Go to cart
driver.get("https://targetcom/cart")

# Step 4: Proceed to checkout
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()
time.sleep(2)

# Step 5: Fill out shipping info
driver.find_element(By.ID, "first_name").send_keys("Ethan")
driver.find_element(By.ID, "last_name").send_keys("mahoney")
driver.find_element(By.ID, "address").send_keys("4612 southwind rd)
driver.find_element(By.ID, "zip").send_keys("30809")

# Step 6: Fill out payment info (test card info in sandbox)
driver.find_element(By.ID, "card_number").send_keys("4535060306034729")
driver.find_element(By.ID, "expiration").send_keys("07/27")
driver.find_element(By.ID, "cvv").send_keys("547")

# Step 7: Place order
place_order_button = driver.find_element(By.ID, "place-order")
place_order_button.click()

# Optional: Close browser
time.sleep(5)
driver.quit()
