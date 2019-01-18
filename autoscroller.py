import pyautogui,time

def main():
	screenWidth, screenHeight = pyautogui.size()
	pyautogui.moveTo(screenWidth/2, screenHeight/2)
	pyautogui.moveTo(200, 500)

	pyautogui.click()
	while True:
		pyautogui.scroll(-50) #scrolls down
		time.sleep(5)       #sleep for 10 seconds
	

main() # Call of the main function