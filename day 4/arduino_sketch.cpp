void setup()
{

  Serial.begin(9600);  // initialize serial communications at 9600 bps
  pinMode(13, OUTPUT);
}

void loop()
{
  // serial read section
  while (Serial.available()) // this will be skipped if no data present, leading to
                             // the code sitting in the delay function below
  {
    delay(30);  //delay to allow buffer to fill
    if (Serial.available() >0)
    {
      char c = Serial.read();  //gets one byte from serial buffer
      if (c == '1')
      {
          digitalWrite(13, HIGH);
      }
      else {
          digitalWrite(13, LOW);
      }
    }
  }
}