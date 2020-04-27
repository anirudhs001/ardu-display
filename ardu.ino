#include <VGAX.h>

//#include <VGAXUAUtils.h>

VGAX vga;
void setup()
{
    Serial.begin('115200');
    pinMode(13, OUTPUT);

    vga.begin();
    vga.clear()
}
const short BWIDTH = 2;
const short HEIGHT = 8;

byte arr[HEIGHT][BWIDTH] PROGMEM=
{
    {1,1},
    {1,1},
    {1,1},
    {1,1},
    {1,1},
    {1,1},
    {1,1},
    
}
byte posn[2]

void loop()
{
    while (Serial.available())
    {
        Serial.readBytes(arr, 16);
        digitalWrite(13, HIGH);
    }
}