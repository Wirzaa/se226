const int led_0 = 43;
const int led_1 = 44;
const int led_2 = 45;
const int led_3 = 46;
const int powerBtn = 38;
const int modeBtn = 39;

bool isRunning = false;      
byte activePattern = 1;      

int prevPowerBtn = LOW;
int prevModeBtn = LOW;

unsigned long lastTick = 0;
const unsigned long waitTime = 1000; 

byte stepIndex = 0; 
bool toggleFlag = LOW;

void setup() {
  pinMode(led_0, OUTPUT);
  pinMode(led_1, OUTPUT);
  pinMode(led_2, OUTPUT);
  pinMode(led_3, OUTPUT);
  
  pinMode(powerBtn, INPUT);
  pinMode(modeBtn, INPUT);
}

void loop() {
  int currentPowerBtn = digitalRead(powerBtn);
  int currentModeBtn = digitalRead(modeBtn);

  if (currentPowerBtn == HIGH && prevPowerBtn == LOW) {
    isRunning = !isRunning; 
    
    if (!isRunning) {
      clearAllLeds(); 
    } else {
      toggleFlag = LOW;
      stepIndex = 0;
      lastTick = millis() - waitTime; 
    }
    delay(40);
  }
  prevPowerBtn = currentPowerBtn;

  if (currentModeBtn == HIGH && prevModeBtn == LOW) {
    if (isRunning) { 
      activePattern++;
      if (activePattern > 3) {
        activePattern = 1; 
      }
      
      stepIndex = 0;
      clearAllLeds();
      lastTick = millis() - waitTime; 
    }
    delay(40);
  }
  prevModeBtn = currentModeBtn;

  if (isRunning) {
    unsigned long now = millis();

    if (now - lastTick >= waitTime) {
      lastTick = now; 

      switch (activePattern) {
        
        case 1:
          toggleFlag = !toggleFlag; 
          digitalWrite(led_0, toggleFlag);
          digitalWrite(led_1, toggleFlag);
          digitalWrite(led_2, toggleFlag);
          digitalWrite(led_3, toggleFlag);
          break;
          
        case 2:
          clearAllLeds(); 
          
          if (stepIndex == 0) digitalWrite(led_3, HIGH);
          else if (stepIndex == 1) digitalWrite(led_2, HIGH);
          else if (stepIndex == 2) digitalWrite(led_1, HIGH);
          else if (stepIndex == 3) digitalWrite(led_0, HIGH);

          stepIndex++;
          if (stepIndex > 3) stepIndex = 0; 
          break;
          
        case 3:
          clearAllLeds(); 
          
          if (stepIndex == 0) digitalWrite(led_0, HIGH);
          else if (stepIndex == 1) digitalWrite(led_1, HIGH);
          else if (stepIndex == 2) digitalWrite(led_2, HIGH);
          else if (stepIndex == 3) digitalWrite(led_3, HIGH);

          stepIndex++;
          if (stepIndex == 4) stepIndex = 0; 
          break;
      }
    }
  }
}

void clearAllLeds() {
  digitalWrite(led_0, LOW);
  digitalWrite(led_1, LOW);
  digitalWrite(led_2, LOW);
  digitalWrite(led_3, LOW);
}
