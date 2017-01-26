#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define  MOUSE_EXT  ".m79"

enum  TAGTYPE {MACRO, PARAM, LOOP};

typedef struct {
   enum TAGTYPE TAG;
   int  POS;
   int  OFF;
   } FRAMETYPE;

char  PROG[5001];
int   DEFINITIONS[27];
int   CALSTACK[21];
FRAMETYPE  STACK[21];
int   DATA[261];
int   CAL, CHPOS, LEVEL, OFFSET, PARNUM, PARBAL, TEMP;
char  CH;
char  filename[133];
FILE  *fp;
char instr[26];


void chomp (char *str);
int  NUM (char CH);
int  VAL (char CH);
void GETCHAR (void);
void PUSHCAL (int DATUM);
int  POPCAL (void);
void PUSH (enum TAGTYPE TAGVAL);
void POP (void);
void SKIP (char LCH, char RCH);
void LOAD (void);


int main (int argc, char *argv[])
{
   if (argc == 1)
      {
      printf("Syntax: MOUSE  filename\n");
      exit(0);
      }

   strcpy(filename, argv[1]);
   if (strchr(filename, (int)'.') == NULL)
      strcat(filename, MOUSE_EXT);

   if ((fp=fopen(filename,"rb"))==NULL)
      {
      printf("Error opening file %s\n", filename);
      exit(1);
      }

   LOAD();
   fclose(fp);

   CHPOS = 0; LEVEL = 0; OFFSET = 0; CAL = 0;
   do {
      GETCHAR();
      switch (CH)
         {
         case ' ':  case ']':  case '$' :
            break;

         case '0':  case '1':  case '2':  case '3':  case '4':
         case '5':  case '6':  case '7':  case '8':  case '9':
                TEMP = 0;
                while ((CH>='0') && (CH<='9'))
                   {
                   TEMP = 10 * TEMP + VAL(CH); GETCHAR();
                   }
                PUSHCAL(TEMP); CHPOS = CHPOS - 1;
                break;

         case 'A':  case 'B':  case 'C':  case 'D':  case 'E':
         case 'F':  case 'G':  case 'H':  case 'I':  case 'J':
         case 'K':  case 'L':  case 'M':  case 'N':  case 'O':
         case 'P':  case 'Q':  case 'R':  case 'S':  case 'T':
         case 'U':  case 'V':  case 'W':  case 'X':  case 'Y':
         case 'Z':
                PUSHCAL(NUM(CH) + OFFSET);
                break;

         case '?'  :
                fgets(instr, 25, stdin);
                chomp(instr);
                sscanf(instr, "%d", &TEMP);
                PUSHCAL(TEMP);
                break;

         case '!'  : printf("%1d", POPCAL());  break;

         case '+'  : PUSHCAL(POPCAL() + POPCAL());  break;

         case '-'  :
                TEMP = POPCAL();
                PUSHCAL(POPCAL() - TEMP);
                break;

         case '*'  : PUSHCAL(POPCAL() * POPCAL());  break;

         case '/'  :
                TEMP = POPCAL();
                PUSHCAL(POPCAL() / TEMP);
                break;

         case '.'  : PUSHCAL(DATA[POPCAL()]);  break;

         case '='  :
                TEMP = POPCAL();
                DATA[POPCAL()] = TEMP;
                break;

         case '"'  :
                do {
                   GETCHAR();
                   if (CH == '!')
                      printf("\n");
                   else if (CH != '"')
                      printf("%c", CH);
                   } while (CH != '"');
                break;

         case '['  : if (POPCAL() <= 0) SKIP('[',']'); break;

         case '('  : PUSH(LOOP);  break;

         case '^'  :
                if (POPCAL() <= 0)
                   {
                   POP(); SKIP('(',')');
                   }
                break;

         case ')'  : CHPOS = STACK[LEVEL].POS;  break;

         case '#'  :
                   GETCHAR();
                   if (DEFINITIONS[NUM(CH)] > 0)
                      {
                      PUSH(MACRO);
                      CHPOS = DEFINITIONS[NUM(CH)];
                      OFFSET = OFFSET + 26;
                      }
                   else SKIP('#',';');
                break;

         case '@'  :
                POP(); SKIP('#',';');
                break;

         case '%'  :
                   GETCHAR(); PARNUM = NUM(CH); PUSH(PARAM);
                   PARBAL = 1; TEMP = LEVEL;
                   do {
                      TEMP = TEMP - 1;
                      switch (STACK[TEMP].TAG)
                         {
                         case MACRO : PARBAL = PARBAL - 1; break;
                         case PARAM : PARBAL = PARBAL + 1; break;
                         case LOOP : break;
                         }
                      } while (PARBAL != 0);
                   CHPOS = STACK[TEMP].POS;
                   OFFSET = STACK[TEMP].OFF;
                   do {
                      GETCHAR();
                      if (CH == '#')
                         {
                         SKIP('#',';'); GETCHAR();
                         }
                      if (CH == ',') PARNUM = PARNUM - 1;
                      } while (!((PARNUM == 0) || (CH == ';')));
                   if (CH == ';') POP();
                break;

         case ',':  case ';'  : POP();  break;

         }
      } while (CH != '$');
   return 0;
   }




int NUM (char CH)
   {
      return ((int)CH - (int)'A' + 1);
   }

int VAL (char CH)
   {
      return ((int)CH - (int)'0');
   }

void GETCHAR (void)
   {
      CHPOS = CHPOS + 1; CH = PROG[CHPOS];
   }

void PUSHCAL (int DATUM)
   {
      CAL = CAL + 1; CALSTACK[CAL] = DATUM;
   }

int POPCAL(void)
   {
      int temp;

      temp = CALSTACK[CAL]; CAL = CAL - 1;
      return (temp);
   }

void PUSH (enum TAGTYPE TAGVAL)
   {
      LEVEL = LEVEL + 1;
      STACK[LEVEL].TAG = TAGVAL;
      STACK[LEVEL].POS = CHPOS;
      STACK[LEVEL].OFF = OFFSET;
   }

void POP (void)
   {
      CHPOS = STACK[LEVEL].POS;
      OFFSET = STACK[LEVEL].OFF;
      LEVEL = LEVEL - 1;
   }

void SKIP (char LCH, char RCH)
   {
      int CNT;

      CNT = 1;
      do {
         GETCHAR();
         if (CH == LCH)
            CNT = CNT + 1;
         else if (CH == RCH)
            CNT = CNT - 1;
         } while (CNT != 0);
   }

void LOAD (void)
   {
      char THIS, LAST; int CHARNUM;
      char IN=0;

      for (CHARNUM = 1; CHARNUM <= 26; CHARNUM++) DEFINITIONS[CHARNUM] = 0;
      CHARNUM = 0; THIS = ' ';
      do {
         LAST = THIS; fread (&THIS, 1, 1, fp);
         if (THIS == '\'')
            {
            do {
               fread (&THIS, 1, 1, fp);
               } while (THIS != '\n');
            fread (&THIS, 1, 1, fp);
            }
         CHARNUM = CHARNUM + 1; PROG[CHARNUM] = THIS;
         if ((THIS >= 'A') && (THIS <= 'Z') && (LAST == '$'))
            DEFINITIONS[NUM(THIS)] = CHARNUM;
         if (THIS == '\"') IN = !IN;
         if (!(!strchr(" \t\n\r",THIS) || IN ||
            (LAST >= '0' && LAST <= '9'))) CHARNUM--;
         } while (!((THIS == '$') && (LAST == '$')));
   }





/*****************************************************************************/
/*  chomp()                                                                  */
/*                                                                           */
/*  Remove final \n from end of string.                                      */
/*****************************************************************************/

void chomp (char *str)
{
int  len;                                   /* length of str (incl \n)       */

len = strlen (str);                         /* get length of str incl \n     */
if (str[len-1] == '\n')                     /* if final char is \n ..        */
   str[len-1] = '\0';                       /* ..then remove it              */
}

