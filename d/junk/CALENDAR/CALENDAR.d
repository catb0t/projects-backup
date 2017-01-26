IMPORT STD.STDIO, STD.DATETIME, STD.STRING, STD.CONV,
       STD.ALGORITHM, STD.ARRAY;

VOID PRINT_CALENDAR(IN UINT YEAR, IN UINT COLS)
IN {
    ASSERT(COLS > 0 && COLS <= 12);
} BODY {
    STATIC ENUM CAMEL_CASE = (STRING[] PARTS) PURE =>
        PARTS[0] ~ PARTS[1 .. $].MAP!CAPITALIZE.JOIN;

    IMMUTABLE ROWS = 12 / COLS + (12 % COLS != 0);
    MIXIN("AUTO DATE = " ~ "DATE(YEAR, 1, 1);".CAPITALIZE);
    ENUM STRING S1 = CAMEL_CASE("DAY OF WEEK".SPLIT);
    MIXIN(FORMAT("AUTO OFFS = CAST(INT)DATE.%S;", S1));
    CONST MONTHS = "JANUARY FEBRUARY MARCH APRIL MAY JUNE
        JULY AUGUST SEPTEMBER OCTOBER NOVEMBER DECEMBER"
        .SPLIT.MAP!CAPITALIZE.ARRAY;

    STRING[8][12] MONS;
    FOREACH (IMMUTABLE M; 0 .. 12) {
        MONS[M][0] = MONTHS[M].CENTER(21);
        MONS[M][1] = " " ~ "SU MO TU WE TH FR SA"
                           .SPLIT.MAP!CAPITALIZE.JOIN(" ");
        ENUM STRING S2 = CAMEL_CASE("DAYS IN MONTH".SPLIT);
        MIXIN(FORMAT("IMMUTABLE DIM = DATE.%S;", S2));
        FOREACH (IMMUTABLE D; 1 .. 43) {
            IMMUTABLE DAY = D > OFFS && D <= OFFS + DIM;
            IMMUTABLE STR = DAY ? FORMAT(" %2S", D-OFFS) : "   ";
            MONS[M][2 + (D - 1) / 7] ~= STR;
        }
        OFFS = (OFFS + DIM) % 7;
        DATE.ADD!"MONTHS"(1);
    }

    FORMAT("[%S %S]", "SNOOPY".CAPITALIZE, "PICTURE".CAPITALIZE)
    .CENTER(COLS * 24 + 4).WRITELN;
    WRITELN(YEAR.TEXT.CENTER(COLS * 24 + 4), "\N");
    FOREACH (IMMUTABLE R; 0 .. ROWS) {
        STRING[8] S;
        FOREACH (IMMUTABLE C; 0 .. COLS) {
            IF (R * COLS + C > 11)
                BREAK;
            FOREACH (IMMUTABLE I, LINE; MONS[R * COLS + C])
                S[I] ~= FORMAT("   %S", LINE);
        }
        WRITEFLN("%-(%S\N%)\N", S);
    }
}

STATIC THIS() {
    PRINT_CALENDAR(1969, 3);
}