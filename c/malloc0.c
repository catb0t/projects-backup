int main (void) {
  return free(malloc(0)) == free(malloc(0));
}