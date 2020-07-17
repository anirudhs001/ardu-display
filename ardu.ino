#include <VGAX.h>

VGAX vga;
void setup()
{
    Serial.begin(9600);
    pinMode(13, OUTPUT);

    vga.begin();
    vga.clear(0);
}


//font generated from BITFONZI - by Sandro Maffiodo
#define FNT_NANOFONT_HEIGHT 6
#define FNT_NANOFONT_SYMBOLS_COUNT 95
//data size=570 bytes
const unsigned char fnt_nanofont_data[FNT_NANOFONT_SYMBOLS_COUNT][1+FNT_NANOFONT_HEIGHT] PROGMEM={
{ 1, 128, 128, 128, 0, 128, 0, }, //glyph '!' code=0
{ 3, 160, 160, 0, 0, 0, 0, }, //glyph '"' code=1
{ 5, 80, 248, 80, 248, 80, 0, },  //glyph '#' code=2
{ 5, 120, 160, 112, 40, 240, 0, },  //glyph '$' code=3
{ 5, 136, 16, 32, 64, 136, 0, },  //glyph '%' code=4
{ 5, 96, 144, 104, 144, 104, 0, },  //glyph '&' code=5
{ 2, 128, 64, 0, 0, 0, 0, },  //glyph ''' code=6
{ 2, 64, 128, 128, 128, 64, 0, }, //glyph '(' code=7
{ 2, 128, 64, 64, 64, 128, 0, },  //glyph ')' code=8
{ 3, 0, 160, 64, 160, 0, 0, },  //glyph '*' code=9
{ 3, 0, 64, 224, 64, 0, 0, }, //glyph '+' code=10
{ 2, 0, 0, 0, 0, 128, 64, },  //glyph ',' code=11
{ 3, 0, 0, 224, 0, 0, 0, }, //glyph '-' code=12
{ 1, 0, 0, 0, 0, 128, 0, }, //glyph '.' code=13
{ 5, 8, 16, 32, 64, 128, 0, },  //glyph '/' code=14
{ 4, 96, 144, 144, 144, 96, 0, }, //glyph '0' code=15
{ 3, 64, 192, 64, 64, 224, 0, },  //glyph '1' code=16
{ 4, 224, 16, 96, 128, 240, 0, }, //glyph '2' code=17
{ 4, 224, 16, 96, 16, 224, 0, },  //glyph '3' code=18
{ 4, 144, 144, 240, 16, 16, 0, }, //glyph '4' code=19
{ 4, 240, 128, 224, 16, 224, 0, },  //glyph '5' code=20
{ 4, 96, 128, 224, 144, 96, 0, }, //glyph '6' code=21
{ 4, 240, 16, 32, 64, 64, 0, }, //glyph '7' code=22
{ 4, 96, 144, 96, 144, 96, 0, },  //glyph '8' code=23
{ 4, 96, 144, 112, 16, 96, 0, },  //glyph '9' code=24
{ 1, 0, 128, 0, 128, 0, 0, }, //glyph ':' code=25
{ 2, 0, 128, 0, 0, 128, 64, },  //glyph ';' code=26
{ 3, 32, 64, 128, 64, 32, 0, }, //glyph '<' code=27
{ 3, 0, 224, 0, 224, 0, 0, }, //glyph '=' code=28
{ 3, 128, 64, 32, 64, 128, 0, },  //glyph '>' code=29
{ 4, 224, 16, 96, 0, 64, 0, },  //glyph '?' code=30
{ 4, 96, 144, 176, 128, 112, 0, },  //glyph '@' code=31
{ 4, 96, 144, 240, 144, 144, 0, },  //glyph 'A' code=32
{ 4, 224, 144, 224, 144, 224, 0, }, //glyph 'B' code=33
{ 4, 112, 128, 128, 128, 112, 0, }, //glyph 'C' code=34
{ 4, 224, 144, 144, 144, 224, 0, }, //glyph 'D' code=35
{ 4, 240, 128, 224, 128, 240, 0, }, //glyph 'E' code=36
{ 4, 240, 128, 224, 128, 128, 0, }, //glyph 'F' code=37
{ 4, 112, 128, 176, 144, 112, 0, }, //glyph 'G' code=38
{ 4, 144, 144, 240, 144, 144, 0, }, //glyph 'H' code=39
{ 3, 224, 64, 64, 64, 224, 0, },  //glyph 'I' code=40
{ 4, 240, 16, 16, 144, 96, 0, },  //glyph 'J' code=41
{ 4, 144, 160, 192, 160, 144, 0, }, //glyph 'K' code=42
{ 4, 128, 128, 128, 128, 240, 0, }, //glyph 'L' code=43
{ 5, 136, 216, 168, 136, 136, 0, }, //glyph 'M' code=44
{ 4, 144, 208, 176, 144, 144, 0, }, //glyph 'N' code=45
{ 4, 96, 144, 144, 144, 96, 0, }, //glyph 'O' code=46
{ 4, 224, 144, 224, 128, 128, 0, }, //glyph 'P' code=47
{ 4, 96, 144, 144, 144, 96, 16, },  //glyph 'Q' code=48
{ 4, 224, 144, 224, 160, 144, 0, }, //glyph 'R' code=49
{ 4, 112, 128, 96, 16, 224, 0, }, //glyph 'S' code=50
{ 3, 224, 64, 64, 64, 64, 0, }, //glyph 'T' code=51
{ 4, 144, 144, 144, 144, 96, 0, },  //glyph 'U' code=52
{ 3, 160, 160, 160, 160, 64, 0, },  //glyph 'V' code=53
{ 5, 136, 168, 168, 168, 80, 0, },  //glyph 'W' code=54
{ 4, 144, 144, 96, 144, 144, 0, },  //glyph 'X' code=55
{ 3, 160, 160, 64, 64, 64, 0, },  //glyph 'Y' code=56
{ 4, 240, 16, 96, 128, 240, 0, }, //glyph 'Z' code=57
{ 2, 192, 128, 128, 128, 192, 0, }, //glyph '[' code=58
{ 5, 128, 64, 32, 16, 8, 0, },  //glyph '\' code=59
{ 2, 192, 64, 64, 64, 192, 0, },  //glyph ']' code=60
{ 5, 32, 80, 136, 0, 0, 0, }, //glyph '^' code=61
{ 4, 0, 0, 0, 0, 240, 0, }, //glyph '_' code=62
{ 2, 128, 64, 0, 0, 0, 0, },  //glyph '`' code=63
{ 3, 0, 224, 32, 224, 224, 0, },  //glyph 'a' code=64
{ 3, 128, 224, 160, 160, 224, 0, }, //glyph 'b' code=65
{ 3, 0, 224, 128, 128, 224, 0, }, //glyph 'c' code=66
{ 3, 32, 224, 160, 160, 224, 0, },  //glyph 'd' code=67
{ 3, 0, 224, 224, 128, 224, 0, }, //glyph 'e' code=68
{ 2, 64, 128, 192, 128, 128, 0, },  //glyph 'f' code=69
{ 3, 0, 224, 160, 224, 32, 224, },  //glyph 'g' code=70
{ 3, 128, 224, 160, 160, 160, 0, }, //glyph 'h' code=71
{ 1, 128, 0, 128, 128, 128, 0, }, //glyph 'i' code=72
{ 2, 0, 192, 64, 64, 64, 128, },  //glyph 'j' code=73
{ 3, 128, 160, 192, 160, 160, 0, }, //glyph 'k' code=74
{ 1, 128, 128, 128, 128, 128, 0, }, //glyph 'l' code=75
{ 5, 0, 248, 168, 168, 168, 0, }, //glyph 'm' code=76
{ 3, 0, 224, 160, 160, 160, 0, }, //glyph 'n' code=77
{ 3, 0, 224, 160, 160, 224, 0, }, //glyph 'o' code=78
{ 3, 0, 224, 160, 160, 224, 128, }, //glyph 'p' code=79
{ 3, 0, 224, 160, 160, 224, 32, },  //glyph 'q' code=80
{ 3, 0, 224, 128, 128, 128, 0, }, //glyph 'r' code=81
{ 2, 0, 192, 128, 64, 192, 0, },  //glyph 's' code=82
{ 3, 64, 224, 64, 64, 64, 0, }, //glyph 't' code=83
{ 3, 0, 160, 160, 160, 224, 0, }, //glyph 'u' code=84
{ 3, 0, 160, 160, 160, 64, 0, },  //glyph 'v' code=85
{ 5, 0, 168, 168, 168, 80, 0, },  //glyph 'w' code=86
{ 3, 0, 160, 64, 160, 160, 0, },  //glyph 'x' code=87
{ 3, 0, 160, 160, 224, 32, 224, },  //glyph 'y' code=88
{ 2, 0, 192, 64, 128, 192, 0, },  //glyph 'z' code=89
{ 3, 96, 64, 192, 64, 96, 0, }, //glyph '{' code=90
{ 1, 128, 128, 128, 128, 128, 0, }, //glyph '|' code=91
{ 3, 192, 64, 96, 64, 192, 0, },  //glyph '}' code=92
{ 3, 96, 192, 0, 0, 0, 0, },  //glyph '~' code=93
{ 4, 48, 64, 224, 64, 240, 0, },  //glyph '£' code=94
};
//data size=512 bytes

#define IMG_DINO_WIDTH 20
#define IMG_DINO_BWIDTH 5
#define IMG_DINO_HEIGHT 16
//data size=112 bytes
const unsigned char img_dino_data[IMG_DINO_HEIGHT][IMG_DINO_BWIDTH] PROGMEM={
{   0,   0,  15, 255,   0, },
{   0,   0,  48, 255, 192, },
{   0,   0,  63, 255, 192, },
{   0,   0,  63, 255,   0, },
{   0,   0,  63, 192,   0, },
{   0,   0,  63, 252,   0, },
{  48,   3, 255,   0,   0, },
{  60,  15, 255, 240,   0, },
{  60,  63, 255,  48,   0, },
{  63, 255, 255,   0,   0, },
{  15, 255, 252,   0,   0, },
{   0, 255, 252,   0,   0, },
{   0, 255, 240,   0,   0, },
{   0,  60, 240,   0,   0, },
{   0,  60,  48,   0,   0, },
{   0,  60,  48,   0,   0, },
};

#define IMG_DINO_MASK_WIDTH 20
#define IMG_DINO_MASK_BWIDTH 5
#define IMG_DINO_MASK_HEIGHT 16
//data size=112 bytes
const unsigned char img_dino_mask_data[IMG_DINO_MASK_HEIGHT][IMG_DINO_MASK_BWIDTH] PROGMEM={
{   0,   0,  15, 255,   0, },
{   0,   0,  48, 255, 192, },
{   0,   0,  63, 255, 192, },
{   0,   0,  63, 255,   0, },
{   0,   0,  63, 192,   0, },
{   0,   0,  63, 252,   0, },
{  48,   3, 255,   0,   0, },
{  60,  15, 255, 240,   0, },
{  60,  63, 255,  48,   0, },
{  63, 255, 255,   0,   0, },
{  15, 255, 252,   0,   0, },
{   0, 255, 252,   0,   0, },
{   0, 255, 240,   0,   0, },
{   0,  60, 240,   0,   0, },
{   0,  60,  48,   0,   0, },
{   0,  60,  48,   0,   0, },
};


#define EMPTY_DINO_BLOB_WIDTH 20
#define EMPTY_DINO_BLOB_BWIDTH 5
#define EMPTY_DINO_BLOB_HEIGHT 16
//data size=112 bytes
const unsigned char empty_dino_blob_data[EMPTY_DINO_BLOB_HEIGHT][EMPTY_DINO_BLOB_BWIDTH] PROGMEM={
{   0,  0,  0,  0,  0, },
{   0,  0,  0,  0,  0, },
{   0,  0,  0,  0,  0, },
{   0,  0,  0,  0,  0, },
{   0,  0,  0,  0,  0, },
{   0,  0,  0,  0,  0, },
{   0,  0,  0,  0,  0, },
{   0,  0,  0,  0,  0, },
{   0,  0,  0,  0,  0, },
{   0,  0,  0,  0,  0, },
{   0,  0,  0,  0,  0, },
{   0,  0,  0,  0,  0, },
{   0,  0,  0,  0,  0, },
{   0,  0,  0,  0,  0, },
{   0,  0,  0,  0,  0, },
{   0,  0,  0,  0,  0, },
};

// #define IMG_TREE_BLOB_WIDTH 10
// #define IMG_TREE_BLOB_BWIDTH 3
// #define IMG_TREE_BLOB_HEIGHT 14
// //data size=48 bytes
// const unsigned char empty_tree_blob_data[IMG_TREE_BLOB_HEIGHT][IMG_TREE_BLOB_BWIDTH] PROGMEM={
// {   0,   0,   0, },
// {   0,   0,   0, },
// {   0,   0,   0, },
// {   0,   0,   0, },
// {   0,   0,   0, },
// {   0,   0,   0, },
// {   0,   0,   0, },
// {   0,   0,   0, },
// {   0,   0,   0, },
// {   0,   0,   0, },
// {   0,   0,   0, },
// {   0,   0,   0, },
// {   0,   0,   0, },
// {   0,   0,   0, },
// };

// #define IMG_TREE_WIDTH 10
// #define IMG_TREE_BWIDTH 3
// #define IMG_TREE_HEIGHT 14
// //data size=48 bytes
// const unsigned char img_tree_data[IMG_TREE_HEIGHT][IMG_TREE_BWIDTH] PROGMEM={
// {   0, 192,   0, },
// {   0, 192,   0, },
// {   0, 192,   0, },
// {   0, 195,   0, },
// {   0, 195,   0, },
// {   0, 195,   0, },
// {   0, 195,   0, },
// {  12, 195,   0, },
// {  15, 252,   0, },
// {   0, 240,   0, },
// {   0, 192,   0, },
// {   0, 192,   0, },
// {   0, 192,   0, },
// {   0, 192,   0, },
// };

// #define IMG_TREE_MASK_WIDTH 10
// #define IMG_TREE_MASK_BWIDTH 3
// #define IMG_TREE_MASK_HEIGHT 14
// //data size=48 bytes
// const unsigned char img_tree_mask_data[IMG_TREE_MASK_HEIGHT][IMG_TREE_MASK_BWIDTH] PROGMEM={
// {   0, 192,   0, },
// {   0, 192,   0, },
// {   0, 192,   0, },
// {   0, 195,   0, },
// {   0, 195,   0, },
// {   0, 195,   0, },
// {   0, 195,   0, },
// {  12, 195,   0, },
// {  15, 252,   0, },
// {   0, 240,   0, },
// {   0, 192,   0, },
// {   0, 192,   0, },
// {   0, 192,   0, },
// {   0, 192,   0, },
// };


#define DINO_ID 'D'
#define TREE_ID 'T'
#define MSG_ID 'M'
#define SPRITE_COUNT 1

char str[10] = "GAME OVER";
const char obstacle[] PROGMEM = "o";
static byte stance[SPRITE_COUNT];
static int posn[SPRITE_COUNT][2];
static bool GAME_OVER = false;
void loop()
{
    //some buffers to read serial:
    static int temp_x, temp_y;
    static char c;
    while (Serial.available())
    {   
        for (byte j = 0; j < SPRITE_COUNT; )//read 3 sprites
        {
            temp_x = posn[j][0];
            temp_y = posn[j][1];
            posn[j][0] = 0;
            posn[j][1] = 1;
            if (Serial.available() > 0)
            {
                c = Serial.read();
                if (c == MSG_ID)
                {
                    read_msg();
                    GAME_OVER = true;
                }
                else if (c == DINO_ID || ( c - '0' >= 0 && c < SPRITE_COUNT)) // for tree, id is in set [0, SPRITE_COUNT-1] 
                {
                    read_sprite(j);
                    j++;
                }
            }
            if (GAME_OVER)
                vga.printSRAM((byte*)fnt_nanofont_data, FNT_NANOFONT_SYMBOLS_COUNT, FNT_NANOFONT_HEIGHT , 3, 1, str, VGAX_WIDTH/2, VGAX_HEIGHT/2, 1);
            
            if (c == DINO_ID)
            {
                if (posn[j - 1][0] != temp_x || posn[j - 1][1] != temp_y)
                    vga.blitwmask((byte*)empty_dino_blob_data, (byte*)img_dino_mask_data, EMPTY_DINO_BLOB_WIDTH, EMPTY_DINO_BLOB_HEIGHT, temp_x, VGAX_HEIGHT - IMG_DINO_HEIGHT - temp_y);
                vga.blitwmask((byte*)img_dino_data, (byte*)img_dino_mask_data, IMG_DINO_WIDTH, IMG_DINO_HEIGHT, posn[j - 1][0], VGAX_HEIGHT - IMG_DINO_HEIGHT - posn[j - 1][1]);
            }
            else //TODO: use sprites instead
            {
                if (posn[j - 1][0] != temp_x || posn[j - 1][1] != temp_y)
                    vga.printPROGMEM((byte*)fnt_nanofont_data, FNT_NANOFONT_SYMBOLS_COUNT, FNT_NANOFONT_HEIGHT, 3, 1, obstacle, temp_x, VGAX_HEIGHT - temp_y, 0);
                vga.printPROGMEM((byte*)fnt_nanofont_data, FNT_NANOFONT_SYMBOLS_COUNT, FNT_NANOFONT_HEIGHT, 3, 1, obstacle, posn[j - 1][0], VGAX_HEIGHT - posn[j - 1][1], 2);
            }
        }
    }
    vga.delay(50);
}

void read_sprite(byte j)
{
    char c;
    for (byte i = 0; i < 4;) // TODO: change 4 to a constant
    {   
        vga.delay(3); //some time to update the buffer
        if (Serial.available() > 0)
        {
            c = Serial.read();

            if (c == '_')
            {
                i++;
                continue;
            }
            else if (c == '|')
            {
                i = 5;
                break;
            }
            switch(i)
            {
                case 1:
                    stance[j] = c - '0';
                    break;
                case 2:
                case 3:
                    posn[j][i - 2] *= 10;
                    posn[j][i - 2] += c - '0';
                    break;
                default:
                    break;
            }
        }
    }    
}

void read_msg() // TODO: merge read_msg and read_sprite
{
    char c;
    char *p =str;
    while (c != '|')
    {
        delay(3); //some time to... yeah i said it already
        if (Serial.available() > 0)
        {
            c = Serial.read();
            if (*p != '\n' && c != '_' && c != '|') 
            {
                *p = c;
                p++;
            }
        }
    }
}