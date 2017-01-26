import std.stdio;
import std.process;

void main() {
  try {
    spawnProcess(["/dev/null"]);
  } catch (Throwable p) {
    writeln("asd");
  }
}
