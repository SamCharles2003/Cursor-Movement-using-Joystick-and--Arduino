int xaxis = A0;
int yaxis = A1;
int button = 13;

 void setup()
 {
   Serial.begin(115200);
   pinMode(xaxis,INPUT);
   pinMode(yaxis,INPUT);
   pinMode(button, INPUT_PULLUP);
 }
 void loop()
 {
   String str,previous_string;
   int raw_xaxis=analogRead(A0);
   int raw_yaxis=analogRead(A1);
   int real_xaxis=map(raw_xaxis,0,1023,2,1918);
   int real_yaxis=map(raw_yaxis,0,1023,2,1078);
   

  
Serial.print(" ");
Serial.print(real_xaxis);
Serial.print(" ");
Serial.print(real_yaxis);
Serial.print(" ");
Serial.println(digitalRead(button));
delay(20);

 
 
}