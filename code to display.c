#include <LiquidCrystal.h>
	
// Initialize the Liquid Crystal Displa 
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
	
void setup() {
// Set up the LCD's number of columns and rows
 lcd.begin(16, 2);  
// Print a message to the LCD
 lcd.print("Welcome!");
	  
// Wait for a random time between 3-5 seconds
int time = random(3000, 5001);
delay(time);
      }

void loop() {
// Main code goes here
  }

    
