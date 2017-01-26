
main (t) {
/*  for(t=20;usleep(500000)|t++^36;)printf("%d\n",++t*2);

  char f, *g = ",048<@DH";
  while (f = *g++) {
    printf("%d\n", f + usleep(500000));
  }*/

  char h, *i = "44\n46\n48\n50\n52\n54\n56\n58\n60\n62\n64\n66\n68\n70\n72";
  while (h = *i++) {
    putchar(h + (h ^ 10 ? usleep(500000) : 0));
  }
}
